import os
from src.DataScienceProject import logger
from ensure import ensure_annotations
import yaml
import json
from box import ConfigBox
from typing import Any
from pathlib import Path
import joblib
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
        logger.info(f"YAML file: {path_to_yaml} carregado com sucesso")
        return ConfigBox(content)
    except BoxValueError as e:
        raise e ("yaml file esta vazio")
    except Exception as e:
        logger.error(f"Erro ao carregar o arquivo YAML: {e}")
        raise e

@ensure_annotations
def create_directories(path_directories: list, verbose =True):
    for path in path_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Diretório criado em: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON salvo em: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path, 'r') as f:
        content = json.load(f)
    logger.info(f"JSON carregado de: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_binary(file_path: Path, data: Any):
    joblib.dump(value= data, filename=file_path)
    logger.info(f"Objeto salvo em formato binário em: {file_path}")

@ensure_annotations
def load_binary(file_path: Path) -> Any:
    data = joblib.load(file_path)
    logger.info(f"Objeto carregado de formato binário em: {file_path}")
    return data