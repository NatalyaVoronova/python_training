import random

from model.contact import Contact
from model.group import Group


def test_del_user_to_group(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="fn for add", lastname="ln for add"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group for add"))
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    groups = orm.get_group_list()
    group = random.choice(groups)
    if contact in orm.get_contacts_not_in_group(group):
        app.contact.add_contact_in_group(contact.id, group.id)
    app.contact.del_contact_from_group(contact.id, group.id)
    assert contact not in orm.get_contacts_in_group(group)
