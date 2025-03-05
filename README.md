# Question 1 
## **Part A: Updating `feature-login` with the Latest Changes from `main`**  
To ensure a smooth integration, follow these steps:

1. **Switch to `feature-login` branch:**  
   ```bash
   git checkout feature-login
   ```
2. **Fetch the latest changes from the remote repository:**  
   ```bash
   git fetch origin
   ```
3. **Merge `main` into `feature-login` (safe way to integrate changes):**  
   ```bash
   git merge origin/main
   ```
   If there are conflicts, resolve them manually, then commit the merge.
---

## **Part B: Reverting a Buggy Commit & Creating a Fix Branch**  

1. **Revert the last commit on `main`:**  
   ```bash
   git checkout main
   git revert HEAD
   git push origin main
   ```
   
2. **Create a new branch to fix the issue:**  
   ```bash
   git checkout -b bugfix/issue-123
   ```

3. **Push the new branch to the remote repository:**  
   ```bash
   git push origin bugfix/issue-123
   ```

# Question 2

Here are the Docker commands for each part:  

### **Part A: Pull and Run the Python Web App with Environment Variables**  
```bash
docker pull myteam/python-app  
docker run -e DEBUG=True -e PORT=5000 -p 5000:5000 myteam/python-app
```

### **Part B: Run a PostgreSQL Database in Docker**  
```bash
docker pull postgres  
docker run --name postgres -e POSTGRES_PASSWORD=1234 -p 5432:5432 -d postgres
```

### **Part C: Tag and Push a Docker Image to Docker Hub**  
```bash
docker tag myapp:v1 i220857/myapp:v1  
docker push i220857/myapp:v1
```
Here are the solutions for each part of the containerization process:  

---

# Question 3
## **Part A: Minimal Dockerfile for a Node.js Application**  
```dockerfile
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
```

---

## **Part B: Dockerfile for a Node.js Application Using Yarn**  
```dockerfile
# Use Node.js 16 as the base image
FROM node:16  

# Set the working directory inside the container
WORKDIR /app  

# Copy package.json and install dependencies using Yarn
COPY package.json yarn.lock ./  
RUN yarn install  

# Copy the rest of the application files
COPY . .  

# Build the application
RUN yarn build  

# Expose port 3000
EXPOSE 3000  

# Start the application
CMD ["yarn", "start"]  
```

---

## **Part C: Persisting Logs in Docker**  
To persist logs, you can mount a volume so that logs are stored outside the container:  

```bash
docker run -v /path/on/host:/app/logs myapp
```
Alternatively, modify the `Dockerfile` to ensure logs are written to a persistent directory:  

```dockerfile
VOLUME [ "/app/logs" ]
```
This ensures logs persist across container restarts.

---

## **Part D: Enforcing a Non-Root User in the Dockerfile**  
Modify the Dockerfile to create and use a non-root user:  

```dockerfile
# Use Python 3.9 as base
FROM python:3.9  

# Set the working directory
WORKDIR /app  

# Create a non-root user
RUN useradd -m myuser  

# Copy application files and set permissions
COPY . .  
RUN chown -R myuser:myuser /app  

# Switch to non-root user
USER myuser  

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt  

# Run the application
CMD ["python", "app.py"]  
```
This ensures the application runs as `myuser`, not root.
