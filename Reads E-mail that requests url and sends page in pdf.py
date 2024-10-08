import imaplib
import email
from email.header import decode_header
from pyhtml2pdf import converter
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

if __name__ == "__main__":
    urls = [] #vector to store urls
    imap_url = 'imap.gmail.com'
    mail = imaplib.IMAP4_SSL(imap_url)
    with open("e-mail.txt", "r") as f:
        usuario = f.readline()
        senha = f.readline()
        f.close()
    mail.login(usuario, senha)
    mail.select("INBOX")
    _, emails_selecionados = mail.search(None, '(BODY "urlreq:")') #searches for e-mails that has "urlreq", short for url requisition 
    print("Requisição de url:", len(emails_selecionados[0].split())) #prints how many e-mails that request url
    #prints e-mails that has "urlreq" in text
    for num in emails_selecionados[0].split():
        _, data = mail.fetch(num, '(RFC822)')
        _, bytes_data = data[0]
        email_message = email.message_from_bytes(bytes_data)
        print("\n===========================================")
        assunto = email_message["subject"]
        decoded_subject, encoding = decode_header(assunto)[0]
        if isinstance(decoded_subject, bytes):
            decoded_subject = decoded_subject.decode(encoding or 'utf-8')
            print("Subject: ", decoded_subject)
        print("To:", email_message["to"])
        print("From: ", email_message["from"])
        print("Date: ", email_message["date"])
        for part in email_message.walk():
            if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
                message = part.get_payload(decode=True)
                print("Message: \n", message.decode())
                temp = message.split()
                #stores url in the vector
                for tem in temp:
                    if tem.decode('utf-8').startswith("https://"):
                        urls.append(tem.decode('utf-8'))
    #iterates the urls, get the pdf and send to the selected e-mail
    for url in urls:
        print(url)
        nome_url = url.replace("/", "")
        nome_url = nome_url.replace("?", "")
        nome_url = nome_url.replace("=", "")
        nome_url = nome_url.replace(":", "")
        nome_url = nome_url.replace("_", "")
        print("==========================================\n")
        diretorio_trabalho = f"C:\\Users\\Administrator\\PycharmProjects\\Utilities\\{nome_url}.pdf"
        converter.convert(url, diretorio_trabalho)
        for mensagem in emails_selecionados[0].split():
            mail.store(mensagem, "+FLAGS", '\\Deleted')
        mail.expunge()
        with open("e-mail.txt", "r") as f:
            remetente_email = f.readline()
            remetente_senha = f.readline()
            destinatario_email = f.readline() #MUDAR ISTO
            f.close()
        smtp_servidor = "smtp.gmail.com"
        smtp_porta = 587
        mensagem = MIMEMultipart()
        mensagem['From'] = remetente_email
        mensagem['To'] = destinatario_email
        mensagem['Subject'] = "Página solicitada"
        mensagem_texto = "Página solicitada:"
        corpo_email = f"{mensagem_texto}\n"
        mensagem.attach(MIMEText(corpo_email, 'plain'))
        arquivo_pdf = diretorio_trabalho
        anexo = open(arquivo_pdf, "rb")
        parte = MIMEBase("application", "pdf")
        parte.set_payload(anexo.read())
        encoders.encode_base64(parte)
        parte.add_header("Content-Disposition", f"attachment; filename= {arquivo_pdf}")
        mensagem.attach(parte)
        try:
            servidor = smtplib.SMTP(smtp_servidor, smtp_porta)
            servidor.starttls()
            servidor.login(remetente_email, remetente_senha)
            servidor.sendmail(remetente_email, destinatario_email, mensagem.as_string())
            servidor.quit()
            print("E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")
