def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group()
    app.session.logout()
