import pandas as pd
import logging

logger = logging.getLogger(__name__)

def clean_data(df: pd.DataFrame, drop_cols: list[str]) -> pd.DataFrame:
    logger.info("Cleaning data")
    return df.drop(columns=drop_cols).dropna()
