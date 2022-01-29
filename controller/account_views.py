from flask import jsonify
from Model import db
from Model.Testmodel import Account
from Route.route import account
from flask import request
from forms.forms import TestForm
from flask import redirect
from flask import url_for
from flask import render_template


@account.route('/add',methods=['GET','POST'])
def add_create_tests():
      accountform=AccountForm(request.form)
      if request.method=="POST" and accountform.validate:
         testid=request.form.get("id")
         testtag=request.form.get("tags")
         testdescription=request.form.get("description")
         testresource=request.form.get("resourcePath")
         method=request.form.get("Method")
         account=Account(testid,testtag,testdescription,testresource,method)
         db.session.add(account)
         db.session.commit()
         return redirect(url_for("account.read_all"))
      return render_template("add_account.html",form=accountform)