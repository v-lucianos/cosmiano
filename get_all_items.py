from pymongo import MongoClient

# Get the connection string from your environment variables
connection_string = ""
# Create a MongoClient object
client = MongoClient(connection_string)

# Connect to your database
db = client['SampleDB']

# Connect to your collection
collection = db['SampleCollection']

# Fetch all documents from your collection
documents = collection.find()

# Print all documents
for document in documents:
    print(document)