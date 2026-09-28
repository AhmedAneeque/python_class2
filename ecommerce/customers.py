# read customers data
customers_list=[{"cust_id":1001,"cust_name":"Aneeque","city":"Malegaon"},
                {"cust_id":1002,"cust_name":"Saadan","city":"Malegaon"},
                {"cust_id":1003,"cust_name":"Sarim","city":"Malegaon"},
                {"cust_id":1004,"cust_name":"Adeem","city":"Malegaon"}]

def register_customers():
    cust_id= input("Enter Customer id: ")
    cust_name = input("Enter Customer name: ")
    city=input("enter you city:")
    customers_list.append({"cust_id":cust_id,"cust_name":cust_name,"city":city})
    print("Customer registration completed")

def get_customer_data():
    return customers_list