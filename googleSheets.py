import os.path
import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]




def sheets():
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "client_secret.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

 
  service = build("sheets", "v4", credentials=creds)

  # Call the Sheets API
  sheet = service.spreadsheets()
  result = (
      sheet.values()
      .get(spreadsheetId="1G_-5eptKriUjYI34quNpjISDPC9VBgDf5ZI6_UD4yv8", range="engenharia_de_software!A1:H27")
      .execute()
  )
  values = result.get("values", [])
  return values     


def upDateSheets(situacao,naf):
    # Carrega as credenciais
    creds = Credentials.from_authorized_user_file('token.json')

    # Inicia o serviço do Google Sheets
    service = build('sheets', 'v4', credentials=creds)

    # Define o ID da planilha e a faixa de células para a situação (coluna G, linhas 4 a 27)
    situacao_range = 'engenharia_de_software!G4:G27'

    # Atualiza a situação
    update_situacao = service.spreadsheets().values().update(
        spreadsheetId='1G_-5eptKriUjYI34quNpjISDPC9VBgDf5ZI6_UD4yv8',
        range=situacao_range,
        valueInputOption='USER_ENTERED',
        body={'values': situacao}
    ).execute()

    # Define o ID da planilha e a faixa de células para o NAF (coluna H, linhas 4 a 27)
    naf_range = 'engenharia_de_software!H4:H27'

    # Atualiza o NAF
    update_naf = service.spreadsheets().values().update(
        spreadsheetId='1G_-5eptKriUjYI34quNpjISDPC9VBgDf5ZI6_UD4yv8',
        range=naf_range,
        valueInputOption='USER_ENTERED',
        body={'values': naf}
    ).execute()
