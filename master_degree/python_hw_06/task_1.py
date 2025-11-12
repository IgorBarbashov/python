from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from enum import StrEnum


class Operator(StrEnum):
    PLUS = '+'
    MINUS = '-'
    MULTIPLY = '*'
    DIVIDE = "/"


def validate_operation(a: float, op: Operator, b: float):
    if op not in Operator:
        raise HTTPException(status_code=400, detail="Unsupported operation")
    if op == Operator.DIVIDE and b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")


def eval_operation(a: float, op: Operator, b: float) -> float:
    if (op == Operator.PLUS):
        return a + b
    elif (op == Operator.MINUS):
        return a - b
    elif (op == Operator.MULTIPLY):
        return a * b
    elif (op == Operator.DIVIDE):
        return a / b


def eval_expression(expression: str) -> float:
    try:
        return eval(expression)
    except:
        raise HTTPException(
            status_code=400, detail="Expression can't been evaluated")


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def root():
    html_content = "<p>Вычислить одну операцию: <code>/calculate/operate/{a}/{op}/{b}</code></p>" \
        "<p>Вычислить выражение: <code>/calculate/expression/{expression}</code></p>"\
        "<p><a href='/docs' target='_self'>Документация</a></p>"
    return html_content


@app.get("/calculate/operate/{a}/{op}/{b}")
def calculate_operation(a: float, op: str, b: float) -> float:
    validate_operation(a, op, b)
    return eval_operation(a, op, b)


@app.get("/calculate/expression/{expression}")
def calculate_operation(expression: str) -> float:
    return eval_expression(expression)
