from model.contact import Contact
from random import randrange
import datetime


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="From edit function", new_group="[none]"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Иван", lastname="Бубликов " + str(datetime.datetime.now()))
    contact.id = old_contacts[index].id
    app.contact.edit_first_contact(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
