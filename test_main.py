from main import *


def test_linear_search():
	""" done. """
	assert linear_search([1, 2, 3, 4, 5], 5) == 4
	assert linear_search([1, 2, 3, 4, 5], 1) == 0
	assert linear_search([1, 2, 3, 4, 5], 6) == -1


def test_binary_search():
	assert binary_search([1, 2, 3, 4, 5], 5) == 4
	assert binary_search([1, 2, 3, 4, 5], 1) == 0
	assert binary_search([1, 2, 3, 4, 5], 6) == -1
	assert binary_search([6, 7, 9, 1, 2, 5], 7) == 1
	assert binary_search([9, 2, 5, 6, 8, 3, 1], 6) == 3

	###


def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1
