# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact1(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Today name One", middlename="name two", lastname="nameLast 02/03/22-17",
                      nickname="bookman", title="ttttitle", company="BookZoo", address="Moscow",
                      home_phone="+495000000", mobile_phone="+3587945", work="back", fax="+6987532",
                      email1="sdfgred@gmail.com", email2="twomail@gmail.com", email3="thrmail@gmail.com",
                      home_articles="https://habr.com/ru/articles/737132/", bday="29", bmonth="December",
                      byear="2023", aday="30", amonth="June", ayear="2024",
                      new_group="[none]")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    print("\nдлина списка ", len(new_contacts))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="", middlename="", lastname="",
#                       new_group="[none]")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
