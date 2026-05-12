"""
Wordy - Natural Language Calculator
"""
OPERATIONS: list[str] = [
    "plus",
    "minus",
    "multiplied",
    "divided"
]


def answer(question: str) -> int:
    """
    Answers a natural language math question

    :param str question: Math question
    :return int: answer
    """
    try:
        answer: int | None = None
        operation: str | None = None
        math_question_part: int
        if not question.startswith("What is ") or not question.endswith("?"):
            raise ValueError("syntax error")
        math_question: list[str] = question[8:-1].split()
        while math_question:
            if answer is None:
                answer = int(math_question.pop(0))
            if math_question:
                operation = math_question.pop(0)
                if operation not in OPERATIONS:
                    if operation.isdigit():
                        raise ValueError("syntax error")
                    raise ValueError("unknown operation")
                if operation in OPERATIONS[2:]:
                    math_question.pop(0)
                if not math_question:
                    raise ValueError("syntax error")
                math_question_part = int(math_question.pop(0))
                if operation == OPERATIONS[0]:
                    answer += math_question_part
                elif operation == OPERATIONS[1]:
                    answer -= math_question_part
                elif operation == OPERATIONS[2]:
                    answer *= math_question_part
                else:
                    if math_question_part == 0:
                        raise ValueError("syntax error")
                    answer //= math_question_part  
        if answer is None:
            raise ValueError("syntax error")
    except ValueError as exception:
        if str(exception) == "unknown operation":
            raise
        raise ValueError("syntax error") from exception
    return answer