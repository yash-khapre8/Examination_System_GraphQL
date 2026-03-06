import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Response

class ResponseType(SQLAlchemyObjectType):
    class Meta:
        model = Response
        interfaces = (graphene.relay.Node, )
