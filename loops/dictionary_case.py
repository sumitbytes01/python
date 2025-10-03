users = [{"id": 1, "total": 100, "coupon": "P20"},
         {"id": 2, "total": 200, "coupon": "P30"},
            {"id": 3, "total": 300, "coupon": "P40"}]

discounts = {"P20": (0.2, 0), "P30": (0.5,0), "P40": (0,10)}

for user in users:
    percent, flat = discounts.get(user["coupon"], (0,0))
    if percent:
        user["total"] = user["total"] * (1 - percent)
    elif flat:
        user["total"] = user["total"] - flat
    else:
        print("No discount applicable")
    print(f"User {user['id']} has to pay {user['total']}")