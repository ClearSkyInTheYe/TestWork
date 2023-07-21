from flask import Flask, request

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
                    <form action = "/s" method = "get">
                    <H2>
                    <input type = "submit" value="Get_Info">
                    </form> 
                    </body> 
                    </html>
        '''


@app.route('/su', methods = ['POST']) 
def success():
    return 'asd'

@app.route('/s', methods = ['GET'])        
def get_info():
    print()
    if request.method == 'GET':
        pass
    return 'qwe'

app.run()