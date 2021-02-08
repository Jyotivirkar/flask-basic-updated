from flask import Flask
from flask import request

app=Flask(__name__) 

@app.route('/') 
def index() :
  return "<h1>Go to /puppy_name/name and see result</h1>

@app.route('/puppy_name/name') 
def puppylatin(name):
   Pupname=''
  if name[-1]=='y':
    Pupname= name[-1]+'iful'
  else:
    Pupname=name+'y'
  return "your puppy Latin name is:{}".format(pupname)
  if __name__=='__main__':
    app.run() 
