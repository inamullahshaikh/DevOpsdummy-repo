# login_feature.py
def feature_login():
    print("Feature-Login: Improved Login System")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == "admin" and password == "password123":
        print("Login successful!")
    else:
        print("Invalid credentials.")

if __name__ == "__main__":
    feature_login()
