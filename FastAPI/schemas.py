
from pydantic import BaseModel, ConfigDict


# Used when the client creates a course
class CourseCreate(BaseModel):
    title: str
    description: str


# Used when the API returns a course
class CourseResponse(BaseModel):
    id: int
    title: str
    description: str

    model_config = ConfigDict(from_attributes=True)
