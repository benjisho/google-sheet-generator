# backend/app/routes.py
from flask import Blueprint, jsonify, current_app
from googleapiclient.discovery import build
from google.oauth2 import service_account

main = Blueprint('main', __name__)

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
        result = drive_service.files().copy(
            fileId=template_file_id,
            body=copied_file
        ).execute()
        return jsonify({'spreadsheetId': result.get('id')}), 200
    except Exception as e:
        current_app.logger.error('An error occurred: %s', e, exc_info=True)
        return jsonify({'error': str(e)}), 500
