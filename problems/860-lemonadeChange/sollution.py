"""
860. Lemonade Change
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
Note that you do not have any change in hand at first.
Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
"""


def lemonadeChange(bills: list[int]) -> bool:
    cash = {"5": 0, "10": 0}

    for c in bills:
        if c == 5:
            cash["5"] += 1

        elif c == 10:
            if cash["5"] == 0:
                return False

            cash["10"] += 1
            cash["5"] -= 1

        elif c == 20:
            if cash["10"] > 0 and cash["5"] > 0:
                cash["10"] -= 1
                cash["5"] -= 1

            elif cash["5"] >= 3:
                cash["5"] -= 3

            else:
                return False

    return True


if __name__ == "__main__":
    bills = [5, 5, 5, 10, 20]
    print(lemonadeChange(bills))
