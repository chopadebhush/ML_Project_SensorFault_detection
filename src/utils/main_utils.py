import sys
import os
from typing import Dict, Tuple
import pandas as pd
import pickle
import yaml
import boto3

from src.constant import *
from src.logger import logging
from src.exception import CustomException


class MainUtils:
    def __init__(self) -> None:
        pass

    def read_yaml_file(self, filename: str) -> dict:
        try:
            with open(filename, "rb") as yaml_file:
                return yaml.safe_load(yaml_file)

        except Exception as e:
            raise CustomException(e, sys)

    def read_schema_config_file(self) -> dict:
        try:
            schema_config = self.read_schema_config_file(
                os.path.join("config", "schema.ymal"))
            return schema_config

        except Exception as e:
            raise CustomException(e, sys) from e

    @staticmethod
    def save_object(self, file_path: str, obj: object) -> None:
        logging.info("Enter the save object method MainUtils class")

        try:
            with open(file_path, "wb") as file_obj:
                pickle.dump(obj, file_obj)

            logging.info("Exited the save_object method of MainUtils class")

        except Exception as e:
            raise CustomException(e, sys) from e

    @staticmethod
    def load_object(self, file_path: str) -> object:
        logging.info("Enter the load object method MainUtils class")

        try:
            with open(file_path, "rb") as file_obj:
                obj = pickle.load(file_obj)

            logging.info("Exited the load_object method of MainUtils class")
            return obj

        except Exception as e:
            raise CustomException(e, sys) from e

    @staticmethod
    def load_object(file_path):
        logging.info("Enter load object method in Main Utils")
        try:
            with open(file_path, "rb") as file_obj:
                return pickle.load(file_obj)

            logging.info("Exited from load object method MainUtils")

        except Exception as e:
            logging.info("Exception occured at load object function MainUtils")
            raise CustomException(e, sys) from e
