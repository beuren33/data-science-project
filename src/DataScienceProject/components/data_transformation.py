import os
from sklearn.model_selection import train_test_split
from src.DataScienceProject import logger
import pandas as pd
from src.DataScienceProject.entity.entity_config import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):
        try:
            df = pd.read_csv(self.config.data_path)
            logger.info(f"Read {self.config.data_path}")
            train, test = train_test_split(df, test_size=0.3, random_state=42)

            train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
            test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

            logger.info("Train test split Completo.")
            logger.info(f"Csv de teste e treino salvo em: {self.config.root_dir}")
            logger.info(f"Train shape: {train.shape}, Test shape: {test.shape}")
        except Exception as e:
            logger.error(f"Erro no train_test_spliting: {e}")
            raise e