
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select

from database import get_db
from models import Course
from schemas import CourseCreate, CourseResponse

app = FastAPI()


# CREATE COURSE
@app.post(
    "/courses",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED
)
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    new_course = Course(
        title=course.title,
        description=course.description
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course


# GET ALL COURSES
@app.get("/courses", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):

    statement = select(Course)
    courses = db.scalars(statement).all()

    return courses


# GET COURSE BY ID
@app.get("/courses/{course_id}", response_model=CourseResponse)
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):

    statement = select(Course).where(Course.id == course_id)
    course = db.scalar(statement)

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course
