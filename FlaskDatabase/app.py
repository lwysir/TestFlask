from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:root@127.0.0.1:3306/flask'

@app.route('/')
def hello_world():  # put application's code here
    print('hello world')
    return 'Hello World! !!'


if __name__ == '__main__':
    app.run()
