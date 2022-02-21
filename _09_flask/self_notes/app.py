from flask import Flask,request,jsonify

app=Flask(__name__)


@app.route('/')
def fun():
    return 'this is flask first app'


if __name__=='__main__':
    app.run()

@app.route('/home/<int:number>')
def some_fun2(number):
    return even_check(number)

