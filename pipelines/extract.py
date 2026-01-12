import requests
import pandas as pd
import logging

# modules installed

logger = logging.getLogger(__name__)

def from_api(url: str, token: str) -> pd.DataFrame:
    logger.info("Fetching data from API")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return pd.DataFrame(response.json())
