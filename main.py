import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1
ROWS=3
COLUMNS=3
SYMBOL_COUNT={
    "₹":5,
    "$":4,
    "£":3,
    "€":2,
}
def check_winnig (columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symobl=columns[0][lines]
        if all(column[line]==symobl for column in columns):
            winnings+= values[symobl]*bet
            winning_lines.append(line+1)
    
    return winnings,winning_lines


def get_slot_machine_spin(row,col,symbols):
    all_symboles=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symboles.append(symbol)
    
    columns=[]
    for _ in range(col):
        column=[]
        current_sysmbols=all_symboles[:]
        for _ in range(row):
            value=random.choice(current_sysmbols)
            current_sysmbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
   for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
               print(column[row],end="|")
            else:
                print(column[row],end='')
        
        print()

def deposit():
    while True:
        amount=input("What would you like to deposit ? ₹ ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greter than Zero.")
        else:
            print("Please enter a number.")

    return amount

def get_bet():
    
    while True:
        amount=input("What would you like to bet on each line ? ₹ ")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between ₹{MIN_BET}-₹{MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
     
    while True:
        lines=input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Enter a valid number of  lines")
        else:
            print("Please enter a number.")
    return lines
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet>balance:
            print(f"You do not have enough to bet that amount,your current balance is:₹{balance}")
        else:
            break
    print(f"you are betting ₹{bet} on {lines} lines. Total bet is equal to: ₹{total_bet}")
    slots = get_slot_machine_spin(ROWS,COLUMNS,SYMBOL_COUNT)
    print_slot_machine(slots)
    winnings,winning_line=check_winnig(slots,lines,bet, SYMBOL_COUNT)
    print(f"You Won ₹{winnings}.")
    print(f'you won on lines:',*winning_line)
    return winnings-total_bet
def main():
    balance = deposit()
    while True:
        print(f"current balance is ₹{balance}")
        answer=input("press enter to Play(q to quit).")
        if answer=='q':
            break
        balance +=  spin(balance)
    print(f'you left with ₹{balance}.')

main()