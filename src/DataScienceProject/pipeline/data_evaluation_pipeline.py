from src.DataScienceProject import logger
import os
import pandas as pd
from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.data_evaluate import ModelEvaluation

STAGE_NAME = 'Data Evaluation Pipeline'

class DataEvaluationPipeline:
    def __init__(self):
        pass

    def init_data_evaluation_pipeline(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()