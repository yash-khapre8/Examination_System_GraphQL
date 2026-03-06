import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Exam

class ExamType(SQLAlchemyObjectType):
    class Meta:
        model = Exam
        interfaces = (graphene.relay.Node, )
