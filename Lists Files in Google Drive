import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

#autenticate service
def carregar_creds():
    global arquivo_credenciais
    dados_credenciais = os.getcwd() + r"\credentials.json" #credentials.json file location
    try:
        credenciais = service_account.Credentials.from_service_account_file(dados_credenciais, scopes=['https://www.googleapis.com/auth/drive']) #create creds
        return credenciais
    except Exception as e:
        print(e)

#create service
def criar_servico(credenciais):
    try:
        servico = build("drive", "v3", credentials=credenciais) #build
        return servico
    except Exception as e:
        print(e)

#lists files
def find_folder_id(servico, folder_name):
    # Search for folders with the given name
    query = f"name='{folder_name}' and trashed=false" #name of the file. Trashed=false ignores deleted files
    response = servico.files().list(q=query, fields="files(name, mimeType)", pageSize=1000).execute() #lists files with service build in criar_servico
    print(response) #prints response. Optional
    # Check if any folders were found
    folders = response.get('files', []) #gets response
    for folder in folders:
        print(folder['name']) #prints folders found

if __name__ == "__main__":
    credenciais = carregar_creds() #loads creds
    servico = criar_servico(credenciais) #builds service
    folder_name = "prompt" #put folder name here
    find_folder_id(servico, folder_name)
