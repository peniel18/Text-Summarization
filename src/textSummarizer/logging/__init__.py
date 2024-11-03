import os 
import sys 
import logging 
from datetime import datetime


log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
logs_dir =  os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)
log_filepath = os.path.join(logs_dir, log_file)
#os.makedirs(log_filepath, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str, 
    handlers=[
        logging.FileHandler(log_filepath), 
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")