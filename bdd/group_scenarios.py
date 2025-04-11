from pytest_bdd import scenario
from .contact_steps import *
from .group_steps import *

@scenario('groups.feature', 'Add new group')
def test_add_new_group():
    pass


@scenario('groups.feature', 'Delete a group')
def test_delete_group():
    pass

@scenario("contacts.feature", "Add new contact")
def test_add_new_contact():
    pass

@scenario("contacts.feature", "Delete a contact")
def test_delete_contact():
    pass

@scenario("contacts.feature", "Modify a contact")
def test_modify_contact():
    pass
