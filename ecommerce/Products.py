products=[{"product_id":101,"pname":"keyboard","price":500,"stock_qty":35,"category":"Electronics"},
          {"product_id":102,"pname":"Mouse","price":350,"stock_qty":45,"category":"Electronics"},
          {"product_id":103,"pname":"Monitor","price":8000,"stock_qty":30,"category":"Electronics"},
          {"product_id":104,"pname":"CPU","price":2500,"stock_qty":25,"category":"Electronics"},
          {"product_id":105,"pname":"Printer","price":10500,"stock_qty":10,"category":"Electronics"},]

def add_new_product():
    product_id=int(input("Enter product_id:"))
    pname=input("Enter Product name:")
    price=float(input("Enter price:"))
    stock_qty=int(input("Enter stock Qty:"))
    category=input("Enter Category:")
    products.append({"product_id":product_id,"pname":pname,"price":price,"stock_qty":stock_qty,"category":category})


def get_product_data():
    return products
