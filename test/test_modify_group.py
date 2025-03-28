from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20),
          footer=random_string("footer", 20)) for i in range(5)
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_modify_group_name(app, group):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = random.randrange(len(old_groups))
    group.id = old_groups[index].id  # запоминаем id группы до внесения изменений в группу
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_modify_group_by_id(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = Group(name="Mod_test")
    old_groups = db.get_group_list()
    group_mod = random.choice(old_groups)
    group.id = group_mod.id
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    old_group_name = next(g for g in old_groups if g.id == group.id)
    old_group_name.name = group.name
    assert old_groups == new_groups
    if check_ui:
        # assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
        #  без функции clean тест падает, если в конце имени группы есть пробел - на ui его нет, в бд - есть
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        db_list_new_groups = map(clean, new_groups)
        assert sorted(db_list_new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
