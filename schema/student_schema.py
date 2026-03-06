import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Student

class StudentType(SQLAlchemyObjectType):
    class Meta:
        model = Student
        interfaces = (graphene.relay.Node, )
