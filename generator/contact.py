from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o =="-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


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
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
