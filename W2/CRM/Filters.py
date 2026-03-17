def filtering_by_amount(clients, min_amount=None, max_amount=None):
    result=[]
    for client in clients:
        amount = client["amount"]
        if min_amount is not None and amount<min_amount:
            continue
        if max_amount is not None and amount>max_amount:
            continue
        result.append(client)
    return result
def filtering_by_date(clients, start_date=None, end_date=None):
    result = []
    for client in clients:
        date = client["date"]

        if start_date and date < start_date:
            continue
        if end_date and date > end_date:
            continue

        result.append(client)

    return result