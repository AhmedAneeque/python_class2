import random
from customers import *
from Products import *
from payments import *
from delivery import *


# def order_details():
#     order_id="ord"+str(random.randint(10001,19999))
#     p_list=Products.getproducts_data()
#     c_list=customers.get_customer_data()
#     print("choose from the list of products")
    
def generate_order():
    order_id="ORD"+str(random.randint(1000,9999))
    print(order_id)
    # print(get_product_data())
     
    
    for a in get_customer_data():
        print(list(a.values()))
    my_customer_id=int(input("enter the customer id:"))
    for a in get_customer_data():
        if my_customer_id==list(a.values())[0]:
            print(list(a.values()))
            break
    else:
        print("customer not found")
        print("Register the customer")
        register_customers()


    for x in get_product_data():
        print(list(x.values()))
    myproduct_id=int(input("enter the product id:"))
    for x in get_product_data():
        if myproduct_id==list(x.values())[0]:
            print(list(x.values()))
            myqty=int(input("Enter Qty:"))
            if myqty>list(x.values())[3]:
                print("Out of Stock")
                break
            else:
                order_amount=myqty*list(x.values())[2]
                print("Product Name:",list(x.values())[1])
                print("Order Qty:",myqty)
                print("Price:",list(x.values())[2])
                s=payment_methods()
                d=delivery_charges()
                print("Total Amount:",(order_amount+s+d))
            break
    else:
        print("Product not Found!")
        

generate_order()


