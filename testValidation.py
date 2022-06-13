# Draft7Validator
from jsonschema import Draft7Validator
from json import load

with open('schema.json') as f:
    schema = load(f)


def validates(list_):
    validator = Draft7Validator(schema)
    return list(validator.iter_errors(list_))
