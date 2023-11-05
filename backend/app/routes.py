# backend/app/routes.py
from flask import Blueprint, jsonify, current_app
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta

main = Blueprint('main', __name__)

def delete_sheet(file_id):
    try:
        creds = service_account.Credentials.from_service_account_file('app/credentials.json')
        drive_service = build('drive', 'v3', credentials=creds)
        drive_service.files().delete(fileId=file_id).execute()
        current_app.logger.info(f'Deleted file with ID {file_id}')
    except Exception as e:
        current_app.logger.error(f'An error occurred: {e}')

@main.route('/generate-sheet', methods=['POST'])
def generate_sheet():
    current_app.logger.info('generate_sheet called')  # Log statement
    creds = service_account.Credentials.from_service_account_file(
            'app/credentials.json')
    drive_service = build('drive', 'v3', credentials=creds)

    # Use your actual template file ID
    template_file_id = '1izfmsZdhXQhJy1ntrI0BMrRxEXNmWN846EbKXSr55QQ'

    copied_file = {
        'name': 'Work Attendance Sheet'
    }
    try:
        # Copy the template file
        result = drive_service.files().copy(
            fileId=template_file_id,
            body=copied_file
        ).execute()
        file_id = result.get('id')

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
        scheduler = current_app.config['SCHEDULER']
        scheduler.add_job(delete_sheet, 'date', run_date=datetime.utcnow() + timedelta(hours=1), args=[file_id])

        # Construct the URL
        spreadsheet_url = f'https://docs.google.com/spreadsheets/d/{file_id}'

        return jsonify({'spreadsheetUrl': spreadsheet_url}), 200

    except HttpError as error:
        current_app.logger.error('An error occurred: %s', error, exc_info=True)
        return jsonify({'error': 'Failed to generate or share the sheet'}), 500
    except Exception as e:
        current_app.logger.error('An error occurred: %s', e, exc_info=True)
        return jsonify({'error': str(e)}), 500