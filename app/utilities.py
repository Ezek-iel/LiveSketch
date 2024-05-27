from uuid import uuid4
def strip_errors(errors : dict):
    error_values = list(errors.values())
    total_list = []
    for value in error_values:
        value_text = "".join(value)
        total_list.append(value_text)
    return total_list

def generate_random_uuid():
    return str(uuid4())