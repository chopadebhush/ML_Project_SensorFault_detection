import os
import sys
from src.logger import logging
from src.exception import CustomException
import numpy as np
import pandas as pd
from pymongo import MongoClient
from zipfile import Path
from src.constant import *
from src.utils.main_utils import MainUtils
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    artifact_folder: str = os.path.join(artifact_folder)


class DataIngestion:
    def __init__(self) -> None:
        self.data_ingestion_config = DataIngestionConfig()
        self.utils = MainUtils()

    def export_collection_as_dataframe(self, collection_name, db_name):
        try:

            mongo_client = MongoClient(MONGO_DB_URL)
            collection = mongo_client[db_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns:
                df = df.drop(columns=['_id'], axis=1)

            df.replace({"na": np.nan}, inplace=True)

            return df

        except Exception as e:
            raise CustomException(e, sys) from e

    def export_data_into_feature_store_file_path(self) -> pd.DataFrame:

        try:
            logging.info("Exporting data from mongo db")
            raw_file_path = self.data_ingestion_config.artifact_folder

            os.makedirs(raw_file_path, exist_ok=True)

            sensor_data = self.export_collection_as_dataframe(
                collection_name=MONGO_COLLECTION_NAME, db_name=MONGO_DATABASE_NAME)

            logging.info(
                f"Saving exported data into feature store file path:{raw_file_path}")

            feature_store_file_path = os.path.join(
                raw_file_path, "wafer_fault.csv")
            sensor_data.to_csv(feature_store_file_path, index=False)

            return feature_store_file_path

        except Exception as e:
            raise CustomException(e, sys) from e

    def initiate_data_ingestion(self) -> Path:
        logging.info(
            "Enter into data ingestion method of data integration class")

        try:
            feature_store_file_path = self.export_data_into_feature_store_file_path()

            logging.info("got the data from mongodb")

            logging.info(
                "Exited initiated data ingestion methods of data ingestion class")

            return feature_store_file_path

        except Exception as e:
            raise CustomException(e, sys) from e
