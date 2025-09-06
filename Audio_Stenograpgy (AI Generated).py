# -*- coding: utf-8 -*-


import sys
import os
import subprocess
import threading
import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq


from PyQt6.QtWidgets import (
   QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
   QPushButton, QLabel, QTextEdit, QLineEdit, QFileDialog, QMessageBox,


   QDialog
)
from PyQt6.QtCore import Qt, QObject, pyqtSignal, QThread


# ==============================================================================
# CONSTANTES E MAPEAMENTO DE SÍMBOLOS
# ==============================================================================


# ALTURA_SENOIDE: Aumentada para criar um sinal mais robusto e detectável.
ALTURA_SENOIDE = 0.01
# DURACAO: Aumentada para melhorar a precisão da decodificação do FFT.
DURACAO = 0.1
FREQUENCIA_AMOSTRAS = 8000
# MAGNITUDE_THRESHOLD: Filtro de ruído. Ignora picos de frequência fracos.
# Este valor pode precisar de ajuste dependendo do ruído de fundo.
MAGNITUDE_THRESHOLD = 50000


# Mapeamento binário -> frequência
frequencia_inicial = 200
frequencia_final = 4000
alfabeto = [format(c, '08b') for c in range(256)]
passo = (frequencia_final - frequencia_inicial) / (len(alfabeto) - 1)
mapeamento_de_simbolos = {
   letra: frequencia_inicial + i * passo for i, letra in enumerate(alfabeto)
}
# Criamos um mapa reverso para facilitar a decodificação
mapeamento_reverso = {v: k for k, v in mapeamento_de_simbolos.items()}


# --- Caminho para o FFMPEG ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FFMPEG_EXE = os.path.join(BASE_DIR, 'ffmpeg', 'bin', 'ffmpeg.exe')


# --- Estilo da Aplicação (QSS) ---
STYLESHEET = """
QWidget {
   background-color: #2E3440;
   color: #D8DEE9;
   font-family: "Segoe UI", Arial, sans-serif;
   font-size: 14px;
}
QMainWindow, QDialog {
   background-color: #2E3440;
}
QLabel#welcomeLabel {
   font-size: 28px;
   font-weight: bold;
   color: #88C0D0;
}
QLabel#statusLabel {
   color: #A3BE8C;
}
QPushButton {
   background-color: #5E81AC;
   color: #ECEFF4;
   border: none;
   padding: 10px 20px;
   border-radius: 5px;
   font-size: 16px;
}
QPushButton:hover {
   background-color: #81A1C1;
}
QPushButton:pressed {
   background-color: #4C566A;
}
QLineEdit, QTextEdit {
   background-color: #3B4252;
   border: 1px solid #4C566A;
   border-radius: 4px;
   padding: 8px;
   color: #ECEFF4;
}
"""




# ==============================================================================
# WORKER THREADS PARA EVITAR TRAVAMENTO DA GUI
# ==============================================================================


class WorkerSignals(QObject):
   finished = pyqtSignal()
   error = pyqtSignal(str)
   success = pyqtSignal(str)
   progress = pyqtSignal(str)




