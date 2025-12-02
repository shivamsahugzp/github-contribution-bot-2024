# Helper utility functions
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

def process_data(data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    # Process and validate input data
    if not data:
        logger.warning("Empty data provided")
        return None
    
    try:
        # Process logic here
        result = {k: v for k, v in data.items() if v is not None}
        return result
    except Exception as e:
        logger.error(f"Error processing data: {e}")
        return None

if __name__ == "__main__":
    test_data = {"key1": "value1", "key2": None}
    result = process_data(test_data)
    print(result)
