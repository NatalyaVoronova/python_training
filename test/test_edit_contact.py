from model.contact import Contact
import datetime


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="From edit function", new_group="[none]"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="Иван", lastname="Бубликов "
                                                                      + str(datetime.datetime.now())))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
