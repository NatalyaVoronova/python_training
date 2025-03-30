from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders, conversions, encoders


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):  # db.Entity - вложенный класс описывает объекты базы данных
        _table_ = 'group_list'  # название таблицы
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        # связь осуществляется через таблицу table="address_in_groups;  # reverse="groups" -  пара к Контакту это параметр группы
        # lazy - информация будет извлекаться в тот момент, когда мы обращаемся к свойству, а не рекурсивно по всем связям м/у объектами
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')  # необходимо для фильтрации
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):  # привязка к базе данных через bind
        self.db.bind('mysql', host=host, database=name, user=user, password=password)  # , conv=decoders)
        # generate_mapping - сопоставление свойств описанных выше классов с таблицами БД и их полями
        self.db.generate_mapping()
        sql_debug(True)  # покажет какие sql-запросы передаются

    def convert_groups_to_model(self, groups):  # преобразовывает ORM в обычный объект Group
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):  #
        # list(select(g for g in ORMFixture.ORMGroup))  # вернет список ORM-объектов, т.е. без id + имя + описание группы
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))  # нужна вспомогатательная f

    # def get_group_list(self):  # вариант указания работы сессии с бд через with
    #     with db_session:
    #         return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):  # преобразовывает ORM в обычный объект Contact
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contact_in_group_by_id(self, id):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))

    @db_session
    def get_contacts_not_in_group_by_id(self, id):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))
