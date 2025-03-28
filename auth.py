import hashlib

users_db = {}  # Simple user database for demonstration

# Register a new user
def register_user(username, password):
    if username in users_db:
        print("Username already taken.")
        return False
    users_db[username] = hashlib.sha256(password.encode()).hexdigest()
    print(f"User {username} registered successfully.")
    return True

# Authenticate a user
def authenticate_user(username, password):
    if username not in users_db:
        print("User not found.")
        return False
    if users_db[username] == hashlib.sha256(password.encode()).hexdigest():
        print(f"User {username} authenticated successfully.")
        return True
    print("Incorrect password.")
    return False
