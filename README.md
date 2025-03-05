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
