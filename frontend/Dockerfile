# Use an official Node runtime as a base image
FROM node:16

# Set the working directory in the container to /app
WORKDIR /app

# Copy package.json and package-lock.json into the container at /app
COPY package*.json ./

# Install any needed packages specified in package.json
RUN npm install --verbose || cat npm-debug.log

# Explicitly install axios
RUN npm install axios --save

# List the contents of node_modules (optional, for debugging purposes)
RUN ls node_modules

# Copy the current directory contents into the container at /app
COPY . .

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run npm start command to start the app
CMD ["npm", "start"]
