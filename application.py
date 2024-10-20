from flask import Flask,request,render_template
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.pipeline.predict_pipeline import CustomData,Pipeline
from src.utils import show_error
application = Flask(__name__)

app = application

@app.route("/",methods =['GET','POST'])
def show_form():
    if request.method=='GET':
        return render_template('home.html')
    else:
        try:
            message = request.form['message']
            data = CustomData(message)
            list_message = data.get_data_as_list()
            predict_pipeline = Pipeline()
            result = predict_pipeline.predict_spam_or_not(list_message)
            
            output = 'Spam' if result[0]==0 else 'not Spam'
            return render_template('home.html',result=output)
        except Exception as e:
            show_error(e,sys)
        

if __name__=="__main__":
    app.run(host="0.0.0.0")