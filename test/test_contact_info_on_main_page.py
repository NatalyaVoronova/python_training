import re
from model.contact import Contact


def test_contact_info_check(app, db):
    contact_from_db = sorted(db.get_contacts_list_like_on_home_page(), key=Contact.id_or_max)
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contact_from_db)):
        assert contact_from_home_page[i].firstname == contact_from_db[i].firstname
        assert contact_from_home_page[i].lastname == contact_from_db[i].lastname
        assert contact_from_home_page[i].address.replace(' ', '') == contact_from_db[i].address.replace(' ', '')
        assert contact_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db[i])
        assert contact_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db[i])


def clear(s):
    return re.sub("[() -]", "", s)


def clear_spase(s):
    return re.sub(r'\s{2,}|(\s$)', ' ', s).strip()


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                        contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_spase(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
