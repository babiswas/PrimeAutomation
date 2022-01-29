from flask import Blueprint

testcase=Blueprint('testcase',__name__,url_prefix='/testcase')
home=Blueprint('home',__name__,url_prefix='/home')
account=Blueprint('account',__name__,url_prefix='/account')