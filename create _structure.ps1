# Define the root directory
$rootDir = "google-sheet-generator"

# Define the backend and frontend directories
$backendDir = Join-Path $rootDir "backend"
$frontendDir = Join-Path $rootDir "frontend"

# Create the root, backend, and frontend directories
New-Item -ItemType Directory -Path $rootDir
New-Item -ItemType Directory -Path $backendDir
New-Item -ItemType Directory -Path $frontendDir

# Create the backend subdirectories and files
New-Item -ItemType Directory -Path (Join-Path $backendDir "app")
New-Item -ItemType Directory -Path (Join-Path $backendDir "app\templates")
New-Item -ItemType Directory -Path (Join-Path $backendDir "tests")
New-Item -ItemType File -Path (Join-Path $backendDir "app\__init__.py")
New-Item -ItemType File -Path (Join-Path $backendDir "app\routes.py")
New-Item -ItemType File -Path (Join-Path $backendDir "app\models.py")
New-Item -ItemType File -Path (Join-Path $backendDir "config.py")
New-Item -ItemType File -Path (Join-Path $backendDir "requirements.txt")
New-Item -ItemType File -Path (Join-Path $backendDir "Dockerfile")
New-Item -ItemType File -Path (Join-Path $backendDir "manage.py")

# Create the frontend subdirectories and files
New-Item -ItemType Directory -Path (Join-Path $frontendDir "public")
New-Item -ItemType Directory -Path (Join-Path $frontendDir "src")
New-Item -ItemType Directory -Path (Join-Path $frontendDir "src\components")
New-Item -ItemType File -Path (Join-Path $frontendDir "src\App.js")
New-Item -ItemType File -Path (Join-Path $frontendDir "src\index.js")
New-Item -ItemType File -Path (Join-Path $frontendDir "package.json")
New-Item -ItemType File -Path (Join-Path $frontendDir "Dockerfile")
New-Item -ItemType File -Path (Join-Path $frontendDir ".env")

# Create the root level files
New-Item -ItemType File -Path (Join-Path $rootDir "docker-compose.yml")
New-Item -ItemType File -Path (Join-Path $rootDir "README.md")
New-Item -ItemType File -Path (Join-Path $rootDir ".gitignore")
