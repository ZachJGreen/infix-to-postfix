from pytest import *
import infix_convert as ic

expression1 = "3 + 2 / 4"
expression2 = "()"
expression3 = "(]"
operator = "+"
operand = "3"

def test_bracket():
    assert ic.check_parentheses(expression1) == True
    assert ic.check_parentheses(expression2) == True
    assert ic.check_parentheses(expression3) == False

def test_operand():
    assert ic.is_operand(operand) == True
    assert ic.is_operand(operator) == False

def test_operator():
    assert ic.operator_check(operand) == False
    assert ic.operator_check(operator) == True

