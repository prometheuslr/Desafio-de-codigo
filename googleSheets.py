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


def upDateSheets(status,finalGrade):
    # Load credentials
    creds = Credentials.from_authorized_user_file('token.json')

    # Initialize Google Sheets service
    service = build('sheets', 'v4', credentials=creds)

    # Define the spreadsheet ID and cell range for status (column G, rows 4 to 27)
    status_range = 'engenharia_de_software!G4:G27'

    # Update status
    update_status = service.spreadsheets().values().update(
        spreadsheetId='1G_-5eptKriUjYI34quNpjISDPC9VBgDf5ZI6_UD4yv8',
        range=status_range,
        valueInputOption='USER_ENTERED',
        body={'values': status}
    ).execute()

    # Define the spreadsheet ID and cell range for finalGrade (column H, rows 4 to 27)
    finalGrade_range = 'engenharia_de_software!H4:H27'

    # Update finalGrade
    update_finalGrade = service.spreadsheets().values().update(
        spreadsheetId='1G_-5eptKriUjYI34quNpjISDPC9VBgDf5ZI6_UD4yv8',
        range=finalGrade_range,
        valueInputOption='USER_ENTERED',
        body={'values': finalGrade}
    ).execute()
