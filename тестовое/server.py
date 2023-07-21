from flask import Flask, request, render_template
import pandas as pd
from to_sql import Db
import time


# app = Flask(__name__)
# eng = create_engine('postgresql+psycopg2://user1:1234@localhost:5432/test')
# eng.connect()
db = Db()

app = Flask(__name__)

@app.route('/')
def upload():
    # print(dir(self))
    return '''<html> 
                    <head> 
                    <title>upload</title> 
                    </head> 
                    <body> 
                    <form action = "/success" method = "post" enctype="multipart/form-data"> 
                    <input type="file" name="file" /> 
                    <input type = "submit" value="Upload">
                    <H2>
                    <head>
                    <a href="/s" class="button">Get Info</a>
                    </form> 
                    </body> 
                    </html>
        '''
    
@app.route('/success', methods = ['POST']) 
def success():
        print(request.method)
        if request.method == 'POST': 
            f = request.files['file']
            if f.filename.endswith('.csv') == False:
                return 'Error'
            df = pd.read_csv(f)
            # db.add_to_list_of_files(f.filename.replace('.csv', ''), df_to_dict(df.dtypes))
            try:
                df.to_sql(db.add_to_list_of_files(f.filename.replace('.csv', ''), df_to_dict(df.dtypes)),
                             db.engine, index=False)
            except:
                 return 'Database Error'
            # db.get_info()
            return f'''
                <html> 
                <head> 
                <title>success</title> 
                </head> 
                <body> 
                <p>File uploaded successfully</p> 
                <p>File Name: {f.filename}</p> 
                </body> 
                </html>
            '''
        
@app.route('/s', methods = ['GET'])        
def get_info():
    print()
    if request.method == 'GET':
        db.get_info()
    return ""

def df_to_dict(info) -> dict:
    res = {}

    for key in dict(info):
        if info[key] == 'object':
               res[key] = 'string'
        else:
             res[key] = str(info[key])
    return res 
        

    
# App().app.run()

app.run()