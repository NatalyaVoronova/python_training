# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert old_groups == new_groups  # оба списка получены из БД; app.group.get_group_list() - из интерфейса
    if check_ui:
        # assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
        #  без функции clean тест падает, если в конце имени группы есть пробел - на ui его нет, в бд - есть
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        db_list_new_groups = map(clean, new_groups)
        assert sorted(db_list_new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
