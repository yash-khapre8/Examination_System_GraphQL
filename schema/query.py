import graphene
from schema.student_schema import StudentType
from schema.exam_schema import ExamType
from schema.question_schema import QuestionType
from schema.attempt_schema import AttemptType
from resolvers.student_resolver import StudentResolver
from resolvers.exam_resolver import ExamResolver
from resolvers.question_resolver import QuestionResolver

class Query(graphene.ObjectType):
    get_students = graphene.List(StudentType)
    get_student_by_id = graphene.Field(StudentType, id=graphene.Int(required=True))
    get_exams = graphene.List(ExamType)
    get_exam_by_id = graphene.Field(ExamType, id=graphene.Int(required=True))
    get_questions_by_exam = graphene.List(QuestionType, exam_id=graphene.Int(required=True))
    get_attempts_by_student = graphene.List(AttemptType, student_id=graphene.Int(required=True))

    def resolve_get_students(self, info):
        return StudentResolver.get_all_students()

    def resolve_get_student_by_id(self, info, id):
        return StudentResolver.get_student_by_id(id)

    def resolve_get_exams(self, info):
        return ExamResolver.get_all_exams()

    def resolve_get_exam_by_id(self, info, id):
        return ExamResolver.get_exam_by_id(id)

    def resolve_get_questions_by_exam(self, info, exam_id):
        return QuestionResolver.get_questions_by_exam(exam_id)

    def resolve_get_attempts_by_student(self, info, student_id):
        return StudentResolver.get_attempts_by_student(student_id)
