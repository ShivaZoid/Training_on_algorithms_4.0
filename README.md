# Решение задач

## 1) Разминка

* #### A. Не минимум на отрезке
	<details>
    <summary>Описание</summary>

    | Ограничение времени | 1 секунда |
    |---------------------|------------|
    | Ограничение памяти  | 64Mb       |
    | Ввод                | стандартный ввод или input.txt |
    | Вывод               | стандартный вывод или output.txt |

    Задана последовательность целых чисел a1, a2, …, an. Задаются запросы: сказать любой элемент последовательности на отрезке от L до R включительно, не равный минимуму на этом отрезке.

    ### Формат ввода

	В первой строке содержатся два целых числа N, 1 ≤ N ≤ 100 и M, 1 ≤ M ≤ 1000 — длина последовательности и количество запросов соответственно.
	Во второй строке — сама последовательность, 0 ≤ ai ≤ 1000.
Начиная с третьей строки перечисляются M запросов, состоящих из границ отрезка L и R, где L, R - индексы массива, нумеруются с нуля.

	### Формат вывода
    На каждый запрос выведите в отдельной строке ответ — любой элемент на [L, R], кроме минимального. В случае, если такого элемента нет, выведите "NOT FOUND".

    ### Пример 1

    | Ввод | Вывод |
    |------|-------|
    | 10 5 | NOT FOUND |
    | 1 1 1 2 2 2 3 3 3 10 | 2 |
    | 0 1 | NOT FOUND |
    | 0 3 | 10 |
    | 3 4 | 3 |
    | 7 9 | |
    | 3 7 | |

    ### Пример 2

    | Ввод | Вывод |
    |------|-------|
    | 4 2 | NOT FOUND |
    | 1 1 1 2 | 2 |
    | 0 2 | |
    | 0 3 | |

    ## [__Решение__](https://github.com/ShivaZoid/Training_on_algorithms_4.0/blob/main/Warm-up/A.py)

## 2) Занятие 1 (Сортировки: быстрая, слиянием и поразрядная)

* #### A. Partition
	<details>
    <summary>Описание</summary>

    | Ограничение времени | 2 секунда |
    |---------------------|------------|
    | Ограничение памяти  | 256Mb       |
    | Ввод                | стандартный ввод или input.txt |
    | Вывод               | стандартный вывод или output.txt |

    Базовым алгоритмом для быстрой сортировки является алгоритм partition, который разбивает набор элементов на две части относительно заданного предиката.

	По сути элементы массива просто меняются местами так, что левее некоторой точки в нем после этой операции лежат элементы, удовлетворяющие заданному предикату, а справа — не удовлетворяющие ему.

	Например, при сортировке можно использовать предикат «меньше опорного», что при оптимальном выборе опорного элемента может разбить массив на две примерно равные части.

	Напишите алгоритм partition в качестве первого шага для написания быстрой сортировки.

    ### Формат ввода

	В первой строке входного файла содержится число N — количество элементов массива (0 ≤ N ≤ 106).

	Во второй строке содержатся N целых чисел ai, разделенных пробелами (-109 ≤ ai ≤ 109).

	В третьей строке содержится опорный элемент x (-109 ≤ x ≤ 109).

	Заметьте, что x не обязательно встречается среди ai.

	### Формат вывода
    Выведите результат работы вашего алгоритма при использовании предиката «меньше x»: в первой строке выведите число элементов массива, меньших x, а во второй — количество всех остальных.

    ### Пример 1

    | Ввод | Вывод |
    |------|-------|
    | 5 | 2 |
    | 1 9 4 2 3 | 3 |
    | 3 | |

    ### Пример 2

    | Ввод | Вывод |
    |------|-------|
    | 0 | 0 |
    | | 0 |
    | 0 | |

    ### Пример 3

    | Ввод | Вывод |
    |------|-------|
    | 1 | 0 |
    | 0 | 1 |
    | 0 | |

    ### Примечания

    Чтобы решить советуем реализовать функцию, которая принимает на вход предикат и пару итераторов, задающих массив (или массив и два индекса в нём), а возвращает точку разбиения, то есть итератор (индекс) на конец части, которая содержащит элементы, удовлетворяющие заданному предикату.

	В таком виде вам будет удобно использовать эту функцию для реализации сортировки.

    ## [__Решение__]()

