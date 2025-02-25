# -*- coding: utf-8 -*-
#from model.group import Group
import datetime

def test_edit_first_group(app):
    app.group.edit_first_group("Optimus Prime " + str(datetime.datetime.now().time()), "header", "footer description")


