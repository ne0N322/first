import logging
logging.basicConfig(level=logging.ERROR)

print()
logging.error("error")
def checker(function):
    def checker2(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc :
            print(f"We have problems - {exc}")
            logging.error("Код не может обработать запрос изза неизвестного символа." )
        else:
            print(f"No problems. Result – {result}")
    return checker2

# @checker
def calculate(expression):
    return eval(expression)

calculate = checker(calculate)    # decoration before
res = calculate("2+2")
print(res) #
