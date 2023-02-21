import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

# Customer instances
customer1 = fc.Customer(570, 'Danni Sellyar', '97 Mitchell Way Hewitt Texas 76712', 'dsellyarft@gmpg.org', '254-555-9362', False)
customer2 = fc.Customer(569, 'Aubree Himsworth', '1172 Moulton Hill Waco Texas 76710', 'ahimsworthfs@list-manage.com', '254-555-2273', True)

# Transaction instances
trans1 = fc.Transaction('2/15/2023', 'The Lone Patty', 17, 569)
trans2 = fc.Transaction('2/15/2023', 'The Octobreakfast', 18, 569)
trans3 = fc.Transaction('2/15/2023', 'The Octoveg', 16, 570)
trans4 = fc.Transaction('2/15/2023', 'The Octoburger', 20, 570)

# function for printing details

def print_report(customer):
   
   order_total = 0
   discount = 0
   final = 0
   
   for trans in [trans1, trans2, trans3, trans4]:
       if trans.get_customerid() == customer.get_customerid():
           order_total += trans.get_cost()
       elif trans.get_customerid() == customer.get_customerid():
           order_total += trans.get_cost()
                  
   print(f"Customer Name: {customer.get_name()}")
   print(f"Phone: {customer.get_phone()}")

   for trans in [trans1, trans2, trans3, trans4]:
       if trans.get_customerid() == customer.get_customerid():
           print(f"Order Item: {trans.get_item_name()}  Price: ${trans.get_cost():.2f}")  
   print(f"Total Cost: ${order_total:.2f}")
   
   # checking for member_status and discount

   discount_applied = False       # boolean var to print 'discount' only for members
   for trans in [trans1, trans2, trans3, trans4]:
    if customer.get_status() and not discount_applied:
        discount = order_total * .2
        final = order_total - discount
        discount_applied = True
   
   if discount_applied:
    print(f"Member Discount: ${discount:.2f}")
    print(f"Total Cost after discount: ${final:.2f}")        

print_report(customer1) 
#print_report(customer2)
