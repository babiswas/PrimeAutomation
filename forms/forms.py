from wtforms import Form,StringField


class TestForm(Form):
        id=StringField("TestId")
        tags=StringField("TestTag")
        description=StringField("Description")
        resourcePath=StringField("ResourcePath")
        method=StringField("Method")
            