import graphene
from addressbook import queries, mutations


schema = graphene.Schema(query=queries.Query, mutation=mutations.Mutation)
