from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Config(object):
    SECRET_KEY = 'AERsf43432ss'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@39.98.39.173:13306/xfy'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)


    from apps.xufeiyu import xufeiyu
    from apps.zhouzy import zhouzy
    app.register_blueprint(xufeiyu, url_prefix="/xfy")
    app.register_blueprint(zhouzy, url_prefix="/zzy")



    return app