
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import mathgenerator

from src.helpers.helpers import remove_dollar_sign
from src.models.responseModel import MathProblemResponse

app = FastAPI(docs_url="/api/docs")

@app.get('/basic_algebra', response_model=MathProblemResponse)
def generate_math_problem_basic_algebra() -> MathProblemResponse:
    problem, solution = mathgenerator.basic_algebra()

    problem = remove_dollar_sign(problem)
    solution = remove_dollar_sign(solution)

    return MathProblemResponse(problem=problem, solution=solution)

@app.get('/addition', response_model=MathProblemResponse)
def generate_math_problem_addition() -> MathProblemResponse:
    problem, solution = mathgenerator.addition()

    problem = remove_dollar_sign(problem)
    solution = remove_dollar_sign(solution)

    return MathProblemResponse(problem=problem, solution=solution)

@app.get('/absolute_difference', response_model=MathProblemResponse)
def generate_math_problem_absolute_difference() -> MathProblemResponse:
    problem, solution = mathgenerator.absolute_difference()

    problem = remove_dollar_sign(problem)
    solution = remove_dollar_sign(solution)

    return MathProblemResponse(problem=problem, solution=solution)

@app.get('/angle_btw_vectors', response_model=MathProblemResponse)
def generate_math_problem_angle_btw_vectors() -> MathProblemResponse:
    problem, solution = mathgenerator.angle_btw_vectors()

    problem = remove_dollar_sign(problem)
    solution = remove_dollar_sign(solution)

    return MathProblemResponse(problem=problem, solution=solution)

@app.get('/angle_regular_polygon', response_model=MathProblemResponse)
def generate_math_problem_angle_regular_polygon() -> MathProblemResponse:
    problem, solution = mathgenerator.angle_regular_polygon()

    problem = remove_dollar_sign(problem)
    solution = remove_dollar_sign(solution)

    return MathProblemResponse(problem=problem, solution=solution)

@app.get('/arc_length', response_model=MathProblemResponse)
def generate_math_problem_arc_length() -> MathProblemResponse:
    problem, solution = mathgenerator.arc_length()

    problem = remove_dollar_sign(problem)
    solution = remove_dollar_sign(solution)

    return MathProblemResponse(problem=problem, solution=solution)

@app.get('/area_of_circle', response_model=MathProblemResponse)
def generate_math_problem_area_of_circle() -> MathProblemResponse:
    problem, solution = mathgenerator.area_of_circle()

    problem = remove_dollar_sign(problem)
    solution = remove_dollar_sign(solution)

    return MathProblemResponse(problem=problem, solution=solution)

@app.get('/area_of_circle_given_center_and_point', response_model=MathProblemResponse)
def generate_math_problem_area_of_circle_given_center_and_point() -> MathProblemResponse:
    problem, solution = mathgenerator.area_of_circle_given_center_and_point()

    problem = remove_dollar_sign(problem)
    solution = remove_dollar_sign(solution)

    return MathProblemResponse(problem=problem, solution=solution)

@app.get('/area_of_triangle', response_model=MathProblemResponse)
def generate_math_problem_area_of_triangle() -> MathProblemResponse:
    problem, solution = mathgenerator.area_of_triangle()

    problem = remove_dollar_sign(problem)
    solution = remove_dollar_sign(solution)

    return MathProblemResponse(problem=problem, solution=solution)

@app.get('/arithmetic_progression_sum', response_model=MathProblemResponse)
def generate_math_problem_arithmetic_progression_sum() -> MathProblemResponse:
    problem, solution = mathgenerator.arithmetic_progression_sum()

    problem = remove_dollar_sign(problem)
    solution = remove_dollar_sign(solution)

    return MathProblemResponse(problem=problem, solution=solution)

@app.get('/arithmetic_progression_term', response_model=MathProblemResponse)
def generate_math_problem_arithmetic_progression_term() -> MathProblemResponse:
    problem, solution = mathgenerator.arithmetic_progression_term()

    problem = remove_dollar_sign(problem)
    solution = remove_dollar_sign(solution)

    return MathProblemResponse(problem=problem, solution=solution)

@app.get('/base_conversion', response_model=MathProblemResponse)
def generate_math_problem_base_conversion() -> MathProblemResponse:
    problem, solution = mathgenerator.base_conversion()

    problem = remove_dollar_sign(problem)
    solution = remove_dollar_sign(solution)

    return MathProblemResponse(problem=problem, solution=solution)

@app.get('/online')
def healthy() -> str:
    return "online"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)