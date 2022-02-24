import graphene
from graphene_file_upload.scalars import Upload
from addressbook import models, types


# Mutation sends data to the database


class CreateContact(graphene.Mutation):
    contact = graphene.Field(types.ContactType)

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        image = Upload(required=True)

    def mutate(self, info, first_name, last_name, email, phone, image):
        contact = models.Contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            image=image,
        )
        contact.save()

        return CreateContact(contact=contact)


class UpdateContact(graphene.Mutation):
    contact = graphene.Field(types.ContactType)

    class Arguments:
        contact_id = graphene.ID(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        image = Upload(required=True)

    def mutate(self, info, contact_id, first_name, last_name, email, phone, image):
        contact = models.Contact.objects.get(pk=contact_id)

        contact.first_name = first_name
        contact.last_name = last_name
        contact.email = email
        contact.phone = phone
        contact.image = image

        contact.save()

        return UpdateContact(contact=contact)


class DeleteContact(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        contact_id = graphene.ID(required=True)

    def mutate(self, info, contact_id):
        contact = models.Contact.objects.get(pk=contact_id)
        contact.delete()

        return DeleteContact(success=True)

class Mutation(graphene.ObjectType):
    create_contact = CreateContact.Field()
    update_contact = UpdateContact.Field()
    delete_contact = DeleteContact.Field()
