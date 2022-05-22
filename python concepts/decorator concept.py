def response_to_mailman(func):
    def wrapper(*args,**kwargs):
        print("A Mailman is coming")
        response = func(*args,**kwargs)
        return response

    return wrapper

@response_to_mailman
def conjure_sound(sound):
    return sound*2


return_value = conjure_sound("woof")

print(return_value)