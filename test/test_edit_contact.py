from model.contact import Contact
import datetime


def test_edit_first_contact(app):
    app.contact.edit(Contact(firstname="Иван", lastname="Бубликов " + str(datetime.datetime.now().time())))