* #### B. Быстрая сортировка
	<details>
    <summary>Описание</summary>

    | Ограничение времени | 10 секунда |
    |---------------------|------------|
    | Ограничение памяти  | 512Mb       |
    | Ввод                | стандартный ввод или input.txt |
    | Вывод               | стандартный вывод или output.txt |

    Реализуйте быструю сортировку, используя алгоритм из предыдущей задачи.

	На каждом шаге выбирайте опорный элемент и выполняйте partition относительно него.

    Затем рекурсивно запуститесь от двух частей, на которые разбился исходный массив.

    ### Формат ввода

	В первой строке входного файла содержится число N — количество элементов массива (0 ≤ N ≤ 106).

	Во второй строке содержатся N целых чисел ai, разделенных пробелами (-109 ≤ ai ≤ 109).

	### Формат вывода
    Выведите результат сортировки, то есть N целых чисел, разделенных пробелами.

    ### Пример

    | Ввод | Вывод |
    |------|-------|
    | 5 | 1 2 3 4 5 |
    | 1 5 2 4 3 | |

    ### Примечания

    Используйте функцию, реализованную в предыдущей задаче.

    ## [__Решение (Частичное!)__]()

* #### C. Слияние
	<details>
    <summary>Описание</summary>

    | Ограничение времени | 5 секунда |
    |---------------------|------------|
    | Ограничение памяти  | 512Mb       |
    | Ввод                | стандартный ввод или input.txt |
    | Вывод               | стандартный вывод или output.txt |

    Базовый алгоритм для сортировки слиянием — алгоритм слияния двух упорядоченных массивов в один упорядоченный массив.
    Эта операция выполняется за линейное время с линейным потреблением памяти.
    Реализуйте слияние двух массивов в качестве первого шага для написания сортировки слиянием.

    ### Формат ввода

	В первой строке входного файла содержится число N — количество элементов первого массива (0 ≤ N ≤ 106).

	Во второй строке содержатся N целых чисел ai, разделенных пробелами, отсортированные по неубыванию (-109 ≤ ai ≤ 109).

	В третьей строке входного файла содержится число M — количество элементов второго массива (0 ≤ M ≤ 106).

	В третьей строке содежатся M целых чисел bi, разделенных пробелами, отсортированные по неубыванию (-109 ≤ bi ≤ 109).

	### Формат вывода
    Выведите результат слияния этих двух массивов, то есть M + N целых чисел, разделенных пробелами, в порядке неубывания.

    ### Пример 1

    | Ввод | Вывод |
    |------|-------|
    | 5 | 1 2 3 5 5 5 6 9 |
    | 1 3 5 5 9 | |
    | 3 | |
    | 256 | |

    ### Пример 2

    | Ввод | Вывод |
    |------|-------|
    | 1 | 0 |
    | 0 | |
    | 0 | |

    ### Пример 3

    | Ввод | Вывод |
    |------|-------|
    | 0 | 0 |
    |  |  |
    | 1 | |
    | 0 | |

    ### Примечания

    Для решения этой задачи советуем реализовать функцию, которая принимает на вход две пары итераторов, задающие два массива, и итератор на начало буфера, в который необходимо записывать результат. Итераторы можжно заменить на передачу массивов и индексов в них. В таком виде вам будет удобно использовать эту функцию для реализации сортировки.

    ## [__Решение (None)__]()

* #### D. Сортировка слиянием
	<details>
    <summary>Описание</summary>

    | Ограничение времени | 15 секунда |
    |---------------------|------------|
    | Ограничение памяти  | 512Mb       |
    | Ввод                | стандартный ввод или input.txt |
    | Вывод               | стандартный вывод или output.txt |

    Реализуйте сортировку слиянием, используя алгоритм из предыдущей задачи.

	На каждом шаге делите массив на две части, сортируйте их независимо и сливайте с помощью уже реализованной функции.

    ### Формат ввода

	В первой строке входного файла содержится число N — количество элементов массива (0 ≤ N ≤ 106).

	Во второй строке содержатся N целых чисел ai, разделенных пробелами (-109 ≤ ai ≤ 109).

	### Формат вывода

    Выведите результат сортировки, то есть N целых чисел, разделенных пробелами, в порядке неубывания.

    ### Пример

    | Ввод | Вывод |
    |------|-------|
    | 5 | 1 2 3 4 5 |
    | 1 5 2 4 3 | |

    ### Примечания

    Используйте функцию, реализованную в предыдущей задаче.

    ## [__Решение (None)__]()

