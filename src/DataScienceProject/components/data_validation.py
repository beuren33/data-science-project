import pandas as pd
from src.DataScienceProject import logger
from src.DataScienceProject.entity.entity_config import DataValidationConfig 

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        logger.info(f"Data Validation config: {self.config}")
    def validate_cols_name(self) -> bool:
        try:
            logger.info("Start data validation")
            validation_status = True

            df = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(df.columns)

            all_schema_cols = self.config.all_schema.keys()
            for col in all_cols:
                if col not in all_schema_cols:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f"Validation Name Status: {validation_status}\n")
                    logger.info(f"Column {col} esta faltando")
                    break
                
                    
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"Validation Name Status: {validation_status}\n")

            validation_col_name_status = validation_status
            return validation_col_name_status
        
        except Exception as e:
            logger.error(f"Erro no data validation: {e}")
            raise e
    
    def validate_type_cols(self) -> bool:
        try:
            status = True
            df = pd.read_csv(self.config.unzip_data_dir)
            all_schema_cols = self.config.all_schema.keys()
            
            for col in all_schema_cols:
                if col not in df.columns:
                    logger.warning(f"Column  not found in dataframe")
                    return False
                expected_type = self.config.all_schema[col]
                actual_type = df[col].dtype
                if expected_type != actual_type:
                    status = False
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f"Validation type Status : {status} \n")
                    logger.info(f"Column {col} has wrong type. Expected: {expected_type}, Actual: {actual_type}")
                    break
            
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"Validation type Status: {status} \n")
             
            logger.info("Type validation passed")
            status_type_validation = status
            return status_type_validation
        except Exception as e:
            logger.error(f"Erro no type validation: {e}")
            raise e