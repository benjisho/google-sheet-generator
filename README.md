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
│   │   ├── routes.py
│   │   ├── models.py
│   │   └── templates/
│   ├── tests/
│   ├── config.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── manage.py
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
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

1. Open a web browser and navigate to http://localhost:3000 to access the application.
2. Follow the on-screen instructions to authenticate with Google and generate a work attendance sheet.

## Contributing
Contributions are welcome! Please read the contributing guidelines before getting started.

## License
GNU License