
def user_decorator(function_repository):
    def wrapper(*qrgs, **kwargs):
        returned_data = function_repository(*qrgs, **kwargs)
        del returned_data["_id"]
        return returned_data
    return wrapper