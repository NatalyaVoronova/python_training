# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact1(app):
    app.contact.create(Contact(firstname="Today name One", middlename="name two", lastname="nameLast 02/03/22-17",
                               nickname="bookman", title="ttttitle", company="BookZoo", address="Moscow",
                               home_phone="+495000000", mobile_phone="+3587945", work="back",
                               fax="+6987532", email1="sdfgred@gmail.com", email2="twomail@gmail.com",
                               email3="thrmail@gmail.com", home_articles="https://habr.com/ru/articles/737132/",
                               bday="29", bmonth="December", byear="2023", aday="30", amonth="June", ayear="2024",
                               new_group="[none]"))
    # app.select_group()
    # app.confirm_the_creation_of_the_contact()
    # app.return_to_home_page()
