import time, json

def save_data(money, balance_list, possible_purchases, limit, cps, timer, start_limit, multiplier):
    _money = money
    _balance_list = balance_list
    _possible_purchases = possible_purchases
    _limit = limit
    _cps = cps
    _timer = timer
    _time = time.perf_counter()
    _start_limit = start_limit
    _multiplier = multiplier

    data_dict = {
        "Money": _money,
        "Limit": _limit,
        "Possibly products": len(_possible_purchases),
        "Balance list": _balance_list,
        "Cockie/sec": _cps,
        "Start Limit": _start_limit,
        "Multiplier": _multiplier,
                 }

    f = open("program_data.txt", "a")
    f.write(json.dumps(data_dict))
    f.write('\n')
    f.close()
