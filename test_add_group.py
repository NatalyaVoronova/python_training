# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from application import Application
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="First", header="This", footer="mushrooms"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()


