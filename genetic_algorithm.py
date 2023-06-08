import random

class Item:
	"""
	Класс, представляющий предметы для размещения в рюкзаке.
	Каждый предмет имеет свою стоимость (`value`) и вес (`weight`).
	"""
	def __init__(self, weight, value):
		self.weight = weight
		self.value = value

class Chromosome:
	"""
	Класс, представляющий хромосому в генетическом алгоритме.
	Хромосома состоит из набора генов (`genes`), каждый из которых соответствует предмету для размещения в рюкзаке.
	Каждый ген принимает значение 0 или 1, где 1 означает выбор предмета, а 0 - его отсутствие.
	Хромосома также хранит ссылку на список предметов (items) и максимальный вес рюкзака (`max_weight`).
	"""
	def __init__(self, genes, items, max_weight):
		self.genes = genes
		self.items = items
		self.max_weight = max_weight
		self._fitness = None

	@property
	def fitness(self):
		"""
		Свойство, возвращающее приспособленность хромосомы.
		Если значение приспособленности не было вычислено ранее, то оно будет вычислено с помощью метода `_calculate_fitness()`.
		"""
		if self._fitness is None:
			self._calculate_fitness()
		return self._fitness

	def _calculate_fitness(self):
		"""
        Метод для вычисления приспособленности хромосомы.
        Приспособленность определяется суммой стоимостей выбранных предметов.
        Если общий вес выбранных предметов превышает максимальный вес рюкзака, приспособленность равна 0.
        """
		total_value = 0
		total_weight = 0
		for i in range(len(self.genes)):
			if self.genes[i] == 1:
				total_value += self.items[i].value
				total_weight += self.items[i].weight
		if total_weight > self.max_weight:
			self._fitness = 0
		else:
			self._fitness = total_value

def create_initial_population(population_size, chromosome_length, items, max_weight):
	"""
    Функция для создания начальной популяции хромосом.
    Принимает параметры:
    - `population_size`: размер популяции (количество хромосом в популяции)
    - `chromosome_length`: длина хромосомы (количество генов)
    - `items`: список предметов для размещения в рюкзаке
    - `max_weight`: максимальный вес рюкзака
    Возвращает список хромосом - начальную популяцию.
    """
	population = []
	for _ in range(population_size):
		genes = [random.randint(0, 1) for _ in range(chromosome_length)]
		chromosome = Chromosome(genes, items, max_weight)
		population.append(chromosome)
	return population

def get_best_chromosome(collection):
	"""
    Функция для нахождения самой приспособленной особи из коллекции.
    Принимает параметр:
    - `collection`: коллекция хромосом
    \nДля каждой хромосомы в популяции вызывается свойства `fitness` для вычисления приспособленности.
    Возвращает лучший результат приспособленности из популяции.
    """
	max_ = -1
	best_chromosome = None
	for chromosome in collection:
		if fitness := chromosome.fitness > max_:
			max_ = fitness
			best_chromosome = chromosome
			
	return best_chromosome

def create_offspring_population(population, tournament_size, mutation_rate):
	"""
    Функция для создания новой популяции потомков на основе родительских хромосом.
    Принимает параметры:
    - `population`: популяция родительских хромосом
    - `tournament_size`: размер турнира для отбора родительских хромосом
    - `mutation_rate`: вероятность мутации гена при создании потомка
    Возвращает новую популяцию потомков.
    """
	offspring_population = []
	while len(offspring_population) < len(population):
		parent1 = tournament_selection(population, tournament_size)
		parent2 = tournament_selection(population, tournament_size)
		offspring = crossover(parent1, parent2)
		offspring = mutate(offspring, mutation_rate)
		offspring_population.append(offspring)
	return offspring_population

def tournament_selection(population, tournament_size):
	"""
    Функция для отбора родительской хромосомы с помощью турнирной селекции.
    Принимает параметры:
    - `population`: популяция хромосом
    - `tournament_size`: размер турнира (количество хромосом, участвующих в турнире)
    Возвращает лучшую хромосому из турнира (с наибольшей приспособленностью).
    """
	tournament = random.sample(population, tournament_size)
	best_chromosome =  get_best_chromosome(tournament)

	return best_chromosome

def crossover(parent1, parent2):
	"""
    Функция для скрещивания двух родительских хромосом и создания потомка.
    Принимает две родительские хромосомы.
    Возвращает новую хромосому - потомка.
    """
	crossover_point = random.randint(1, len(parent1.genes) - 1)
	child_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
	return Chromosome(child_genes, parent1.items, parent1.max_weight)

def mutate(chromosome, mutation_rate):
	"""
    Функция для мутации генов хромосомы.
    Принимает хромосому и вероятность мутации гена.
    Возвращает хромосому с мутировавшими генами.
    """
	mutated_genes = []
	for gene in chromosome.genes:
		if random.random() < mutation_rate:
			mutated_genes.append(1 - gene)  # Сменить бит
		else:
			mutated_genes.append(gene)
	return Chromosome(mutated_genes, chromosome.items, chromosome.max_weight)

if __name__ == '__main__':
	# Задание предметов
	# items = [
	# 	Item(10,15),
	# 	Item(6,10),
	# 	Item(11,22),
	# 	Item(4,7),
	# 	Item(1,1),
	# 	Item(4,9),
	# 	Item(3,4),
	# ]
	# Пример из лекции. Ответ: [1,0,0,1,1] | Ст-ть: 25 | Вес: 11/11
	# items = [
	# 	Item(2,6),
	# 	Item(3,7),
	# 	Item(6,8),
	# 	Item(4,9),
	# 	Item(5,10),
	# ]
	items = [
		Item(3,6),
		Item(4,2),
		Item(10,1),
		Item(11,7),
		Item(3,3),
		Item(1,4),
		Item(5,7),
	]
	
	# Задание максимального веса рюкзака
	max_weight = 10

	# Определение параметров генетического алгоритма
	population_size = 1000
	chromosome_length = len(items)
	tournament_size = 5
	mutation_rate = 0.05
	max_generations = 1000

	# Создание начальной популяции
	population = create_initial_population(population_size, chromosome_length, items, max_weight)

	# Главный цикл генетического алгоритма
	for generation in range(max_generations):
		# Нахождение самой приспособленной особи популяции
		best_chromosome = get_best_chromosome(population)

		# Проверка условия завершения
		if best_chromosome.fitness == sum(item.value for item in items):
			break

		# Формирование новой популяции
		population = create_offspring_population(population, tournament_size, mutation_rate)

	# Вывод результатов
	best_chromosome = max(population, key=lambda x: x.fitness)
	print("Лучшая хромосома:", best_chromosome.genes)
	print("Максимальная стоимость:", best_chromosome.fitness)

	total_weight = 0
	for i in range(chromosome_length):
		if best_chromosome.genes[i] == 1:
			total_weight += items[i].weight
	print(f"Занято места: {total_weight}/{max_weight}")
