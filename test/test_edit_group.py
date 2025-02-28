# -*- coding: utf-8 -*-
from model.group import Group
import datetime


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="Optimus Prime " + str(datetime.datetime.now().time()),
                                     header="New constellation" + str(datetime.datetime.now().time())))
