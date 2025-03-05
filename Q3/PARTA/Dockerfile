# Use an official Node.js image
FROM node:latest  

# Set the working directory
WORKDIR /app  

# Copy package.json and install dependencies
COPY package.json .  
RUN npm install  

# Copy the rest of the application files
COPY . .  

# Expose the required port
EXPOSE 3000  

# Run the application
CMD ["node", "index.js"]
