# Use Node.js 16 as the base image
FROM node:16  

# Set the working directory
WORKDIR /app  

# Copy package.json and yarn.lock
COPY package.json yarn.lock ./  

# Install dependencies using Yarn
RUN yarn install  

# Copy the rest of the application files
COPY . .  

# Build the application
RUN yarn build  

# Expose port 3000
EXPOSE 3000  

# Start the application
CMD ["yarn", "start"]
