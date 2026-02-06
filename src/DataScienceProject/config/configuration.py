import os
from src.DataScienceProject.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.DataScienceProject.utils.common import read_yaml, create_directories
from src.DataScienceProject.entity.entity_config import (DataIngestionConfig, DataTransformationConfig, DataValidationConfig, ModelEvaluationConfig,ModelTrainerConfig)

class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath= PARAMS_FILE_PATH, schema_filepath= SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_dir=config.unzip_data_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema,
        )
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation= DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path)
        return data_transformation
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            model_name = config.model_name,
            train_data = config.train_data,
            test_data = config.test_data,
            root_dir = config.root_dir,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema
        )


        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params= self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])    

        model_evaluation_config = ModelEvaluationConfig(
            root_dir = config.root_dir,
            model = config.model,
            test_file_path = config.test_file_path,
            metric_file_path = config.metric_file_path,
            all_params = self.params,
            target_col = self.schema.TARGET_COLUMN,
            mlflow_uri = 'https://dagshub.com/matheusbeuren/data-science-project.mlflow'


        )

        return model_evaluation_config