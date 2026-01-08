"""
Data Pipeline Package

This package provides extract, transform, and load functionality
for handling and processing data efficiently.
"""

from .extract import extract_data
from .transform import transform_data
from .load import load_data
from .config import PIPELINE_CONFIG

__all__ = ['extract_data', 'transform_data', 'load_data', 'PIPELINE_CONFIG']
__version__ = "0.1.0"
