import pandas as pd
import sqlalchemy
import logging

# Set up logger
logger = logging.getLogger(__name__)

def load_data(df: pd.DataFrame, connection_uri: str, table_name: str, if_exists: str = "replace"):
    """
    Load a cleaned DataFrame into a SQL database.

    Parameters:
    - df: pandas DataFrame to be loaded
    - connection_uri: SQLAlchemy-style database URI
    - table_name: Name of the target table in the database
    - if_exists: What to do if the table already exists ('fail', 'replace', 'append')
    """
    try:
        logger.info(f"Connecting to database at {connection_uri}")
        engine = sqlalchemy.create_engine(connection_uri)

        logger.info(f"Loading data into table '{table_name}' with if_exists='{if_exists}'")
        df.to_sql(name=table_name, con=engine, index=False, if_exists=if_exists)

        logger.info("Data successfully loaded into database.")
    except Exception as e:
        logger.error(f"Error loading data to database: {e}")
        raise
