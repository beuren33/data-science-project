from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.data_ingestion import DataIngestion
from src.DataScienceProject import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainPipeline:
    def __init__(self):
        pass

    def init_data_ingestion(self):
        config = ConfigurationManager()
        config_ingestion = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=config_ingestion)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainPipeline()
        obj.init_data_ingestion()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e