from pprint import pprint


class CarCollector:
    car_list = [
        {"id": 1, "price": 10000},
        {"id": 2, "price": 20000},
        {"id": 3, "price": 30000},
    ]
    car_dict = {
        1: "Ford",
        2: "Mazda",
        3: "Chevy"
    }

    @staticmethod
    def get_data():
        return list(map(CarCollector._combine, CarCollector.car_list))

    @staticmethod
    def _combine(cars):
        get_make = CarCollector.car_dict[cars["id"]]
        return {"id": cars["id"], "make": get_make, "price": cars["price"]}


pprint(CarCollector.get_data())
