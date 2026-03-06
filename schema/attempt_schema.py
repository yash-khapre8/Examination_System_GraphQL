import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Attempt

class AttemptType(SQLAlchemyObjectType):
    class Meta:
        model = Attempt
        interfaces = (graphene.relay.Node, )
