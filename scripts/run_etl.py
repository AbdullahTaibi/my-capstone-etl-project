import os
import sys
from config.env_config import setup_env
from src.utils.logging_utils import setup_logger
from src.extract.extract import extract_global_flights
from src.transform.transform import clean_data
from src.load.load import load_global_flight_db

# Get the argument from the run_etl command to set up  env



log_base_path = os.getenv("LOG_BASE_PATH")
logger = setup_logger(
    "etl_pipeline", "etl_pipeline.log", base_path=log_base_path)

def main():
    
    
    
    try:
        # Get the argument from the run_etl command and set up the environment
        setup_env(sys.argv)
        env = os.getenv("ENV", "unknown")
        logger.info(f"Starting ETL pipeline in {env} environment")
        logger.info("Beginning data extraction phase")
        extracted_data = extract_global_flights()
        logger.info("Data extraction phase completed")
        
        logger.info("Beginning transformation phase")
        transformed_data = clean_data(extracted_data)
        logger.info("Data extraction phase completed")
        
        logger.info("Beginning transformation phase")
        transformed_data = clean_data(extracted_data)
        logger.info("Data extraction phase completed")

        logger.info("Beginning loading phase")
        load_global_flight_db(transformed_data)
        logger.info("Loading phase completed")

        return transformed_data
    except Exception as e:
        logger.error(f"ETL pipeline failed: {str(e)}")
    sys.exit(1)


if __name__ == "__main__":
    main()
