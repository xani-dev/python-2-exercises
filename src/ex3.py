def calc_bmi(people_list):
    # Calculate BMI : BMI = round(weight / height ** 2, 1)
    bmi_list = list(map(lambda person_object: {**person_object, 'bmi': round(person_object['weight_kg'] /
                                                                             person_object['height_meters'] ** 2, 1)},
                        people_list))
    return bmi_list


people_list = [
    {'id': 2, 'name': 'bob', 'weight_kg': 90, 'height_meters': 1.7},
    {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
]

new_people_list = calc_bmi(people_list)
print(new_people_list)
