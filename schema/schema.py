import graphene
from schema.query import Query
from schema.mutation import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
