'''
log all info of any execution that happens in some file
'''

import logging
import os
from datetime import datetime


LOG_FILE =f"{datetime.now().strftime('%y_%m_%d_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)#cwd:correct working directory
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH= os.path.join(logs_path, LOG_FILE)


'''
generic log format for every print in the loh files
'''
logging.basicConfig(
    filename= LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

#for testing
# if __name__=="__main__":
#     logging.info('Logging has started')