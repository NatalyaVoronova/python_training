
from pytest_bdd import given, when, then, parsers
from model.contact import Contact
import random


@given('a contact list', target_fixture="contact_list")
def contact_list(db):
    return db.get_contact_list()

@given(parsers.parse("a contact with {firstname} and {lastname}"), target_fixture="new_contact")
def new_contact(firstname, lastname):
   return Contact(firstname=firstname, lastname=lastname)

@when('I add the contact to the list', target_fixture="add_new_contact")
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)

@then('The new contact list is equal to the old list with the added contact', target_fixture="verify_contact_add")
def verify_contact_add(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

@given("a non-empty contact list", target_fixture="non_empty_contact_list")
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.group.create(Contact(firstname="Test FN", lastname="Test LN"))
    return db.get_contact_list()

@given("a random contact from the list", target_fixture="random_contact")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when("I delete the contact from the list", target_fixture="delete_contact")
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@then("The new contact list is equal to the old list without deleted contact", target_fixture="verify_contact_deleted")
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

@when(parsers.parse("I modify the contact data with {firstname} and {lastname} from the list"), target_fixture="modify_contact")
def modify_contact(app, random_contact, firstname, lastname):
    contact = Contact(firstname=firstname, lastname=lastname)
    contact.id = random_contact.id
    app.contact.edit_contact_by_id(random_contact.id, contact)
    return contact

@then("The list with edited contact is equal to the old contact list", target_fixture="verify_contact_modified")
def verify_contact_modified(db, non_empty_contact_list, random_contact, modify_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    old_contacts.append(modify_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
