from Model import db
from Model.Testmodel import Testcase,PrimeConfig
from Route.route import testcase
from flask import request
from forms.forms import TestForm
from flask import redirect
from flask import url_for
from flask import render_template

@testcase.route('/<int:envid>/add/<int:accountid>',methods=['GET','POST'])
def add_create_tests(envid,accountid):
      testform=TestForm(request.form)
      if request.method=="POST" and testform.validate:
         testid=request.form.get("id")
         testtag=request.form.get("tags")
         testdescription=request.form.get("description")
         testresource=request.form.get("resourcePath")
         mthd=request.form.get("method")
         testcase=Testcase(testid,testtag,testdescription,testresource,mthd,accountid,envid)
         db.session.add(testcase)
         db.session.commit()
         return redirect(url_for("testcase.test_list",accountid=accountid))
      return render_template("add_test.html",form=testform)


@testcase.route('/<int:accountid>/read',methods=['GET'])
def test_list(accountid):
      testlist=Testcase.query.filter_by(acc_id=accountid).all()
      return render_template('test_list.html',testlist=testlist)


@testcase.route('/edit/<int:testid>',methods=['GET','POST'])
def account_list(testid):
         testobj=Testcase.query.get(testid)
         testform=TestForm(obj=testobj)
         if request.method=="POST" and testform.validate:
               testobj.testtag=request.form.get("tags")
               testobj.testdescription=request.form.get("description")
               testobj.testresource=request.form.get("resourcePath")
               testobj.method=request.form.get("Method")
               db.session.commit()
               return redirect(url_for("testcase.read"))
         return render_template("add_test.html",form=testform)

   
       


