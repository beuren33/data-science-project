from src.DataScienceProject import logger
import os
import pandas as pd
from src.DataScienceProject.components.data_train import ModelTrainer
from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.entity.entity_config import ModelTrainerConfig

STAGE_NAME = 'Data Train Pipeline'

class DataTrainPipeline:
    def __init__(self):
        pass

    def init_data_train_pipeline(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train_model()