# Slot Machine Game
This is a Python program that simulates a slot machine game. It uses a 3x3 grid and allows the user to bet on up to 3 lines per spin. The game includes a deposit system to allow the user to add money to their balance, and a check_winning function to calculate the winnings for each spin.

# Dependencies
This program requires Python version 3.0 or higher.

# How to Run
1.Open a Python IDE or text editor and run the program.

2.When prompted, enter the amount you would like to deposit into your balance.

3.Follow the instructions to bet on a number of lines and spin the slot machine.

4.If you win, your winnings will be added to your balance. If you lose, your bet will be subtracted from your balance.

5.You can choose to play again or quit the game at any time.

# Code Description
The code starts by defining some constants such as MAX_LINES, MAX_BET, MIN_BET, ROWS, COLUMNS, and SYMBOL_COUNT. These constants are used throughout the code to set limits and determine the winning lines.

The check_winning function takes the columns, lines, bet, and values as input and returns the winnings and winning_lines. It checks the columns for winning lines and calculates the winnings based on the bet and value of the winning symbol.

The get_slot_machine_spin function takes the row, column, and symbols as input and returns a list of randomly generated symbols for each column.

The print_slot_machine function takes the columns as input and prints the slot machine grid to the console.

The deposit, get_bet, and get_number_of_lines functions handle user input to set the balance, bet amount, and number of lines to bet on.

The spin function is where the main logic of the game is implemented. It calls the get_number_of_lines, get_bet, and check_winning functions, and updates the balance based on the winnings or losses.

Finally, the main function handles the overall flow of the game. It calls the deposit function to set the initial balance, and then prompts the user to play or quit the game. If the user chooses to play, it calls the spin function and updates the balance. The game continues until the user chooses to quit. At the end of the game, the user's final balance is printed to the console.
