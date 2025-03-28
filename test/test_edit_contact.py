from model.contact import Contact
import datetime
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


def random_digits(maxamount):
    return str(random.randrange(1, maxamount))


def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return random.choice(months)


testdata = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            title=random_string("title", 10), company=random_string("company", 10),
            address=random_string("address", 10), home_phone=random_string("home", 10),
            mobile_phone=random_string("mobile", 10), work_phone=random_string("work", 10),
            fax=random_string("fax", 10), email=random_string("email", 10),
            email2=random_string("email2", 10), email3=random_string("email3", 10),
            home_articles=random_string("homepage", 10), bday=random_digits(32), bmonth=random_month(),
            byear=random_digits(2021), aday=random_digits(32), amonth=random_month(),
            ayear=random_digits(2021), new_group="[none]")
    for i in range(5)
]


# @pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_edit_contact_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="From edit function", new_group="[none]"))
    old_contacts = db.get_contact_list()
    mod_contact = random.choice(old_contacts)
    contact = Contact(firstname="Cat", middlename="Second", lastname="Boooook")
    contact.id = mod_contact.id
    app.contact.edit_contact_by_id(mod_contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contact_f = next(c for c in old_contacts if c.id == contact.id)
    old_contact_f.firstname = contact.firstname
    old_contact_f.lastname = contact.lastname
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
