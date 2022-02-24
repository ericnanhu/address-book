import graphene
from addressbook import models, types


# The Query class
class Query(graphene.ObjectType):
    all_contacts = graphene.List(types.ContactType)
    contact_by_id = graphene.Field(types.ContactType, id=graphene.ID())

    def resolve_all_contacts(root, info):
        return (
            models.Contact.objects.all()
        )

    def resolve_contact_by_id(root, info, id):
        return (
            models.Contact.objects.get(pk=id)
        )