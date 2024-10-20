import pandas as pd
import numpy as np
import sys, os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from dataclasses import dataclass

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exception import CustomException
from logger import logging
from utils import show_error, save_object

@dataclass 
class DataTransformationConfig:
    preproccesor_file_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.dataConfig = DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            logging.info("Data transformation pipeline creation started")

            preprocessor = Pipeline(steps=[
                ('tfidf', TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)),
                ('scaler', StandardScaler(with_mean=False)) 
            ])

            logging.info("Data transformation pipeline created")
            return preprocessor

        except Exception as e:
            show_error(e, sys)

    def initialize_data_transformation(self, train_path, test_path):
        try:
            logging.info("Train-test data reading started")

            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)
            logging.info(f"Train data shape: {train_data.shape}, Test data shape: {test_data.shape}")

            preprocessor = self.get_data_transformation_object()
            input_feature_train = train_data['Message']
            output_feature_train = train_data['Category']

            input_feature_test = test_data['Message']
            output_feature_test = test_data['Category']

            logging.info("Train-test data transformation started")

            scaled_data_train = preprocessor.fit_transform(np.array(input_feature_train))
            scaled_data_test = preprocessor.transform(np.array(input_feature_test))
            logging.info("Train-test data transformed")

            output_feature_train = output_feature_train.astype('int').values.reshape(-1, 1)
            output_feature_test = output_feature_test.astype('int').values.reshape(-1, 1)

            train_arr = np.hstack((scaled_data_train.toarray(), output_feature_train))
            test_arr = np.hstack((scaled_data_test.toarray(), output_feature_test))

            save_object(self.dataConfig.preproccesor_file_path, preprocessor)
            logging.info("Preprocessor pipeline pickle file saved")

            return (train_arr, test_arr)

        except Exception as e:
            show_error(e, sys)
