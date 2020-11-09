import sqlite3
conn = sqlite3.connect('card.s3db')

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS  card("
            "id INTEGER,"
            "number TEXT,"
            "pin TEXT,"
            "balance INTEGER DEFAULT 0"
            ")")
conn.commit()


import random

#account_details = {}


def write():
    print(r'''1. Create an account
2. Log into account
0. Exit''')
    n = int(input())
    print()
    if n == 1:
        createAccount()
    elif n == 2:
        logAccount()
    elif n == 0:
        print()
        print("Bye!")
        exit()

def check(cards):
    card = str(cards)
    n = 0
    no = card[:15]
    checksum = 0
    for i in range(len(no)):
        if i % 2 == 0:
            value = int(no[i]) * 2
            if value > 9:
                value -= 9
            no = no[:i] + str(value) + no[i + 1:]
    for i in range(len(no)):
        checksum += int(no[i])
    if checksum % 10 != 0:
        n = 10 - (checksum % 10)
    if str(n) == card[-1]:
        return True
    else:
        return False

def createAccount():
    i_d = 0
    card_no = "400000" + str(random.randint(100000000, 999999999))
    card_nos = card_no
    #print(card_nos)
    checksum = 0
    for i in range(len(card_no)):
        if i%2 == 0:
            value = int(card_no[i]) * 2
            if value > 9:
                value -= 9
            card_no = card_no[:i] + str(value) + card_no[i+1:]
    for i in range(len(card_no)):
        checksum += int(card_no[i])
    if checksum % 10 != 0:
        card_nos = int(card_nos + str(10 - (checksum%10)))
    else:
        card_nos = int(card_nos + '0')
    card_pin = random.randint(1000, 9999)
    details = (i_d, card_nos, card_pin)
    cur.execute("INSERT INTO card(id, number, pin) "
                "VALUES (?, ?, ?)", details)
    conn.commit()
    i_d += 1
    print(f"""Your card has been created
Your card number:
{card_nos}
Your card PIN:
{card_pin}
""")


def logAccount():
    print("Enter your card number:")
    no = int(input())
    nos = (no, )
    print("Enter your PIN:")
    Pin = int(input())
    cur.execute("SELECT pin FROM card WHERE number = ?", nos)
    try:
        pins = list(cur.fetchone())
        pin = int(pins[0])
    except:
        pin = 0
    if pin != 0:
        print()
        if Pin == pin:
            print("You have successfully logged in!")
            print()
            account_info(nos)
        else:
            print("Wrong card number or PIN!")
            print()
    else:
        print("Wrong card number or PIN!")
        print()


def account_info(cn):
    print('''1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit''')
    a = int(input())
    print()
    if a == 1:
        cur.execute("SELECT balance FROM card WHERE number=?", cn)
        bals = list(cur.fetchone())
        bal = int(bals[0])
        print(f"Balance: {bal}")
        print()
        account_info(cn)
    elif a == 2:
        cur.execute("SELECT balance FROM card WHERE number=?", cn)
        bals = list(cur.fetchone())
        bal = int(bals[0])
        print("Enter income:")
        Inc = int(input())
        print("Income was added!")
        print()
        bal += Inc
        nos = list(cn)
        no = nos[0]
        Bal = (bal, no)
        cur.execute("UPDATE card SET balance = ? WHERE number = ?", Bal)
        conn.commit()
        account_info(cn)
    elif a == 3:
        print("Transfer")
        print("Enter card number:")
        trans = int(input())
        cur.execute("SELECT balance FROM card WHERE number=?", cn)
        bals = list(cur.fetchone())
        bal_s = bals[0]
        nos = list(cn)
        no = nos[0]
        if check(trans):
            Trans = (trans, )
            cur.execute("SELECT balance FROM card WHERE number=?", Trans)
            try:
                bals = list(cur.fetchone())
                bal_r = int(bals[0])
                print("Enter how much money you want to transfer:")
                Inc = int(input())
                if bal_s < Inc:
                    print("Not enough money!")
                assert bal_s >= Inc
            except:
                print("Such a card does not exist.")
            else:
                bal_s = bal_s - Inc
                bal_r += Inc
                Trans = (bal_r, trans)
                Ball = (bal_s, no)
                cur.execute("UPDATE card SET balance = ? WHERE number = ?", Trans)
                cur.execute("UPDATE card SET balance = ? WHERE number = ?", Ball)
                conn.commit()
                print("Success!")
        else:
            print("Probably you made a mistake in the card number. Please try again!")
        print()
        account_info(cn)
    elif a== 4:
        print("The account has been closed!")
        print()
        cur.execute("DELETE FROM card where number = ?", cn)
        conn.commit()
        write()
    elif a == 5:
        print("You have successfully logged out!")
        print()
        write()
    elif a == 0:
        print("Bye!")
        exit()

if __name__ == '__main__':
    while True:
        write()
