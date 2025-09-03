#Import libraries

import os
import logging
import pandas as pd
import timeit
from src.utils.logging_utils import setup_logger, log_extract_success
# Define the file path for the customers CSV file
FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "data",
    "raw",
    "global_flights_data.csv",
)
# Configure the logger
logger = setup_logger(__name__, "extract_data.log", level=logging.DEBUG)
EXPECTED_PERFORMANCE = 0.0001
TYPE = "GLOBAL_FLIGHTS from CSV"

def extract_global_flights() -> pd.DataFrame:
    start_time = timeit.default_timer()
    try:
        global_flights_df = pd.read_csv(FILE_PATH)
        extract_global_flights_execution_time = timeit.default_timer() - start_time
        log_extract_success(
            logger,
            TYPE,
            global_flights_df.shape,
            extract_global_flights_execution_time,
            EXPECTED_PERFORMANCE,
        )

        return global_flights_df
    except Exception as e:
        logger.setLevel(logging.ERROR)
        logger.error(f"Error loading {FILE_PATH}: {e}")
        raise Exception(f"Failed to load CSV file: {FILE_PATH}")