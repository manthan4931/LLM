def calculator(expression:str):
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"
    