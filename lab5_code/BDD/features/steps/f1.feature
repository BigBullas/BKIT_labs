#Feature: Sorting elements by abs with function sorted
#  Scenario: Data need to be sorted by abs with function sorted
#  Given some data
#  When data get sorted with my_sort1
#  Then data is sorted


Feature: Testing the Equation
  Scenario: Test calculate 4 roots
    Given equation with coef A 1 B -10 C 9
    When we calculate roots
    Then we should see root1 -3.0 root2 -1.0 root3 1.0 root4 3.0

  Scenario: Test calculate 2 roots
    Given equation with coef A 1 B -2 C 1
    When we calculate roots
    Then we should see root1 -1.0 root2 1.0 root3 empty root4 empty

  Scenario: Test calculate 0 roots
    Given equation with coef A 1 B 2 C 3
    When we calculate roots
    Then we should see root1 empty root2 empty root3 empty root4 empty

#Feature: Сортировка чисел по модулю в порядке убывания без использования лямбда функции
#
#  Scenario: Требуется отсортировать массив чисел по модулю в порядке убывания без использованием лямбда функции
#    Given массив чисел
#    When массив чисел сортируется в функции sort1
#    Then массив чисел отсортирован