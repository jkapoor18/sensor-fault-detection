import pymongo
import pandas as pd
import json



from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://Jkapoor04:Jkapoor18@cluster0.fg5f9he.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

DATA_FILE_PATH = (r"D:\sensor-fault-detection-main\sensus_fault.csv")
DATABASE_NAME = "SCANIA"
COLLECTION_NAME = "SCANIA_PROJECT"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    df = df.iloc[:34000, :]
    print(f"Rows and columns: {df.shape}")

    # Convert dataframe to json so that we can dump these records into MongoDB
    df.reset_index(drop=True, inplace=True)

    json_record = json.loads(df.to_json(orient="records"))

    # Insert converted json record to MongoDB
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    collection.insert_many(json_record)

    print("Data inserted successfully.")
