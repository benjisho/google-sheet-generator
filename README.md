# Google Sheet Generator

This project provides a web application to generate work attendance sheets as Google Sheets for each user in their own Google Drive. The application is split into a frontend and backend, each running in its own Docker container.

## Table of Contents

1. [Technologies Used](#technologies-used)
2. [File Structure](#file-structure)
3. [Setup Instructions](#setup-instructions)
4. [Usage Instructions](#usage-instructions)
5. [Contributing](#contributing)
6. [License](#license)

## Technologies Used

- Backend: Flask
- Frontend: React
- Containerization: Docker
- Google Sheets API
- Google OAuth 2.0

## File Structure

```bash
google-sheet-generator/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── cleanup_sheets_from_api.py
│   │   ├── credentials.json
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── templates/
│   ├── tests/
│   ├── config.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── manage.py
│   └── credentials.json
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── Button.css
│   │   │   └── Button.js
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   ├── Dockerfile
│   └── .env
├── docker-compose.yml
├── README.md
└── .gitignore
```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/benjisho/google-sheet-generator.git
cd google-sheet-generator
```

2. Build and run the Docker containers:
```bash
docker-compose up --build
```

## Usage Instructions

1. Add your [GCP service-account](https://console.cloud.google.com/iam-admin/serviceaccounts) credentials into this file: `credentials.json`
2.  Open a web browser and navigate to http://localhost:3000 to access the application.
3. Follow the on-screen instructions to authenticate with Google and generate a work attendance sheet.

## To Test Backend Endpoint Manually

If possible, test the `/generate-sheet`` route manually using a tool like curl or Postman to see if you can reproduce the error and get more information about what might be causing it.
```bash
curl -X POST http://localhost:5000/generate-sheet
```

## Delete the environment we deployed

```bash
docker system prune -a
```
## Contributing
Contributions are welcome! Please read the contributing guidelines before getting started.

## License
GNU License