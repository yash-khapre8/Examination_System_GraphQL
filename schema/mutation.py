import graphene
from schema.student_schema import StudentType
from schema.exam_schema import ExamType
from schema.question_schema import QuestionType
from schema.option_schema import OptionType
from schema.attempt_schema import AttemptType
from resolvers.student_resolver import StudentResolver
from resolvers.exam_resolver import ExamResolver
from resolvers.question_resolver import QuestionResolver

class CreateStudent(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        status = graphene.String()
    
    student = graphene.Field(StudentType)

    def mutate(self, info, name, email, status='active'):
        student = StudentResolver.create_student(name, email, status)
        return CreateStudent(student=student)

class CreateExam(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        duration = graphene.Int(required=True)
        status = graphene.String()
    
    exam = graphene.Field(ExamType)

    def mutate(self, info, title, duration, status='upcoming'):
        exam = ExamResolver.create_exam(title, duration, status)
        return CreateExam(exam=exam)

class StartExamInput(graphene.InputObjectType):
    student_id = graphene.Int(required=True)
    exam_id = graphene.Int(required=True)

class StartExam(graphene.Mutation):
    class Arguments:
        input = StartExamInput(required=True)
    
    attempt = graphene.Field(AttemptType)

    def mutate(self, info, input):
        attempt = ExamResolver.start_exam(input.student_id, input.exam_id)
        return StartExam(attempt=attempt)

class AnswerInput(graphene.InputObjectType):
    question_id = graphene.ID(required=True)
    option_id = graphene.ID(required=True)

class SubmitExam(graphene.Mutation):
    class Arguments:
        student_id = graphene.Int(required=True)
        exam_id = graphene.Int(required=True)
        answers = graphene.List(AnswerInput, required=True)
    
    attempt = graphene.Field(AttemptType)

    def mutate(self, info, student_id, exam_id, answers):
        attempt = ExamResolver.submit_exam(student_id, exam_id, answers)
        return SubmitExam(attempt=attempt)

class CreateQuestion(graphene.Mutation):
    class Arguments:
        exam_id = graphene.Int(required=True)
        text = graphene.String(required=True)
        marks = graphene.Int(required=True)
    
    question = graphene.Field(QuestionType)

    def mutate(self, info, exam_id, text, marks):
        question = QuestionResolver.create_question(exam_id, text, marks)
        return CreateQuestion(question=question)

class CreateOption(graphene.Mutation):
    class Arguments:
        question_id = graphene.Int(required=True)
        text = graphene.String(required=True)
        is_correct = graphene.Boolean(required=True)
    
    option = graphene.Field(OptionType)

    def mutate(self, info, question_id, text, is_correct):
        option = QuestionResolver.create_option(question_id, text, is_correct)
        return CreateOption(option=option)

class Mutation(graphene.ObjectType):
    create_student = CreateStudent.Field()
    create_exam = CreateExam.Field()
    start_exam = StartExam.Field()
    submit_exam = SubmitExam.Field()
    create_question = CreateQuestion.Field()
    create_option = CreateOption.Field()
    
    # Other management mutations
    update_student = graphene.Field(StudentType, id=graphene.Int(required=True), name=graphene.String(), email=graphene.String(), status=graphene.String())
    def resolve_update_student(self, info, id, name=None, email=None, status=None):
        return StudentResolver.update_student(id, name, email, status)
