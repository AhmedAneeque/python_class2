def delivery_charges():
    method=input("enter delivery method as stadnard or prime:")
    d_charges=0
    if method=="standard":
        d_charges=100
    elif method=="prime":
        d_charges=50
    else:
        pass
    return d_charges

# print(delivery_charges())
    
