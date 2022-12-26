# from functions import sort1, sort2
# import pytest
# from behave import When, Given, Then
# from pytest_bdd import scenario, given, when, then


# @Scenario('C:\\Users\\alikn\\Desktop\\python\\BKIT\\BKIT_2022\\code\\lab5_code\\BDD\\features\\f1.feature',
#           'Требуется отсортировать массив чисел по модулю в порядке убывания без использованием лямбда функции')
# def testing_sort1():
#     pass
#
#
# @scenario('C:\\Users\\alikn\\Desktop\\python\\BKIT\\BKIT_2022\\code\\lab5_code\\BDD\\features\\f2.feature',
#           'Требуется отсортировать массив чисел по модулю в порядке убывания с использованием лямбда функции')
# def testing_sort2():
#     pass

#
# @Given('массив чисел', target_fixture='data')
# def data():
#     return [4, -30, 100, -100, 123, 1, 0, -1, -4]
#
#
# @When('массив чисел сортируется в функции sort1', target_fixture='sorted_data')
# def sorted_data(arg):
#     return sort1(arg)
#
#
# @Then('массив чисел отсортирован')
# def sorted_data(arg):
#     assert arg == [123, 100, -100, -30, 4, -4, 1, -1, 0]
#
# #
# # @When('массив чисел сортируется в функции sort2', target_fixture='sorted_data')
# # def sorted_data(arg):
# #     return sort2(arg)

from behave import Given, When, Then
from functions import get_roots


@Given("equation with coef A {A} B {B} C {C}")
def given_increment(context, A: str, B: str, C: str):
    context.A = int(A)
    context.B = int(B)
    context.C = int(C)


@When("we calculate roots")
def given_increment(context):
    context.results = get_roots(context.A, context.B, context.C)


@Then("we should see root1 {root1} root2 {root2} root3 {root3} root4 {root4}")
def then_results(context, root1: str, root2: str, root3: str, root4: str):
    if root1 == "empty":
        assert context.results == []
    elif root2 == "empty":
        assert context.results == [float(root1)]
    elif root3 == "empty":
        assert context.results == [float(root1), float(root2)]
    elif root4 == "empty":
        assert context.results == [float(root1), float(root2), float(root3)]
    else:
        assert context.results == [float(root1), float(root2), float(root3), float(root4)]
