import random
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

def write():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")

    menu_var = int(input())
    print()
    if menu_var == 1:
        createAccount()
    elif menu_var == 2:
        logAccount()
    elif menu_var == 0:
        print()
        print("Bye!")
        exit()

def luhn_algorithm(cards):
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
    card_number = "400000" + str(random.randint(100000000, 999999999))
    card_numbers = card_number
    #print(card_nos)
    checksum = 0
    for i in range(len(card_number)):
        if i%2 == 0:
            value = int(card_number[i]) * 2
            if value > 9:
                value -= 9
            card_number = card_number[:i] + str(value) + card_number[i+1:]
    for i in range(len(card_number)):
        checksum += int(card_number[i])
    if checksum % 10 != 0:
        card_numbers = int(card_numbers + str(10 - (checksum%10)))
    else:
        card_numbers = int(card_numbers + '0')
    card_pin = random.randint(1000, 9999)
    details = (i_d, card_numbers, card_pin)
    cur.execute("INSERT INTO card(id, number, pin) "
                "VALUES (?, ?, ?)", details)
    conn.commit()
    i_d += 1
    print("Your card has been created")
    print("Your card number:")
    print(f"{card_numbers}")
    print("Your card PIN:")
    print(f"{card_pin}")


def logAccount():
    print("Enter your card number:")
    number = int(input())
    numbers = (number, )
    print("Enter your PIN:")
    Pin = int(input())
    cur.execute("SELECT pin FROM card WHERE number = ?", numbers)
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
            account_info(numbers)
        else:
            print("Wrong card number or PIN!")
            print()
    else:
        print("Wrong card number or PIN!")
        print()


def account_info(cn):
    print("1. Balance")
    print("2. Add income")
    print("3. Do transfer")
    print("4. Close account")
    print("5. Log out")
    print("0. Exit")

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
        if luhn_algorithm(trans):
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
