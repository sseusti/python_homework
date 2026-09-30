def lemonadeChange(bills: list[int]) -> bool:
    cash = {
        "5": 0,
        "10": 0,
        "20": 0        
    }
    
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
    bills = [5,5,5,10,20]
    print(lemonadeChange(bills))