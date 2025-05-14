def create_user(username, password, email, role, fullname, resume_path):
    return {
        "username": username,
        "password": password,
        "email": email,
        "role": role,
        "fullname": fullname,
        "resume": resume_path
    }

