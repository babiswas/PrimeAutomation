from Model import db
from Model.Testmodel import Account
from Route.route import account
from flask import request
from forms.forms import AccountForm
from flask import redirect
from flask import url_for
from flask import render_template


@account.route('/add',methods=['GET','POST'])
def add_account():
      accountform=AccountForm(request.form)
      if request.method=="POST" and accountform.validate:
         accountid=request.form.get("id")
         clientid=request.form.get("tags")
         clientsecret=request.form.get("description")
         refreshtoken=request.form.get("resourcePath")
         account=Account(accountid,clientid,clientsecret,refreshtoken)
         db.session.add(account)
         db.session.commit()
         return redirect(url_for("account.read_all"))
      return render_template("add_account.html",form=accountform)


@account.route('/read',methods=['GET'])
def account_list():
      page=request.args.get('page',1,type=int)
      accountlist=Account.query.paginate(page=page,per_page=5)
      next_url=url_for('account.account_list',page=accountlist.next_num) if accountlist.has_next else None
      prev_url=url_for('account.account_list',page=accountlist.prev_num) if accountlist.has_prev else None
      return render_template('account_list.html',accountlist=accountlist,next_url=next_url,prev_url=prev_url)