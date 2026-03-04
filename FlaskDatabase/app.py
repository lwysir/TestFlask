
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import config
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData
app = Flask(__name__)
app.config.from_object(config)

# db = SQLAlchemy(app)
#定义命名约定的Base类
class Base(DeclarativeBase):
    metadata = MetaData(naming_convention = {
        #ix:index,索引。
        "ix": 'ix_%(column_0_label)s',
        #Un:unique,唯一约束
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        #ck:Check,检查约柬
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        #fk:Foreign Key,外键约束
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        #pk:Primary Key,主键约束
        "pk": "pk_%(table_name)s"
    })


db = SQLAlchemy(app=app,model_class=Base)


@app.route('/')
def hello_world():  # put application's code here
    print('hello world')
    print('Mathe')
    print('123456789')
    return 'Hello World! !!'


if __name__ == '__main__':
    app.run()
