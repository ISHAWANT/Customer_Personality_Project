from flask import Flask 
from src.personality.logger import logging 
from src.personality.exception import CustomException 
import os,sys 

app = Flask(__name__) 

@app.route('/',methods=['GET','POST']) 

def index():
    try:
        a=2
        b=0
        c=a/b
        return c
        # raise Exception('We are testing our custom exception file') 
    except Exception as e:
        customer = CustomException(e,sys) 
        logging.info(customer.error_message) 
        logging.info('We are testing logging module') 
        return "Hello World" 
     

if __name__=="__main__":
    app.run(port='5000',debug=True) 