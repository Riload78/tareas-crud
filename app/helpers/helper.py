from werkzeug.security import generate_password_hash

def create_password(password):
    if password:
        return generate_password_hash(password)