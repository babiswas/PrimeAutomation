from wtforms import Form,StringField


class TestForm(Form):
        id=StringField("TestId")
        tags=StringField("TestTag")
        description=StringField("Description")
        resourcePath=StringField("ResourcePath")
        method=StringField("Method")


class AccountForm(Form):
        name=StringField("Name")
        accountid=StringField("AccountId")
        clientid=StringField("Client Id")
        clientsecret=StringField("Client Secret")
        refreshtoken=StringField("Refresh Token")


class EnviromentForm(Form):
        name=StringField("Name")
        accountid=StringField("AccountId")
        clientid=StringField("Client Id")
        clientsecret=StringField("Client Secret")
        refreshtoken=StringField("Refresh Token")
            