import sys,os
import dill 
def show_error(e,error:sys):
    _,_,exc_traceback=error.exc_info()
    print(f"file-name:{exc_traceback.tb_frame.f_code.co_filename}, has error:{str(e.__str__())}, in line-no:{exc_traceback.tb_lineno}")
    
def save_object(file_path,obj):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'wb') as file:
            dill.dump(obj,file)
    except Exception as e:
        show_error(e,sys)

def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        show_error(e,sys)