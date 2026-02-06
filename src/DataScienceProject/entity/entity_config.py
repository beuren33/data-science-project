from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: str
    all_schema: dict

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass
class ModelTrainerConfig:
    model_name: str
    train_data: Path
    test_data: Path
    root_dir: Path
    alpha: float
    l1_ratio: float
    target_column: str

@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    model: Path
    test_file_path: Path
    metric_file_path: Path
    all_params: dict
    target_col: str
    mlflow_uri: str
