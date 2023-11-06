from googleapiclient.discovery import build
from google.oauth2 import service_account

# Load the credentials
creds = service_account.Credentials.from_service_account_file(
    'app/credentials.json'
)

# Build the Drive API client
drive_service = build('drive', 'v3', credentials=creds)

# The email address of the service account
service_account_email = 'generator-service-account@swift-adviser-404201.iam.gserviceaccount.com'

def delete_file(file_id):
    try:
        drive_service.files().delete(fileId=file_id).execute()
        print(f'Deleted file {file_id}')
    except Exception as e:
        print(f'An error occurred: {e}')

# List files in Drive
results = drive_service.files().list(
    q=f"'{service_account_email}' in writers and mimeType='application/vnd.google-apps.spreadsheet'",
    pageSize=10,
    fields="nextPageToken, files(id, name)"
).execute()

# Delete the files and print the file names and IDs
for file in results.get('files', []):
    print(f'Deleting {file["name"]} ({file["id"]})')
    delete_file(file["id"])
