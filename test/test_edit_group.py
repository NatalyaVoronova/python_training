# -*- coding: utf-8 -*-
from model.group import Group
import datetime


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="Optimus Prime " + str(datetime.datetime.now().time()),
                                     header="New constellation" + str(datetime.datetime.now().time())))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
