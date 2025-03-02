from model.contact import Contact
import datetime


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="From edit function", new_group="[none]"))
    app.contact.edit_first_contact(Contact(firstname="Иван", lastname="Бубликов "
                                                                      + str(datetime.datetime.now())))
