# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Group name is New 36", header="This 36", footer="mushrooms 36"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
