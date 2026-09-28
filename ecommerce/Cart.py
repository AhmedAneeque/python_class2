def calculate_total(price,qty):
    if qty<=0:
        raise ValueError("Quantity must be greater than zero")
    return price * qty

