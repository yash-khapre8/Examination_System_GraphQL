import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Option

class OptionType(SQLAlchemyObjectType):
    class Meta:
        model = Option
        interfaces = (graphene.relay.Node, )
