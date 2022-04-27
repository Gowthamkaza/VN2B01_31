from flask import Flask,request,jsonify
from service2 import func3_even,func4_age


app=Flask(__name__)


@app.route('/')
def fun():
    return 'this is flask first app'



@app.route('/home3/<int:number>')
def some_fun2(number):
    return func3_even(number)


@app.route('/gl/')
def some_func5():
    return 'this is the thing created'


@app.route('/post-end',methods=['POST','GET'])
def post_method():
    if request.method == 'POST':
        name = request.json['name']
        id = request.json['id']
        try:
            if type(name) == str:
                print('...............name....',type(name))
                print('...........id.................',type(id))
                return f'my name is {name} and id is {id}'
            else:
                raise ValueError("you have entered invalid string")
        except ValueError as ve:
            print(ve)
            return 'from except bloclk'
    else:
        return "im a get mothod"

if __name__=='__main__':
    app.run(debug = True)



