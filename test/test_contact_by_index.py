from random import randrange
import re


def test_contact_by_index_on_home_page(app):  #
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == clear_end(contact_from_edit_page.firstname)
    assert contact_from_home_page.lastname == clear_end(contact_from_edit_page.lastname)
    assert contact_from_home_page.address == clear_end(contact_from_edit_page.address)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_phone_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_phone_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def clear_end(s):
    return re.sub(r'\s{2,}|(\s$)', '', s)


def clear_spase(s):
    return re.sub(r'\s{2,}|(\s$)', ' ', s).strip()


def merge_phones_like_on_phone_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                        contact.secondary_phone]))))


def merge_emails_like_on_phone_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_spase(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
