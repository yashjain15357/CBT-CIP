# modules/storage.py
import pandas as pd
from sqlalchemy import create_engine
from config.settings import DATABASE_URI
from modules.utils import logger

class Storage:
    def __init__(self):
        self.engine = create_engine(DATABASE_URI)

    def save_to_csv(self, data, file_path):
        try:
            df = pd.DataFrame([data])
            df.to_csv(file_path, mode='a', header=False, index=False)
            logger.info(f'Successfully saved data to {file_path}')
        except Exception as e:
            logger.error(f'Error saving data to CSV: {e}')

    def save_to_db(self, data, table_name):
        try:
            df = pd.DataFrame([data])
            df.to_sql(table_name, self.engine, if_exists='append', index=False)
            logger.info(f'Successfully saved data to database table {table_name}')
        except Exception as e:
            logger.error(f'Error saving data to database: {e}')

