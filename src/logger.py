import sys
import os
from datetime import datetime
import logging

from utils import show_error
from exception import CustomException


File_path = f"{datetime.now().strftime('%d_%m_%Y_%H_%M')}.log"
os.makedirs(os.path.join(os.getcwd(),'logfiles'),exist_ok=True)

Log_file_path = os.path.join(os.getcwd(),'logfiles',File_path)

logging.basicConfig(
    filename=Log_file_path,
    format="[%(asctime)s]  %(lineno)d  %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__=="__main__":
    try:
        if(True):
            raise CustomException("error kheyechi")
    
    except Exception as e:
        show_error(e, sys)
