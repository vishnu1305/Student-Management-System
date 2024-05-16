
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://sxcmt:sxcmt@sxcmt.uvrp8pj.mongodb.net/?retryWrites=true&w=majority&appName=SXCMT"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


# Sample MongoDB data
# Database Name: userdb
# Collection Name: users


# Create or access the database
db = client["userdb"]

# Create or access the collection
collection = db["update"]

# Insert sample data
sample_data = [
    {"username": "abc", "password": "abc"}
    # {"username": "sushilbilung", "password": "viceprincipal"}
]

collection.insert_many(sample_data)


# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)