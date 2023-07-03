from dataclasses import dataclass
from pprint import pprint

@dataclass(frozen=False, order=True)
class Invoice():
    invoice_id: int
    user_id: str
    amount: float
    paid: bool 
    



def get_invoices(invoice_data):
    
    
    # working_list = list(map(lambda invoices:
    #                     **invoices, 'invoice_id': invoices[0], 'user_id': invoices[1], 'amount': invoices[2], 'paid': [3]}, invoice_data))
    # print(working_list)
    
    working_list = list(map(lambda i:i, invoice_data))
    print(working_list)
    
    invoice = [Invoice(working_list[0], working_list[1], working_list[3], working_list[4])]
    print(invoice)





data = [
    "1, 2322, 10.00, False",
    "2, 5435, 60.30, True",
    "3, 3433, 15.63, False",
    "4, 8439, 12.77, False",
    "5, 3424, 11.34, False",
]

get_invoices(data)