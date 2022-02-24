import graphene
from graphene_django import DjangoObjectType
from addressbook import models


class ContactType(DjangoObjectType):
    class Meta:
        model = models.Contact
