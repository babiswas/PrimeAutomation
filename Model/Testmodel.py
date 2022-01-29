from Model import db

class Testcase(db.Model):
   __tablename__="testcase"
   id=db.Column(db.String(20),nullable=False,unique=True,primary_key=True)
   tags=db.Column(db.String(100),nullable=False,unique=True)
   description=db.Column(db.String(100),nullable=False)
   resourcePath=db.Column(db.String(100),nullable=False)
   method=db.Column(db.String(100),nullable=False)
   env_id=db.Column(db.Integer,db.ForeignKey('primeconfig.id'))

   def __str__(self):
       return f"{self.id} {self.method} {self.tags}"

   def __init__(self,id,tags,description,resourcePath,method):
       print("Executing init method")
       self.id=id
       self.tags=tags
       self.description=description
       self.resourcePath=resourcePath
       self.method=method

class PrimeConfig(db.Model):
   __tablename__="primeconfig"
   id=db.Column(db.Integer,nullable=False,unique=True,primary_key=True)
   enviromenturl=db.Column(db.String(100),nullable=False)
   testcase=db.relationship("testcase",backref="enviroment")

   def __str__(self):
       return f"{self.id} {self.method} {self.tags}"

   def __init__(self,enviromenturl):
       self.enviromenturl=enviromenturl


class AccountConfig(db.Model):
   __tablename__="primeconfig"
   id=db.Column(db.Integer,nullable=False,unique=True,primary_key=True)
   env_id=db.Column(db.Integer,db.ForeignKey('primeconfig.id'))

   def __str__(self):
       return f"{self.id} {self.method} {self.tags}"

   def __init__(self,enviromenturl):
       self.enviromenturl=enviromenturl
   
   