class EncryptWorker(QObject):
   def __init__(self, text, mp3_path, output_path):
       super().__init__()
       self.signals = WorkerSignals()
       self.text = text
       self.mp3_path = mp3_path
       self.output_path = output_path
       self.temp_wav_path = os.path.join(BASE_DIR, "temp_data.wav")


   def run(self):
       try:
           self.signals.progress.emit("Gerando arquivo WAV a partir do texto...")
           self._generate_wav_from_text(self.text, self.temp_wav_path)


           self.signals.progress.emit("Combinando áudios com FFMPEG...")
           self._combine_audio(self.temp_wav_path, self.mp3_path, self.output_path)


           if os.path.exists(self.temp_wav_path):
               os.remove(self.temp_wav_path)


           self.signals.success.emit(f"Arquivo '{os.path.basename(self.output_path)}' criado com sucesso!")
       except Exception as e:
           if os.path.exists(self.temp_wav_path):
               os.remove(self.temp_wav_path)
           self.signals.error.emit(f"Ocorreu um erro: {str(e)}")
       finally:
           self.signals.finished.emit()


   def _generate_wav_from_text(self, text, output_filename):
       # A amplitude é baseada na constante fornecida
       amplitude = np.iinfo(np.int16).max * ALTURA_SENOIDE


       # Gera a base de tempo para um único caractere
       t = np.linspace(0., DURACAO, int(FREQUENCIA_AMOSTRAS * DURACAO), endpoint=False)


       signal = np.array([], dtype=np.int16)


       # Para cada caractere no texto, encontra a frequência e gera a onda
       for char in text:
           binary_char = format(ord(char), '08b')
           if binary_char in mapeamento_de_simbolos:
               freq = mapeamento_de_simbolos[binary_char]
               wave_segment = amplitude * np.sin(2. * np.pi * freq * t)
               signal = np.append(signal, wave_segment)


       if len(signal) == 0:
           raise ValueError("O texto de entrada não produziu nenhum dado de áudio.")


       wavfile.write(output_filename, FREQUENCIA_AMOSTRAS, signal.astype(np.int16))


   def _combine_audio(self, wav_path, mp3_path, output_path):
       command = [
           FFMPEG_EXE, '-y',
           '-i', wav_path,
           '-stream_loop', '-1', '-i', mp3_path,
           '-map', '1:a:0', '-map', '0:a:0',
           '-c:a', 'aac', '-b:a', '192k',
           '-shortest', output_path
       ]
       result = subprocess.run(command, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
       if result.returncode != 0:
           raise RuntimeError(f"Erro no FFMPEG: {result.stderr}")




class DecryptWorker(QObject):
   def __init__(self, mp4_path):
       super().__init__()
       self.signals = WorkerSignals()
       self.mp4_path = mp4_path
       self.extracted_wav_path = os.path.join(BASE_DIR, "extracted_data.wav")


   def run(self):
       try:
           self.signals.progress.emit("Extraindo faixa de dados do arquivo MP4...")
           self._extract_hidden_track(self.mp4_path, self.extracted_wav_path)


           self.signals.progress.emit("Analisando áudio e recuperando texto...")
           original_text = self._recover_text_from_wav(self.extracted_wav_path)


           if os.path.exists(self.extracted_wav_path):
               os.remove(self.extracted_wav_path)


           self.signals.success.emit(original_text)
       except Exception as e:
           if os.path.exists(self.extracted_wav_path):
               os.remove(self.extracted_wav_path)
           self.signals.error.emit(f"Ocorreu um erro: {str(e)}")
       finally:
           self.signals.finished.emit()


   def _extract_hidden_track(self, mp4_path, output_wav_path):
       command = [
           FFMPEG_EXE, '-y',
           '-i', mp4_path,
           '-map', '0:a:1',
           '-acodec', 'pcm_s16le',
           '-ar', str(FREQUENCIA_AMOSTRAS),  # Garante a mesma taxa de amostragem
           output_wav_path
       ]
       result = subprocess.run(command, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
       if result.returncode != 0:
           raise RuntimeError(f"Erro no FFMPEG ao extrair áudio: {result.stderr}")


   def _recover_text_from_wav(self, wav_path):
       rate, data = wavfile.read(wav_path)
       if rate != FREQUENCIA_AMOSTRAS:
           raise ValueError(f"Taxa de amostragem incorreta! Esperado {FREQUENCIA_AMOSTRAS}, obtido {rate}")


       samples_per_char = int(DURACAO * rate)
       num_chunks = len(data) // samples_per_char


       recovered_chars = []


       for i in range(num_chunks):
           chunk = data[i * samples_per_char: (i + 1) * samples_per_char]


           # FFT para encontrar a frequência dominante
           yf = fft(chunk)
           xf = fftfreq(len(chunk), 1 / rate)


           # Pega a frequência correspondente à maior amplitude no espectro positivo
           idx = np.argmax(np.abs(yf[:len(chunk) // 2]))


           # Aplica o filtro de ruído (Threshold)
           if np.abs(yf[idx]) < MAGNITUDE_THRESHOLD:
               continue  # Ignora este chunk por ser considerado ruído/silêncio


           detected_freq = abs(xf[idx])


           # Encontra o símbolo mais próximo da frequência detectada
           # Isso busca a frequência mais próxima no nosso dicionário
           closest_freq = min(mapeamento_reverso.keys(), key=lambda f: abs(f - detected_freq))
           binary_char = mapeamento_reverso[closest_freq]


           # Converte o binário para caractere
           char_code = int(binary_char, 2)
           recovered_chars.append(chr(char_code))


       return "".join(recovered_chars)




# ==============================================================================
# JANELAS DA INTERFACE GRÁFICA (GUI) - Sem grandes alterações
# ==============================================================================


class ResultDialog(QDialog):
   def __init__(self, text, parent=None):
       super().__init__(parent)
       self.setWindowTitle("Mensagem Recuperada")
       self.setMinimumSize(600, 400)


       layout = QVBoxLayout(self)
       label = QLabel("A mensagem recuperada do arquivo é:")
       layout.addWidget(label)


       self.text_display = QTextEdit()
       self.text_display.setReadOnly(True)
       self.text_display.setText(text)
       layout.addWidget(self.text_display)


       close_button = QPushButton("Fechar")
       close_button.clicked.connect(self.accept)
       layout.addWidget(close_button, alignment=Qt.AlignmentFlag.AlignRight)
       self.setLayout(layout)




class EncryptWindow(QWidget):
   def __init__(self):
       super().__init__()
       self.setWindowTitle("Criptografar Mensagem")
       self.setMinimumSize(600, 500)


       layout = QVBoxLayout(self);
       layout.setSpacing(15)
       self.msg_input = QTextEdit();
       self.msg_input.setPlaceholderText("Sua mensagem secreta aqui...")
       self.mp3_path_input = QLineEdit();
       self.mp3_path_input.setReadOnly(True)
       self.mp3_select_button = QPushButton("Procurar MP3...");
       self.mp3_select_button.clicked.connect(self.select_mp3)
       mp3_layout = QHBoxLayout();
       mp3_layout.addWidget(self.mp3_path_input);
       mp3_layout.addWidget(self.mp3_select_button)
       self.encrypt_button = QPushButton("Criptografar e Gerar MP4");
       self.encrypt_button.clicked.connect(self.start_process)
       self.status_label = QLabel("");
       self.status_label.setObjectName("statusLabel")


       layout.addWidget(QLabel("Digite a mensagem a ser escondida:"))
       layout.addWidget(self.msg_input)
       layout.addWidget(QLabel("Selecione o arquivo de áudio MP3 para disfarce:"))
       layout.addLayout(mp3_layout)
       layout.addStretch()
       layout.addWidget(self.status_label)
       layout.addWidget(self.encrypt_button)
       self.setLayout(layout)


   def select_mp3(self):
       file_name, _ = QFileDialog.getOpenFileName(self, "Selecionar MP3", "", "Arquivos MP3 (*.mp3)")
       if file_name: self.mp3_path_input.setText(file_name)


   def start_process(self):
       text, mp3_path = self.msg_input.toPlainText(), self.mp3_path_input.text()
       if not text: QMessageBox.warning(self, "Aviso", "Por favor, digite uma mensagem."); return
       if not mp3_path: QMessageBox.warning(self, "Aviso", "Por favor, selecione um arquivo MP3."); return
       if not os.path.exists(FFMPEG_EXE): QMessageBox.critical(self, "Erro Crítico",
                                                               f"FFMPEG não encontrado em:\n{FFMPEG_EXE}"); return


       output_path, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo MP4", "", "Arquivos MP4 (*.mp4)")
       if not output_path: return


       self.encrypt_button.setEnabled(False);
       self.status_label.setText("Iniciando processo...")
       self.thread, self.worker = QThread(), EncryptWorker(text, mp3_path, output_path)
       self.worker.moveToThread(self.thread)
       self.thread.started.connect(self.worker.run)
       self.worker.signals.finished.connect(self.thread.quit);
       self.worker.signals.finished.connect(self.worker.deleteLater)
       self.thread.finished.connect(self.thread.deleteLater)
       self.worker.signals.progress.connect(lambda msg: self.status_label.setText(msg))
       self.worker.signals.error.connect(self.process_error)
       self.worker.signals.success.connect(self.process_success)
       self.thread.start()


   def process_finished(self):
       self.encrypt_button.setEnabled(True); self.status_label.setText("")


   def process_error(self, err):
       self.process_finished(); QMessageBox.critical(self, "Erro", err)


   def process_success(self, msg):
       self.process_finished(); QMessageBox.information(self, "Sucesso", msg); self.close()




class DecryptWindow(QWidget):
   def __init__(self):
       super().__init__()
       self.setWindowTitle("Descriptografar Mensagem")
       self.setMinimumSize(600, 300)


       layout = QVBoxLayout(self);
       layout.setSpacing(15)
       self.mp4_path_input = QLineEdit();
       self.mp4_path_input.setReadOnly(True)
       self.mp4_select_button = QPushButton("Procurar MP4...");
       self.mp4_select_button.clicked.connect(self.select_mp4)
       mp4_layout = QHBoxLayout();
       mp4_layout.addWidget(self.mp4_path_input);
       mp4_layout.addWidget(self.mp4_select_button)
       self.mp3_path_input = QLineEdit();
       self.mp3_path_input.setReadOnly(True)  # Apenas para seguir o fluxo do usuário
       self.mp3_select_button = QPushButton("Procurar MP3 original...");
       self.mp3_select_button.clicked.connect(self.select_mp3)
       mp3_layout = QHBoxLayout();
       mp3_layout.addWidget(self.mp3_path_input);
       mp3_layout.addWidget(self.mp3_select_button)
       self.decrypt_button = QPushButton("Recuperar Mensagem");
       self.decrypt_button.clicked.connect(self.start_process)
       self.status_label = QLabel("");
       self.status_label.setObjectName("statusLabel")


       layout.addWidget(QLabel("Selecione o arquivo MP4 que contém a mensagem:"))
       layout.addLayout(mp4_layout)
       layout.addWidget(QLabel("Selecione o arquivo MP3 original (usado na criação):"))
       layout.addLayout(mp3_layout)
       layout.addStretch()
       layout.addWidget(self.status_label)
       layout.addWidget(self.decrypt_button)
       self.setLayout(layout)


   def select_mp4(self):
       file_name, _ = QFileDialog.getOpenFileName(self, "Selecionar MP4", "", "Arquivos MP4 (*.mp4)")
       if file_name: self.mp4_path_input.setText(file_name)


   def select_mp3(self):
       file_name, _ = QFileDialog.getOpenFileName(self, "Selecionar MP3", "", "Arquivos MP3 (*.mp3)")
       if file_name: self.mp3_path_input.setText(file_name)


   def start_process(self):
       mp4_path, mp3_path = self.mp4_path_input.text(), self.mp3_path_input.text()
       if not mp4_path or not mp3_path: QMessageBox.warning(self, "Aviso",
                                                            "Por favor, selecione ambos os arquivos."); return
       if not os.path.exists(FFMPEG_EXE): QMessageBox.critical(self, "Erro Crítico",
                                                               f"FFMPEG não encontrado em:\n{FFMPEG_EXE}"); return


       self.decrypt_button.setEnabled(False);
       self.status_label.setText("Iniciando recuperação...")
       self.thread, self.worker = QThread(), DecryptWorker(mp4_path)
       self.worker.moveToThread(self.thread)
       self.thread.started.connect(self.worker.run)
       self.worker.signals.finished.connect(self.thread.quit);
       self.worker.signals.finished.connect(self.worker.deleteLater)
       self.thread.finished.connect(self.thread.deleteLater)
       self.worker.signals.progress.connect(lambda msg: self.status_label.setText(msg))
       self.worker.signals.error.connect(self.process_error)
       self.worker.signals.success.connect(self.process_success)
       self.thread.start()


   def process_finished(self):
       self.decrypt_button.setEnabled(True); self.status_label.setText("")


   def process_error(self, err):
       self.process_finished(); QMessageBox.critical(self, "Erro", err)


   def process_success(self, text):
       self.process_finished()
       if not text.strip():
           QMessageBox.warning(self, "Concluído", "Nenhuma mensagem de texto foi encontrada.")
       else:
           ResultDialog(text, self).exec()
       self.close()




class MainWindow(QMainWindow):
   def __init__(self):
       super().__init__()
       self.setWindowTitle("Audio Steganographer V2")
       self.setFixedSize(500, 300)
       self.central_widget = QWidget()
       self.setCentralWidget(self.central_widget)
       layout = QVBoxLayout(self.central_widget)
       layout.setAlignment(Qt.AlignmentFlag.AlignCenter);
       layout.setSpacing(20)
       welcome_label = QLabel("Bem-vindo!");
       welcome_label.setObjectName("welcomeLabel");
       welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
       encrypt_button = QPushButton("Criptografar Mensagem");
       encrypt_button.clicked.connect(self.open_encrypt_window)
       decrypt_button = QPushButton("Descriptografar Mensagem");
       decrypt_button.clicked.connect(self.open_decrypt_window)
       layout.addWidget(welcome_label);
       layout.addWidget(encrypt_button);
       layout.addWidget(decrypt_button)
       self.encrypt_win = None;
       self.decrypt_win = None


   def open_encrypt_window(self):
       if self.encrypt_win is None or not self.encrypt_win.isVisible(): self.encrypt_win = EncryptWindow(); self.encrypt_win.show()


   def open_decrypt_window(self):
       if self.decrypt_win is None or not self.decrypt_win.isVisible(): self.decrypt_win = DecryptWindow(); self.decrypt_win.show()




if __name__ == '__main__':
   if not os.path.exists(FFMPEG_EXE):
       app = QApplication(sys.argv)
       QMessageBox.critical(None, "Erro Crítico de Inicialização",
                            f"O FFMPEG não foi encontrado em:\n{FFMPEG_EXE}\nVerifique a instalação.")
       sys.exit(1)


   app = QApplication(sys.argv)
   app.setStyleSheet(STYLESHEET)
   window = MainWindow()
   window.show()
   sys.exit(app.exec())

