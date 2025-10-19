def validate_data(monthly_payment: float, target_amount: float, monthly_rate: float) -> bool:
    return monthly_payment > 0 and target_amount > 0 and monthly_rate > 0

if __name__ == "__main__":
    monthly_payment = float(input())
    target_amount = float(input())
    monthly_rate = float(input())

    if not validate_data(monthly_payment, target_amount, monthly_rate):
        print("ошибка")
        exit()

    current = 0
    months = 0

    while current < target_amount:
        current += monthly_payment
        current += current * (monthly_rate / 100)
        months += 1

    print(months)
