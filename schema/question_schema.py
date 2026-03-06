import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Question

class QuestionType(SQLAlchemyObjectType):
    class Meta:
        model = Question
        interfaces = (graphene.relay.Node, )
