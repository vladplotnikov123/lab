from account import Account

def test___init__():
    a = Account("yet")
    
    

def test_deposit():
    s = Account("Jeremy")
    assert s.deposit(500) == True
    assert s.deposit(-120) == False

def test_withdraw():
    w = Account("Yeet")
    assert w.deposit(500) == True
    assert w.withdraw(200) == True