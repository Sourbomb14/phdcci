users_db = []

def insert_user(username, password_hash, role):
    user = {"username": username, "password": password_hash, "role": role}
    users_db.append(user)

def get_user(username, role):
    for user in users_db:
        if user["username"] == username and user["role"] == role:
            return user
    return None
