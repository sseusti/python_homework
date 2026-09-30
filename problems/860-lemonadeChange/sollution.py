"""
860. Lemonade Change
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
Note that you do not have any change in hand at first.
Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
"""


def lemonadeChange(bills: list[int]) -> bool:
    cash = {"5": 0, "10": 0, "20": 0}

    for i in bills:
        cash[str(i)] += 1
        if i == 10:
            cash["5"] -= 1
        elif i == 20:
            if cash["10"] > 0:
                cash["10"] -= 1
                cash["5"] -= 1
            else:
                cash["5"] -= 3

        for _, v in cash.items():
            if v < 0:
                return False

    return True


if __name__ == "__main__":
    bills = [5, 5, 5, 10, 20]
    print(lemonadeChange(bills))
