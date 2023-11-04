# Use an official Node runtime as a base image
FROM node:16-alpine

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in package.json
RUN npm install

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run npm start command to start the app
CMD ["npm", "start"]
