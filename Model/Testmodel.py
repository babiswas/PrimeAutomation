from Model import db
from sqlalchemy.dialects.postgresql import JSON

class Testcase(db.Model):
    __tablename__="testcase"
    id=db.Column(db.String(20),nullable=False,unique=True,primary_key=True)
    tags=db.Column(db.String(100),nullable=False,unique=True)
    description=db.Column(db.String(100),nullable=False)
    resourcePath=db.Column(db.String(100),nullable=False)
    method=db.Column(db.String(100),nullable=False)
    env_id=db.Column(db.Integer,db.ForeignKey('primeconfig.id'))
    acc_id=db.Column(db.Integer,db.ForeignKey('account.id'))
    child=db.relationship('Testdata',backref='testcasedata',uselist=False)

    def __str__(self):
        return f"{self.id} {self.method} {self.tags}"

    def __init__(self,id,tags,description,resourcePath,method,accountid,envid):
        self.id=id
        self.tags=tags
        self.description=description
        self.resourcePath=resourcePath
        self.method=method
        self.acc_id=accountid
        self.env_id=envid

class PrimeConfig(db.Model):
    __tablename__="primeconfig"
    id=db.Column(db.Integer,nullable=False,unique=True,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    description=db.Column(db.String(100),nullable=False)
    enviromenturl=db.Column(db.String(100),nullable=False)
    testcase=db.relationship("Testcase",backref="enviroment")
    account=db.relationship("Account",backref="primeaccount")

    def __str__(self):
        return f"{self.id} {self.method} {self.tags}"

    def __init__(self,enviromenturl):
        self.enviromenturl=enviromenturl


class Account(db.Model):
    __tablename__="account"
    id=db.Column(db.Integer,nullable=False,unique=True,primary_key=True)
    accountid=db.Column(db.String(100),nullable=False)
    name=db.Column(db.String(100),nullable=False)
    clientid=db.Column(db.String(100),nullable=False)
    clientsecret=db.Column(db.String(100),nullable=False)
    refreshtoken=db.Column(db.String(100),nullable=False)
    env_id=db.Column(db.Integer,db.ForeignKey('primeconfig.id'))
    account=db.relationship("Testcase",backref="testaccount")

    def __str__(self):
        return f"{self.id} {self.method} {self.tags}"

    def __init__(self,name,accountid,clientid,clientsecret,refreshtoken,envid):
        self.accountid=accountid
        self.name=name
        self.clientid=clientid
        self.clientsecret=clientsecret
        self.refreshtoken=refreshtoken
        self.env_id=envid


class Testdata(db.Model):
        __tablename__="testdata"
        id=db.Column(db.Integer,nullable=False,unique=True,primary_key=True)
        data=db.Column(JSON)
        testcase_id=db.Column(db.String(20),db.ForeignKey('testcase.id'))


        def __init__(self,data,testid):
            self.data=data
            self.testcase_id=testid

        def __str__(self):
            return f"{self.testid}"





    
   
