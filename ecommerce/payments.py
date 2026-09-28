
def payment_methods():
    n=input("Enter payment methods(UPI,net_banking,COD):")
    if n=="UPI" or n=="net_banking" or n=="COD":
        if n=="COD":
            shipping_charges=100
        else:
            shipping_charges=50
        # print(f'Payment Method:{n} Shipping Charges={shipping_charges}')
         
    else:
        print("Please select Valid Payment Methods")
        shipping_charges=0
        
    return shipping_charges 
    '''
    if n=="UPI":
        bank=input("Enter your bank name:")
        # account_no=input("enter your account number:")
        # IFSC_code=input("Enter IFSC code:")
        # username=input("Enter username:")
    elif n=="net_banking":
        bank=input("Enter your bank name:")
        account_no=input("enter your account number:")
        IFSC_code=input("Enter IFSC code:")
        username=input("Enter username:")
    elif n=="COD":
        address=input("enter your addresss")
        mobile_no=input("enter mobile number")
    else:
        print("ERROR enter valid payment_method")
    '''
# print(payment_methods())