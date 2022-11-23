from pprint import pprint


combinations = []
chars = ['A', 'B', 'C']
places_count = 5


def point_a(place_count, char_mas, answer=None):
	if answer is None:
		answer = []

	if place_count > 0:
		answer.append('A')

		point_a(place_count - 1, char_mas, answer.copy())
		point_b(place_count - 1, char_mas, answer.copy())
		point_c(place_count - 1, char_mas, answer.copy())

	else:
		answer.append('A')
		combinations.append(answer.copy())


def point_b(place_count, char_mas, answer=None):
	if answer is None:
		answer = []

	if place_count > 0:
		answer.append('B')

		point_a(place_count - 1, char_mas, answer.copy())
		point_b(place_count - 1, char_mas, answer.copy())
		point_c(place_count - 1, char_mas, answer.copy())

	else:
		answer.append('B')
		combinations.append(answer.copy())


def point_c(place_count, char_mas, answer=None):
	if answer is None:
		answer = []

	if place_count > 0:
		answer.append('C')

		point_a(place_count - 1, char_mas, answer.copy())
		point_b(place_count - 1, char_mas, answer.copy())
		point_c(place_count - 1, char_mas, answer.copy())

	else:
		answer.append('C')
		combinations.append(answer.copy())


		point_a(places_count, chars)
		point_b(places_count, chars)
		point_c(places_count, chars)

pprint(combinations)
pprint(len(combinations))