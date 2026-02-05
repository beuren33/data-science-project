from src.DataScienceProject import logger
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.DataScienceProject.components.data_transformation import DataTransformation
from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.entity.entity_config import DataTransformationConfig

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainPipeline:
    def __init__(self):
        pass
    
    def init_data_transformation(self):
        try:
            with open("artifacts/data_validation/status.txt", "r") as f:
                lines = f.readlines()

                name_status = lines[0].strip().split(":")[-1].strip()
                type_status = lines[1].strip().split(":")[-1].strip()
            
            if name_status == 'True' and type_status == 'True':
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("O shema nao é valido")
        except Exception as e:
            logger.error(f"Erro na validação do schema: {e}")
            raise e

    