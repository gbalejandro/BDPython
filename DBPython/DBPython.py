from peewee import *
from datetime import date

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db

def create_and_connect():
    db.connect()
    db.create_tables([Person,Pet])

def create_family_members():
    uncle_tommy = Person(name='Tommy', birthday=date(1945, 10, 7),is_relative=True)
    uncle_tommy.save()

    grandma_ana = Person.create(name="Ana",birthday=date(1930, 1, 21),is_relative=True)

    tommys_dog = Pet.create(owner=uncle_tommy, name='Kitty', animal_type='dog')
    anas_cat = Pet.create(owner=grandma_ana, name='Mittens', animal_type='cat')

create_and_connect()
create_family_members()

for person in Person.select():
    print(person.name)
