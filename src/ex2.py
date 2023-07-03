def filter_males(list_name):
    filtered = list(filter(lambda p: p['sex'] == 'female', list_name))
    print(filtered)


people_list = [
    {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
    {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]

filter_males(people_list)
