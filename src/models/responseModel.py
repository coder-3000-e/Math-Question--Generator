from pydantic import BaseModel

class MathProblemResponse(BaseModel):
    problem: str
    solution: str