import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import show_error,save_object
from logger import logging
from dataclasses import dataclass
import pandas as pd,numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report


@dataclass
class ModelTrainingConfig:
    model_file_path = os.path.join("artifacts","model.pkl")
    models = {
        "LogisticRegression":LogisticRegression(),
        "DecisionTreeClassifier":DecisionTreeClassifier(),
        "RandomForestClassifier":RandomForestClassifier(),
        "SVC":SVC()
    }

class ModelTraining:
    def __init__(self):
        self.dataConfig = ModelTrainingConfig()
    
    def initiate_model_training(self,train_arr,test_arr):
        try:
            logging.info("Train test spliting start")
            x_train = train_arr[:,:-1]
            y_train = train_arr[:,-1]

            x_test = test_arr[:,:-1]
            y_test = test_arr[:,-1]
            logging.info("Train test spliting completed")

        
            report={}
            models = self.dataConfig.models
            logging.info("Models training started")

            for modelname in models.keys():
                model = models[modelname]
                model.fit(x_train,y_train)
                y_test_pred = model.predict(x_test)
                test_accuracy_score = accuracy_score(y_test,y_test_pred)
                report[modelname] = test_accuracy_score
            logging.info("Models training completed")

            best_score = max(list(report.values()))
            best_model_name = list(report.keys())[list(report.values()).index(best_score)]
            logging.info("Best model found")

            print(best_model_name)
            print(best_score)
            logging.info("Best model training started")

            final_model = models[best_model_name].fit(x_train,y_train)            
            final_y_test_pred = final_model.predict(x_test)
            final_accuracy_score = accuracy_score(y_test,final_y_test_pred)
            logging.info("Best model training completed")

            print(final_accuracy_score)
            logging.info("Best model pickle file save started")

            save_object(self.dataConfig.model_file_path,final_model)
            logging.info("Best model pickle file save completed")

        except Exception as e:
            show_error(e,sys)
        
        

        

    