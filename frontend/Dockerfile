# Get official Node.js image
FROM node:16-alpine

# Set the working directory
WORKDIR /app

# Copy packages to container
COPY package*.json ./

# Install node dependencies
RUN npm install

# Copy the code and the rest of the application
COPY . .

# Build the application
RUN npm run build

# Expose the port the app runs on
EXPOSE 8080

# Run the application
CMD ["npm", "run", "serve"]

