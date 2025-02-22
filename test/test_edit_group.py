# -*- coding: utf-8 -*-
#from model.group import Group
import datetime

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group("Optimus Prime " + str(datetime.datetime.now().time()), "header", "footer description")
    app.session.logout()

