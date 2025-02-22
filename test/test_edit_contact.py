

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit("Иван", "Бубликов33")
    app.session.logout()
