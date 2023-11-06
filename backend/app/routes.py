# backend/app/routes.py
import subprocess  # Import the subprocess module
from flask import Blueprint, jsonify, current_app
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta

main = Blueprint('main', __name__)  # initialize Blueprint object with name 'main'

last_creation_time = None  # Global variable to store the last creation timestamp

def run_cleanup_script():
    try:
        subprocess.run(['python3', 'app/cleanup_sheets_from_api.py'], check=True)  # Run the cleanup script
        current_app.logger.info('Cleanup script executed successfully')
    except subprocess.CalledProcessError as e:
        current_app.logger.error(f'An error occurred while executing the cleanup script: {e}')

@main.route('/generate-sheet', methods=['POST'])
def generate_sheet():
    global last_creation_time  # Declare the global variable
    current_time = datetime.utcnow()  # Get the current time
    
    # Check if the last creation time is within the specified timeframe (e.g., 10 minutes)
    if last_creation_time and (current_time - last_creation_time).total_seconds() < 600:
        return jsonify({'error': 'A sheet was already created within the last 10 minutes. Please try again later.'}), 429
    
    last_creation_time = current_time  # Update the last creation time
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

        # Schedule the execution of the cleanup script
        scheduler = current_app.config['SCHEDULER']  # Get the scheduler from the app config
        scheduler.add_job(run_cleanup_script, 'date', run_date=datetime.utcnow() + timedelta(hours=1))  # Schedule the execution of the cleanup script in 1 hour

        # Construct the URL
        spreadsheet_url = f'https://docs.google.com/spreadsheets/d/{file_id}'

        return jsonify({'spreadsheetUrl': spreadsheet_url}), 200

    except HttpError as error: # If there's an error with the HTTP request (e.g. invalid credentials):
        current_app.logger.error('An error occurred: %s', error, exc_info=True) # Log statement with error and traceback info (exc_info) 
        return jsonify({'error': 'Failed to generate or share the sheet'}), 500 # Return a JSON response with a 500 status code (server error) and an error message 
    except Exception as e: # If there's any other error: 
        current_app.logger.error('An error occurred: %s', e, exc_info=True) # Log statement with error and traceback info (exc_info) 
        return jsonify({'error': str(e)}), 500 # Return a JSON response with a 500 status code (server error) and an error message