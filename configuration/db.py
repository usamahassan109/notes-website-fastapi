# from pymongo import MongoClient
# import certifi

# ca = certifi.where()

# MONGO_URI = "mongodb+srv://usamahassan311_db_user:sORJeo98Eu4buhXX@cluster0.jhhjdft.mongodb.net/?retryWrites=true&w=majority"

# client = MongoClient(MONGO_URI, tls=True, tlsCAFile=ca)
# db = client['notes']

# print("✅ Connected to MongoDB!")
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://usamahassan311_db_user:sORJeo98Eu4buhXX@cluster0.jhhjdft.mongodb.net/?retryWrites=true&w=majority"

try:
    client = MongoClient(
        MONGO_URI,
        tls=True, 
        tlsAllowInvalidCertificates=True, 
        connectTimeoutMS=30000
    )
    db = client["notes"]
    collection = db["notes"]
    print("✅ MongoDB Connected (SSL disabled)")
except Exception as e:
    print("❌ MongoDB Connection Error:", e)
