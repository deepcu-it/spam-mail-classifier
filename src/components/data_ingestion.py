import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import show_error
from logger import logging
from dataclasses import dataclass
import pandas as pd,numpy as np
from sklearn.model_selection import train_test_split
from data_transformatin import DataTransformation
from model_training import ModelTraining

@dataclass
class DataIngestionConfig:
    raw_data_path = os.path.join("artifacts",'data.csv')
    train_data_path = os.path.join("artifacts",'train.csv')
    test_data_path = os.path.join("artifacts",'test.csv')

class DataIngestion:
    def __init__(self):
        self.dataConfig = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv("notebook/mail_spam_classifier.csv")
            logging.info("data read from file")
            df['Category'] = np.where(df['Category']=='spam',0,1)
            logging.info("spams are marked as 0 and ham as 1")
            currWorkingDir = os.getcwd()
            os.makedirs("artifacts",exist_ok=True)
            
            logging.info("Artifact folder creeated")
            df.to_csv(os.path.join(currWorkingDir,self.dataConfig.raw_data_path),index=False,header=True)
            train_set,test_set = train_test_split(df,random_state=42,test_size=0.2)
            train_set.to_csv(os.path.join(currWorkingDir,self.dataConfig.train_data_path),index=False,header=True)
            test_set.to_csv(os.path.join(currWorkingDir,self.dataConfig.test_data_path),index=False,header=True)
            logging.info("train test data saved on the artifacts")
            return (
                self.dataConfig.train_data_path,
                self.dataConfig.test_data_path
            )

        except Exception as e:
            show_error(e,sys)

            
if __name__=="__main__":
    di = DataIngestion()
    train_path,test_path = di.initiate_data_ingestion()

    dt = DataTransformation()
    train_arr,test_arr = dt.initialize_data_transformation(train_path,test_path)
    
    mt = ModelTraining()
    mt.initiate_model_training(train_arr,test_arr)

