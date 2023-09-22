def calculate_riders_payment(successful_deliveries):
    base_pay = 5000
    commission = 0

    if successful_deliveries < 50:
        commission = 160
    elif 50 <= successful_deliveries < 59:
        commission = 200
    elif 60 <= successful_deliveries < 69:
        commission = 250
    else:
        commission = 500

    payment = successful_deliveries * commission + base_pay

    return payment

