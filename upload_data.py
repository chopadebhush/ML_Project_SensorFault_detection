from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# mongodb uri
uri = "mongodb+srv://chopadebhush:12345@cluster0.hrjlw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# create client connect to server
client = MongoClient(uri)

# create database and collection Name
DATABASE_NAME = "pwskills"
COLLECTION_NAME = "waferfault"

# upload the data using pandas
df = pd.read_csv(
    "D:\PW SKILL\PW_ML_Project\Sensor_Fault_detection\notebooks\wafer_23012020_041211.csv")
df.head()

df.drop("Unnamed: 0", axis=1, inplace=True)

# Convert dataframe into json
json_record = list(json.loads(df.T.to_json()).values())

# Insert records into DB and collections
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
