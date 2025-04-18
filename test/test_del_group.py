import random
from model.group import Group


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)  # удаление из списка группы по id
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)  # удаление из списка группы по id, выбранной ранее рандомно
    assert old_groups == new_groups  # оба списка получены из БД; app.group.get_group_list() - из интерфейса
    if check_ui:
        # assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
        #  без функции clean тест падает, если в конце имени группы есть пробел - на ui его нет, в бд - есть
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        db_list_new_groups = map(clean, new_groups)
        assert sorted(db_list_new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
