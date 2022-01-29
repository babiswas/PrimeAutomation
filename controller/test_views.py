from flask import jsonify
from Model import db
from Model.Testmodel import Testcase
from Route.route import testcase
from flask import request
from forms.forms import TestForm
from flask import redirect
from flask import url_for
from flask import render_template

@testcase.route('/add',methods=['GET','POST'])
def add_create_tests():
      testform=TestForm(request.form)
      if request.method=="POST" and testform.validate:
         testid=request.form.get("id")
         testtag=request.form.get("tags")
         testdescription=request.form.get("description")
         testresource=request.form.get("resourcePath")
         method=request.form.get("Method")
         testcase=Testcase(testid,testtag,testdescription,testresource,method)
         db.session.add(testcase)
         db.session.commit()
         return redirect(url_for("testcase.read_all"))
      return render_template("add_test.html",form=testform)


@testcase.route('/read',methods=['GET'])
def test_list():
      page=request.args.get('page',1,type=int)
      testlist=Testcase.query.paginate(page=page,per_page=5)
      next_url=url_for('testcase.test_list',page=testlist.next_num) if testlist.has_next else None
      prev_url=url_for('testcase.test_list',page=testlist.prev_num) if testlist.has_prev else None
      return render_template('test_list.html',testlist=testlist,next_url=next_url,prev_url=prev_url)

   
       


