# Google Sheet Generator

This project provides a web application to generate work attendance sheets as Google Sheets for each user in their own Google Drive. The application is split into a frontend and backend, each running in its own Docker container.

## Table of Contents
1. [Technologies Used](#technologies-used)
2. [File Structure](#file-structure)
3. [Setup Instructions](#setup-instructions)
    
    3.1. [Clone the repository](#clone-the-repository)
4. [Nginx and SSL Configuration](#nginx-and-ssl-configuration)
    
    4.1. [Generate SSL certificate](#generate-ssl-certiificate-into-`nginx/certs/`-directory)
    
    4.2. [Add GCP Credentials](#add-gcp-credentials)
    
    4.3. [Build and Run Docker Containers](#build-and-run-docker-containers)
5. [Usage Instructions](#usage-instructions)
6. [To Test Backend Endpoint Manually](#to-test-backend-endpoint-manually)
7. [Delete the Environment](#delete-the-environment-we-deployed)
    
    7.1. [Delete Docker Environment](#delete-the-docker-environment)
    
    7.2. [Delete Generated Sheets](#delete-the-generated-sheets-by-the-clients)
8. [Contributing](#contributing)
9. [License](#license)


## Technologies Used
- Backend: Flask
- Frontend: React
- Containerization: Docker
- Reverse Proxy: Nginx
- SSL/TLS: OpenSSL
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
│   └── manage.py
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
├── nginx/
│   ├── nginx.conf
│   ├── certs/
│   │   ├── server.crt
│   │   └── server.key
│   └── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore
```

## Setup Instructions

### Clone the repository:
```bash
git clone https://github.com/benjisho/google-sheet-generator.git
cd google-sheet-generator
```

### Nginx and SSL Configuration
#### Generate SSL certiificate into `nginx/certs/` directory
1. Run the following command to generate a 2048-bit RSA private key, which is used to decrypt traffic:
```
openssl genrsa -out nginx/certs/server.key 2048
```
2. Run the following command to generate a certificate, using the private key from the previous step.
```
openssl req -new -key nginx/certs/server.key -out nginx/certs/server.csr
```

3. Run the following command to self-sign the certificate with the private key, for a period of validity of 365 days:
```
openssl x509 -req -days 365 -in nginx/certs/server.csr -signkey nginx/certs/server.key -out nginx/certs/server.crt
```
#### Add GCP Credentials
4. Add your [GCP service-account](https://console.cloud.google.com/iam-admin/serviceaccounts) credentials into this file: `credentials.json`
```bash
vi backend/app/credentials.json
```
#### Build and Run Docker Containers
5. Build and run the Docker containers:
```bash
docker-compose up --build
```

## Usage Instructions
2. Open a web browser and navigate to `https://<your-domain-or-IP>` to access the application.

> Please replace `<your-domain-or-IP>` with your actual domain name or IP address where the application is hosted. Also, make sure to follow best practices and keep your SSL certificates secure.


## To Test Backend Endpoint Manually

If possible, test the `/generate-sheet`` route manually using a tool like curl or Postman to see if you can reproduce the error and get more information about what might be causing it.
```bash
curl -X POST http://localhost:5000/generate-sheet
```

## Delete the environment we deployed

### Delete the docker environment
```bash
docker system prune -a
```
### Delete the generated Sheets by the clients

1. Create and Activate a Virtual Environment (if not already done):
- Create a virtual environment:
```bash
python3 -m venv ~/venv
```
- Activate the virtual environment:
```bash
source ~/venv/bin/activate
```
2. Install Dependencies:
- Navigate to the `backend/`` directory where your requirements.txt file is located.
```bash
cd backend/
```
- Run the following command:
```bash
cd backend/
pip install -r requirements.txt
```
3. Run the Cleanup Script:
```bash
cd 
python3 app/cleanup_sheets_from_api.py
```
## Contributing
Contributions are welcome! Please read the contributing guidelines before getting started.

## License
GNU License