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
