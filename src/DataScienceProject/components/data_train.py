from src.DataScienceProject import logger
from sklearn.linear_model import ElasticNet
import pandas as pd
import joblib
from src.DataScienceProject.entity.entity_config import ModelTrainerConfig
import os


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self):
        try:
            logger.info("Carregando dados de treinamento")
            train_data = pd.read_csv(self.config.train_data)

            logger.info("Dividindo dados de treinamento em X e y")
            x_train = train_data.drop(columns=[self.config.target_column], axis=1)
            x_test = train_data.drop(columns=[self.config.target_column], axis=1)
            y_train = train_data[self.config.target_column]
            y_test = train_data[self.config.target_column]

            logger.info("Treino modelo ElasticNet")
            model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
            model.fit(x_train, y_train)

            logger.info("Salvando modelo")
            model_path = os.path.join(self.config.root_dir, self.config.model_name)
            joblib.dump(model, model_path)

            logger.info("Modelo Salvo")
        except Exception as e:
            logger.exception(e)
            raise e