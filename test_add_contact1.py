# -*- coding: utf-8 -*-
import pytest
from application import Application
from contact import Contact

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact1(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="name One", middlename="name two", lastname="nameLast", nickname="bookman", title="ttttitle", company="BookZoo", address="Moscow",
                            home_phone="+495000000", mobile_phone="+3587945", work="back", fax="+6987532", email1="sdfgred@gmail.com", email2="twomail@gmail.com",
                            email3="thrmail@gmail.com", home_articles="https://habr.com/ru/articles/737132/"))
    # app.select_group()
    # app.confirm_the_creation_of_the_contact()
    # app.return_to_home_page()
    app.logout()
