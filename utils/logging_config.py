import os
import logging
from pathlib import Path
from datetime import datetime

def setup_logging(script_name: str, logs_subdir: str = None):
    """
    Set up logging with timestamped files in a centralized logs directory
    
    Args:
        script_name: Name of the script (e.g., 'agent_demo', 'test_endpoint')
        logs_subdir: Optional subdirectory within logs (e.g., 'tests', 'examples')
    """
    # Find project root (go up until we find main project files)
    current_dir = Path(__file__).parent
    project_root = current_dir.parent
    
    # Create logs directory structure
    logs_dir = project_root / "logs"
    if logs_subdir:
        logs_dir = logs_dir / logs_subdir
    logs_dir.mkdir(parents=True, exist_ok=True)
    
    # Create timestamped log file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = logs_dir / f"{script_name}_{timestamp}.log"
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ],
        force=True
    )
    
    return log_file

def get_logger(name: str):
    """Get a logger instance"""
    return logging.getLogger(name)