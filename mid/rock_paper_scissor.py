def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    
    
    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if rules[p1] == p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"
