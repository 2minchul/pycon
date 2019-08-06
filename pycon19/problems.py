import json
import os


problem_set = []


if 'SOLUTION' in os.environ:
    with open(os.environ['SOLUTION'], 'r') as fp:
        problem_set.extend(json.load(fp))
