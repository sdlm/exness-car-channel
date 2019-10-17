import datetime

import peewee


class Room(peewee.Model):
    pk = peewee.PrimaryKeyField()
    name = peewee.CharField(null=True)
    created = peewee.DateTimeField(default=datetime.datetime.utcnow)


class User(peewee.Model):
    pk = peewee.PrimaryKeyField()
    id = peewee.IntegerField()
    room = peewee.ForeignKeyField(model=Room)
