import random


def random_exercise(difficulty_level):
    if difficulty_level == 0:
        operando_1 = random.randrange(1, 10)
        operando_2 = random.randrange(1, 10)
        operador = random.choice(['+', '-', '*'])
        exercise_list = [
            operando_1,
            operando_2,
            operador
        ]

    if difficulty_level == 1:
        operando_1 = random.randrange(1, 100)
        operando_2 = random.randrange(1, 100)
        operador = random.choice(['+', '-', '*'])
        exercise_list = [
            operando_1,
            operando_2,
            operador
        ]

    if difficulty_level == 2:
        operando_1 = random.randrange(10, 100)
        operando_2 = random.randrange(10, 100)
        operador = random.choice(['+', '-', '*', '/'])
        exercise_list = [
            operando_1,
            operando_2,
            operador
        ]

    if difficulty_level == 3:
        operando_1 = random.randrange(10, 1000)
        operando_2 = random.randrange(10, 1000)
        operador = random.choice(['+', '-', '*', '/'])
        exercise_list = [
            operando_1,
            operando_2,
            operador
        ]

    if difficulty_level == 4:
        operando_1 = random.randrange(100, 1000)
        operando_2 = random.randrange(100, 1000)
        operador = random.choice(['+', '-', '*', '/'])
        exercise_list = [
            operando_1,
            operando_2,
            operador
        ]

    if difficulty_level == 5:
        operando_1 = random.randrange(1000, 10000)
        operando_2 = random.randrange(1000, 10000)
        operador = random.choice(['+', '-', '*', '/'])
        exercise_list = [
            operando_1,
            operando_2,
            operador
        ]
    # all other levels
    return exercise_list


