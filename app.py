from flask import Flask
app =Flask(__name__)
@app.route('/')
def hello():
return "hello from Sanjit openshift flask app!"
if _ _name__=='__main__':
app.run(host0.0.0.0.0',port=8080)
