from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="count", new_group="[none]"))
    app.contact.delete()
