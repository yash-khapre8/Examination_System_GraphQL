# Online Examination System (ITM Skills University)

A production-ready GraphQL API for managing students, exams, questions, and results, built with **Python, Flask, Graphene, and SQLAlchemy**.

---

## 🚀 Project Overview
This project provides a comprehensive backend for an Online Examination System. It handles the complete lifecycle of an exam: from creation and student enrollment to real-time attempt tracking and automatic scoring.

### Tech Stack
*   **Python 3.12+**
*   **Flask**: Web Framework
*   **GraphQL (Graphene)**: API Layer
*   **SQLAlchemy ORM**: Database Management
*   **SQLite**: Development Database
*   **Flask-CORS**: Cross-Origin Support

---

## ✅ Implementation Checklist
All items requested in the project scope have been successfully implemented:

- [x] **Project Setup**: Modular architecture with separate models, schemas, and resolvers.
- [x] **Database Models**: Student, Exam, Question, Option, Attempt, Response.
- [x] **GraphQL Queries**: All getters for students, exams, questions, and attempts.
- [x] **GraphQL Mutations**: 
    - [x] `createStudent`, `updateStudent`, `deleteStudent`
    - [x] `createExam`
    - [x] `createQuestion`, `createOption`
    - [x] `startExam` (with timing & duplicate validation)
    - [x] `submitExam` (with auto-scoring and response logging)
- [x] **Business Logic**:
    - [x] Exam status validation (Upcoming, Ongoing, Completed).
    - [x] Duplicate attempt prevention.
    - [x] Automatic score calculation.
    - [x] Question-Option linkage and response recording.
- [x] **Developer Tools**: 
    - [x] Interactive **GraphiQL** interface at `/graphql`.
    - [x] `seed.py` for instant testing data.

---

## 📊 Database Models & Relationships

| Model | Fields | Description |
| :--- | :--- | :--- |
| **Student** | id, name, email, status | Individual candidates. |
| **Exam** | id, title, date, duration, status | Test metadata (Status: upcoming, ongoing, completed). |
| **Question** | id, exam_id, text, marks | Questions belonging to specific exams. |
| **Option** | id, question_id, text, is_correct | Multiple choice options for each question. |
| **Attempt** | id, student_id, exam_id, score, status | Student's session (Status: started, submitted). |
| **Response** | id, attempt_id, question_id, selected_option_id | Individual answers picked by students. |

### Relationships:
*   **One Exam** → Many Questions → Many Options.
*   **One Student** → Many Attempts.
*   **One Attempt** → Many Responses.

---

## 🛠️ GraphQL API Reference

### 1. Queries (Data Retrieval)

**Get All Exams**
```graphql
query {
  getExams {
    id
    title
    status
    questions {
      edges {
        node {
          text
          options {
            edges {
              node { id text }
            }
          }
        }
      }
    }
  }
}
```

**Get Student Attempts**
```graphql
query {
  getAttemptsByStudent(studentId: 1) {
    exam { title }
    score
    status
  }
}
```

### 2. Mutations (Data Modification)

**Start an Exam**
*Logic: Prevents multiple attempts and checks if the exam is 'ongoing'.*
```graphql
mutation {
  startExam(input: { studentId: 1, examId: 1 }) {
    attempt {
      id
      status
    }
  }
}
```

**Submit an Exam**
*Logic: Records all responses and calculates the final score automatically.*
```graphql
mutation {
  submitExam(
    studentId: 1, 
    examId: 1, 
    answers: [
      { questionId: "1", optionId: "2" }
    ]
  ) {
    attempt {
      status
      score
    }
  }
}
```

**Management Mutations**
```graphql
mutation {
  createStudent(name: "John Doe", email: "john@itm.edu") {
    student { id name }
  }
  
  createQuestion(examId: 1, text: "What is Python?", marks: 5) {
    question { id }
  }
}
```

---

## ⚙️ How to Run

### 1. Installation
```bash
# Navigate to project
cd exam_system

# Create & activate environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Setting Up Data
Populate the database with initial test data (1 student, 1 ongoing exam, 1 question):
```bash
python seed.py
```

### 3. Start the Server
```bash
python app.py
```

### 4. Interactive Testing
Open your browser to: **[http://127.0.0.1:5000/graphql](http://127.0.0.1:5000/graphql)**
This opens the built-in **GraphiQL** editor where you can run any of the queries above!

---

## 📁 Project Structure
```text
exam_system/
├── app.py              # Application entry point & routes
├── database.py         # SQLAlchemy configuration
├── config.py           # Database URL & secret keys
├── seed.py             # Testing data script
├── models/             # Database model definitions
├── schema/             # GraphQL ObjectTypes & Root Schema
└── resolvers/          # Core Business Logic
```
