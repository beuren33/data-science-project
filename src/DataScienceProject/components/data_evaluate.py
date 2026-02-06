import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.DataScienceProject.utils.common import save_json, read_yaml, create_directories
from src.DataScienceProject.constants import *
from pathlib import Path
from src.DataScienceProject.entity.entity_config import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def evaluate_metrics(self, actual, predicted):
        rmse = np.sqrt(mean_squared_error(actual, predicted))
        mae = mean_absolute_error(actual, predicted)
        r2 = r2_score(actual, predicted)
        return rmse, mae, r2
    
    def evaluate(self):
        test_data = pd.read_csv(self.config.test_file_path)
        model = joblib.load(self.config.model)

        test_x = test_data.drop(self.config.target_col, axis=1)
        test_y = test_data[self.config.target_col]

        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        mlflow.set_experiment("model_evaluation")


        with mlflow.start_run():
            predicted = model.predict(test_x)
            (rmse, mae, r2) = self.evaluate_metrics(test_y, predicted)

            score = {
                "rmse": rmse,
                "mae": mae,
                "r2": r2
            }
            save_json(path=Path(self.config.metric_file_path), data=score)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(score)
            

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")