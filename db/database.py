from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient("mongodb+srv://PHDCCI_Internship_admin:k6lnh1oryhad9ovR@cluster0.ht97vch.mongodb.net/")
db = client["phdcci"]

users_col = db["users"]
jobs_col = db["job_posts"]
apps_col = db["applications"]

def insert_user(user):
    users_col.insert_one(user)

def get_user_by_username(username):
    return users_col.find_one({"username": username})

def insert_job(job):
    jobs_col.insert_one(job)

def get_all_jobs():
    return list(jobs_col.find())

def insert_application(app):
    apps_col.insert_one(app)

def get_applications_by_student(username):
    return list(apps_col.find({"student": username}))
