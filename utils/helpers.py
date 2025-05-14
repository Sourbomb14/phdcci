import hashlib
import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(password, hashed):
    return hash_password(password) == hashed

def send_email(to_email, subject, content):
    sender = os.getenv("GMAIL_USER")
    password = os.getenv("GMAIL_PASS")
    yag = yagmail.SMTP(sender, password)
    yag.send(to=to_email, subject=subject, contents=content)
