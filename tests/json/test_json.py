import json
import os

from gramat.actions import compile_file, tokenize


def test_json():
    cwd = os.path.dirname(__file__)
    grammar_file = os.path.join(cwd, 'json.gmt')
    actual_file = os.path.join(cwd, 'case_1.actual.json')
    expected_file = os.path.join(cwd, 'case_1.expected.json')

    grammar = compile_file(grammar_file)
    expression = grammar.get_rule('value')
    nodes = tokenize(expression, actual_file)
    actual = [node.to_dict() for node in nodes]

    with open(expected_file) as r:
        expected = json.load(r)

    assert actual == expected
