from random import random


def create_rand_list(len_list: int) -> list:
    rand_list = [int(random()*100) for _ in range(len_list)]
    return  rand_list


def counter(random_list: list) -> set:
    print(random_list)
    count_lst = [random_list.count(x) for x in random_list]
    print(count_lst)
    lst_set = set([(random_list[count_lst.index(i)], i) for i in count_lst if i > 1])
    return lst_set

#print(create_rand_list(10))
print(counter(create_rand_list(10)))

