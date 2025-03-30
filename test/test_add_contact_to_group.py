import random

from model.contact import Contact
from model.group import Group


def test_add_contact_with_group(app, orm_db):
    group_list = app.contact.get_group_list()
    if len(group_list) == 0:
        app.group.create(Group(name="test", header="header_test", footer="footer_test"))
        app.open_home()
        group_list = app.contact.get_group_list()
    random_group_id = random.choice(group_list)
    contacts_not_in_group = orm_db.get_contacts_not_in_group_by_id(random_group_id)
    if len(contacts_not_in_group) == 0 or app.contact.count() == 0:
        app.contact.create(Contact(firstname="edit", middlename="middlename", lastname="last test", nickname="nicktest",
                                   title="title test", company="company test", address="address test",
                                   home_phone="+7843564224", mobile_phone="+7946545455",
                                   work_phone="+9373632923", fax="+432423", email="test@mail.ru",
                                   email2="test2@yandex.ru", email3="test3@yandex.ru",
                                   articles="homepage", bday="11", bmonth="August",
                                   byear="1998", aday="13", amonth="August", ayear="1999",
                                   secondary_phone="secondary home test"))
        contacts_not_in_group = orm_db.get_contacts_not_in_group_by_id(random_group_id)
    random_contact = random.choice(contacts_not_in_group)
    app.contact.select_contact_by_id_to_add(random_contact.id)
    random_group_id = random.choice(group_list)
    app.contact.change_select_value_by_value('to_group', random_group_id)
    app.contact.click_add_too()
    contacts = orm_db.get_contact_in_group_by_id(random_group_id)  #
    contact_found = False
    for c in contacts:
        if c.id == random_contact.id:
            contact_found = True
    assert contact_found, f"contact {random_contact.id} doesn't exist in group {random_group_id}"
