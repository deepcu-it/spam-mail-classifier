import pandas as pd
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_object,show_error

class CustomData:
    try:
        def __init__(self,message):
            self.message = message
    
        def get_data_as_list(self):
            return  [self.message]
    except Exception as e:
        show_error(e,sys)
    
class Pipeline:
    def predict_spam_or_not(self,message_list)->int:
        try:
            preprocessor = load_object(os.path.join('artifacts','preprocessor.pkl'))
            model = load_object(os.path.join('artifacts','model.pkl'))
            scaled_input = preprocessor.transform(message_list)
            return model.predict(scaled_input)
        except Exception as e:
            show_error(e,sys)

