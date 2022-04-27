from flask import Flask,request,jsonify
from service3 import fun_even
app=Flask(__name__)


@app.route('/')
def fun():
    return 'this is second first app'

if __name__=='__main__':
    app.run(debug = True)

