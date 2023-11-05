# backend/app/routes.py
from flask import Blueprint, jsonify, current_app
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta

main = Blueprint('main', __name__) # initialize Blueprint object with name 'main' 

def delete_sheet(file_id):
    try:
        creds = service_account.Credentials.from_service_account_file('app/credentials.json') # Your credentials file path
        drive_service = build('drive', 'v3', credentials=creds) # Build the service object
        drive_service.files().delete(fileId=file_id).execute() # Delete the file by ID
        current_app.logger.info(f'Deleted file with ID {file_id}') # Log statement with file ID
    except Exception as e:
        current_app.logger.error(f'An error occurred: {e}') # Log statement with error

@main.route('/generate-sheet', methods=['POST']) 
def generate_sheet(): 
    current_app.logger.info('generate_sheet called')  # Log statement
    creds = service_account.Credentials.from_service_account_file(
            'app/credentials.json') # Your credentials file path
    drive_service = build('drive', 'v3', credentials=creds)

    # Use your actual template file ID
    template_file_id = '1izfmsZdhXQhJy1ntrI0BMrRxEXNmWN846EbKXSr55QQ' # Template file ID

    copied_file = {
        'name': 'Work Attendance Calculation Sheet' # Name of the new file
    }
    try:
        # Copy the template file to the new file
        
        result = drive_service.files().copy(  # pylint: disable=maybe-no-member
            fileId=template_file_id,
            body=copied_file 
        ).execute()
        file_id = result.get('id') # Get the ID of the new file

        # Set the permissions to 'Anyone with the link'
        permission = {
            'type': 'anyone',
            'role': 'reader',
        }
        drive_service.permissions().create(
            fileId=file_id,
            body=permission,
            fields='id',
        ).execute() 
 
        # Schedule the deletion of the sheet
        scheduler = current_app.config['SCHEDULER'] # Get the scheduler from the app config 
        scheduler.add_job(delete_sheet, 'date', run_date=datetime.utcnow() + timedelta(hours=1), args=[file_id]) # Schedule the deletion of the sheet in 1 hour 

        # Construct the URL
        spreadsheet_url = f'https://docs.google.com/spreadsheets/d/{file_id}'

        return jsonify({'spreadsheetUrl': spreadsheet_url}), 200

    except HttpError as error: # If there's an error with the HTTP request (e.g. invalid credentials):
        current_app.logger.error('An error occurred: %s', error, exc_info=True) # Log statement with error and traceback info (exc_info) 
        return jsonify({'error': 'Failed to generate or share the sheet'}), 500 # Return a JSON response with a 500 status code (server error) and an error message 
    except Exception as e: # If there's any other error: 
        current_app.logger.error('An error occurred: %s', e, exc_info=True) # Log statement with error and traceback info (exc_info) 
        return jsonify({'error': str(e)}), 500 # Return a JSON response with a 500 status code (server error) and an error message