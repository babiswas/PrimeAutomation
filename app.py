from Model import db
from flask import Flask
from Route.route import testcase
from controller import test_views
from controller import home_views


class Config:
   SECRET_KEY="hello"
   SQLALCHEMY_DATABASE_URI="postgresql://postgres:36network@localhost:5432/hello"
   SQLALCHEMY_TRACK_MODIFICATIONS=False


def create_app():
   app=Flask(__name__)
   app.config.from_object(Config)
   db.init_app(app)
   with app.app_context():
      db.create_all()
   app.register_blueprint(testcase)
   return app

if __name__=="__main__":
   app=create_app()
   app.run(debug=True)
