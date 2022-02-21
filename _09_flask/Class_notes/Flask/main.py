# MVT --> model view template

from flask import Flask,request,jsonify
from service import even_check

app = Flask(__name__)

@app.route('/')
def some_fun():
    return "Hello World"

@app.route('/home/<int:number>')
def some_fun2(number):
    return even_check(number)

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
                

if __name__ == '__main__':
    app.run()