* #### E. Поразрядная сортировка
	<details>
    <summary>Описание</summary>

    | Ограничение времени | 1 секунда |
    |---------------------|------------|
    | Ограничение памяти  | 64Mb       |
    | Ввод                | стандартный ввод или input.txt |
    | Вывод               | стандартный вывод или output.txt |

    Поразрядная сортировка является одним из видов сортировки, которые работают практически за линейное от размера сортируемого массива время. Такая скорость достигается за счет того, что эта сортировка использует внутреннюю структуру сортируемых объектов. Изначально этот алгоритм использовался для сортировки перфокарт. Первая его компьютерная реализация была создана в университете MIT Гарольдом Сьюардом (Harold Н. Seward). Опишем алгоритм подробнее. Пусть задан массив строк s1 , ..., si причём все строки имеют одинаковую длину m.

    Работа алгоритма состоит из m фаз. На i -ой фазе строки сортируются па i -ой с конца букве. Происходит это следующим образом. Будем, для простоты, в этой задаче рассматривать строки из цифр от 0 до 9. Для каждой цифры создается «корзина» («bucket»), после чего строки si распределяются по «корзинам» в соответствии с i-ой цифрой с конца. Строки, у которых i-ая с конца цифра равна j попадают в j-ую корзину (например, строка 123 на первой фазе попадет в третью корзину, на второй — во вторую, на третьей — в первую). После этого элементы извлекаются из корзин в порядке увеличения номера корзины. Таким образом, после первой фазы строки отсортированы по последней цифре, после двух фаз — по двум последним, ..., после m фаз — по всем. При важно, чтобы элементы в корзинах сохраняли тот же порядок, что и в исходном массиве (до начала этой фазы). Например, если массив до первой фазы имеет вид: 111, 112, 211, 311, то элементы по корзинам распределятся следующим образом: в первой корзине будет. 111, 211, 311, а второй: 112. Напишите программу, детально показывающую работу этого алгоритма на заданном массиве.

    ### Формат ввода

	Первая строка входного файла содержит целое число n (1 ≤ n ≤ 1000) . Последующие n строк содержат каждая по одной строке si . Длины всех si , одинаковы и не превосходят 20. Все si состоят только из цифр от 0 до 9.

	### Формат вывода

    В выходной файл выведите исходный массив строк в, состояние «корзин» после распределения элементов по ним для каждой фазы и отсортированный массив. Следуйте формату, приведенному в примере.

    ### Пример

    | Ввод | Вывод |
    |------|-------|
    | 9 | Initial array: |
    | 12 | 12, 32, 45, 67, 98, 29, 61, 35, 09 |
    | 32 | ********** |
    | 45 | Phase 1 |
    | 67 | Bucket 0: empty |
    | 98 | Bucket 1: 61 |
    | 29 | Bucket 2: 12, 32 |
    | 61 | Bucket 3: empty |
    | 35 | Bucket 4: empty |
    | 09 | Bucket 5: 45, 35 |
    |  | Bucket 6: empty|
    |  | Bucket 7: 67 |
    |  | Bucket 8: 98 |
    |  | Bucket 9: 29, 09 |
    |  | ********** |
    |  | Phase 2 |
    |  | Bucket 0: 09 |
    |  | Bucket 1: 12 |
    |  | Bucket 2: 29 |
    |  | Bucket 3: 32, 35 |
    |  | Bucket 4: 45 |
    |  | Bucket 5: empty |
    |  | Bucket 6: 61, 67 |
    |  | Bucket 7: empty |
    |  | Bucket 8: empty |
    |  | Bucket 9: 98 |
    |  | ********** |
    |  | Sorted array: |
    |  | 09, 12, 29, 32, 35, 45, 61, 67, 98 |

    ## [__Решение (None)__]()