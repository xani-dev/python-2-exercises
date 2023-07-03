class TaxMan:

    def __init__(self, list_of_items, percent):
        self.list_of_items = list_of_items
        self.__percent = percent

    def calc_total(self):
        prices = list(map(lambda i: i['price'], self.list_of_items))
        tax_to_int = int(self.__percent.replace('%', ''))
        tax = tax_to_int/100
        total = sum(prices)
        return (tax*total)+total


items = [
    {"id": 1, "desc": "clock", "price": 1.00},
    {"id": 2, "desc": "socks", "price": 2.00},
    {"id": 3, "desc": "razor", "price": 3.00},
]

tm = TaxMan(items, '10%')
print(tm.calc_total())
