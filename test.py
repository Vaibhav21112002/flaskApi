# Draft7Validator
from jsonschema import Draft7Validator
from json import load

with open('schema.json') as f:
    schema = load(f)


def validates(list_):
    validator = Draft7Validator(schema)
    return list(validator.iter_errors(list_))


# list_ = {"name": "Rishabh Gupta",
#          "branch": "COE",
#          "college": "Delhi Technological University",
#          "roll": "2K20/EE/254"}

# validator = Draft7Validator(schema)
# l = list(validator.iter_errors(list_))
# # print(list(validator.iter_errors(list_)))
# if(len(l)):
#     print(l[0].message)
# else:
#     print("NO")
