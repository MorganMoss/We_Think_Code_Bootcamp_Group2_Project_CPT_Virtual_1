#####################################################
#                  CREDITS TO:                      #
#   ---------------------------------------------   #    
#   # Ndumiso   -   ndmkhize020 - CPT - Python      #
#   # Kerslee   -   mamulaud020-CPT-Python          #
#   # Morgan    -   mmoss020-CPT-Python             #
#   # Keenos    -   ksmith020-CPT-Python            #
#                                                   #
#####################################################

#### Imported Goods: ####
from colorama import Fore, Back, Style, init 
init()
import math
import os
import os.path
from os import path
import sys
import random
#########################

####Morgan's Code########
class puzzle_solver:
    #reference was taken from several sites as my initial blind attempt gave me weird errors
    #https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
    #https://towardsdatascience.com/solve-sudokus-automatically-4032b2203b64   
    def __init__(self, board):
        #initialising the board and grid size when object created
        self.grid_size = 9
        self.board = board

    def find_next_unsolved(self):
        #loops through board until it finds a blank space
        for co_ord_y in range(self.grid_size):
            for co_ord_x in range(self.grid_size):
                if self.board[co_ord_y][co_ord_x] == 0:
                    return (co_ord_y, co_ord_x)
                
        return None #will return none if there's no blank spaces - means it's solved too!
     
    def check_block(self, co_ord_y, co_ord_x, number):
        #checks if move valid in the 3x3 box the current position is in
                                                            # from 0 to 8    0|1|2
        box_x = co_ord_x // int(math.sqrt(self.grid_size))  #                3|4|5
        box_y = co_ord_y // int(math.sqrt(self.grid_size))  #                6|7|8
                                                            # same for both directions
        
        for y in range(box_y*3, box_y*3 + 3):
            for x in range(box_x * 3, box_x*3 + 3):
                if self.board[y][x] == number and (y,x) != (co_ord_y, co_ord_x):
                    return False
        return True                                              

    def check_row(self, co_ord_y, co_ord_x, number):
        #checks if move valid in the row of the current position
        for i in range(len(self.board[0])):
            if self.board[co_ord_y][i] == number and co_ord_x != i:
                return False
        return True
    
    def check_col(self, co_ord_y, co_ord_x, number):
        #checks if move valid in the column of the current position
        for i in range(len(self.board)):
            if self.board[i][co_ord_x] == number and co_ord_y != i:
                return False
        return True
            
    def check_all(self, co_ord_y, co_ord_x, number):
        #returns true if all checks passed
        #all checks go through the 
        return self.check_row(co_ord_y, co_ord_x, number) and self.check_col(co_ord_y, co_ord_x, number) and self.check_block(co_ord_y, co_ord_x, number)

    def solve(self):
        # This is a recursive method of solving, it will try all the legal moves for each sqaure until there are no blanks left. It backtracks if it's at a dead end
        next_unsolved = self.find_next_unsolved() 

        if not next_unsolved: # Will stop running when the entire board is full, as it returns None if it loops through everything and reaches the end
            return True # It'll stop the recursion once full
        else:
            co_ord_y, co_ord_x = next_unsolved # Otherwise it goes to the next blank space

        for n in range(1,10):
            if self.check_all(co_ord_y, co_ord_x, n): # It'll only accept valid moves for the next space
                self.board[co_ord_y][co_ord_x] = n  # It's going to take the smallest to largest valid moves for that space and try them one by one

                if self.solve(): # Recursion, it will go to the next unsolved, and see if it has valid moves
                    return True

                self.board[co_ord_y][co_ord_x] = 0 # Resets the space if the solve() returns false, as it means it needs to back track and try again because it hit a dead end

        return False # If the current space has no possible moves
#########################
    
####### Complete ########
class levels:
###### Constructor ######
    def __init__(self):
        self.normal = False
        self.textfile_name = "1.txt"
        self.random = True

        self.random_list = [] #make a list of all the textfiles in the current folder
        for _, _, files in os.walk("."):
            for filename in files:
                if filename[-4:] == ".txt":
                    self.random_list += [filename]

#########################
### Level 1 Complete ####
    ###Kerslee's Code####
    def read(self, textfile_name):
        # getting the path of the input file
        THE_BOARD = os.getcwd()
        my_file = os.path.join(THE_BOARD, textfile_name)

        # saving the ocntents of the file in a variable
        with open(my_file, 'r') as f1:
        
            string_list = f1.read()

        string_list = string_list.split()       # converting the string into a list

        # terminating the program if the list is not 9x9
        if len(string_list) != 81:
            print("Please enter a 9x9 board")
            exit()

        unsolved = []

        index = 0       # counter to keep track of the string list's index

        # saving the contents of the string list into a 2-d list
        for i in range(9):
            unsolved.append([])
            for _ in range(9):
                unsolved[i].append(int(string_list[index]))
                index += 1

        return(unsolved)
    def print_board(self, board):
        """Function to print a sudoku board in readable format

        Args:
            board (list): Sudoku board to be printed
        """

        num_of_rows = len(board)        # saving the number of rows to reduce time complexity later
        num_of_cols = len(board[0])     # saving the number of columns to reduce time complexity later

        # Checking if the board is a sudoku board
        if num_of_rows != 9 and num_of_cols != 9:
            print("This is not a sudoku board")
            return None         # returning nothing if the board is not a sudoku board
    
        seperator = "-" * 25        # a border/line to create vertical lines for 3x3 grid
        print(seperator)        # printing the top border

    
        # loop to print the board
        # iterates each row
        for i in range(num_of_rows):
        
            # loop to print the contents in each row
            for j in range(num_of_cols):
            
                # adding left border and horizontal line for 3x3 grid
                if (j % 3 == 0):
                    print('| ', end = "")
            
                number = board[i][j]        # saving the current number to reduce time complexity
                # printing the number only if it is not zero
                if number == 0:
                    print("_ ", end = "")
                else:
                    print("%d " %(number), end = "")

                # adding the right-side border
                if (j == num_of_rows - 1):
                    print('| ', end = "")
        
            print() # new line
        
            # bottom border
            if (i+1) % 3 == 0:
                print(seperator)
        # function which returns a solved sudoku puzzle
        # creates a copy of the board and then passes in into the recursive function to retain original board
    def print(self, unsolved):
        if self.normal:
            print("input board: ")
            self.print_board(unsolved)
            print()
        else: 
            self.print_colour(unsolved)
    #####################   

    ####Morgan's Code####  
    def set_value(self, board, co_ord_x, co_ord_y, value): #Code was left unused, but works the same as the other code.
        grid_size = 9
        board = board
        if board[co_ord_x][co_ord_y] > 0:
            print("That co-ordinate has a value! Choose a different co-ordinate")
            return board

        elif value in range(grid_size): 
            board[co_ord_x][co_ord_y] = value 
            return board

        else:
            print("That value is out of range! Value must be between 1 and ", grid_size)
            return board
        # Changes the value of the co-ordinate
    #####################
#########################
### Level 2 Complete ####
    ###Ndumiso's Code####
    def check_user_board(self, user_array, solution):
        matches = True #varible for matching cases 
        for check_down in range (9):    #starts by scanning array - down
            for colum_right in range (9):    #starts by scanning array - from left to right 
                if user_array [check_down] [colum_right] != solution  [check_down] [colum_right]:   #If array left != array user input
                    matches = False    #changes matches variable to "False"
        # goes through all the indexes and checks whether they match, or not. If they match, the `matches` variable reamains "True" (boolean). If not, the matches variable = "False
        #indent once to keep it in function

        if matches == True:                  
            print("Your answers are correct!")
        else:
            print("Your answers are incorrect!") 
            self.show_mistakes(solution, user_array)
    #####################
#########################
### Level 3 Complete ####
    #####Keeno's Code####
    def user_plays(self, board):
        user_board = []

        for i in range(len(board)):
            user_board.append([])
            for j in range(len(board)):
                user_board[i].append(board[i][j])

        
        continu = 'Y'
        while (continu == 'Y'):
            row = input('Row: ')
            #Input check
            while (row.isdigit() == False) or row[0] == "0" or len(row) > 1:
                print('Invalid row. Please enter a row value from 1 to 9.')
                row = input('Row: ')

            row = int(row[0])

            col = input('Column: ')
            #Input check
            while col.isdigit() == False or col[0] == "0" or len(col) > 1:
                print('Invalid column. Please enter a column value from 1 to 9.')
                col = input('Column: ')
 
            col = int(col[0])

            
            if board[row-1][col-1] != 0:
                print(board[row-1][col-1]) 
                print('You can\'t enter a value in there. Please enter a value in the blank spaces only.')
            else:
                val = input('Value: ')
                while (val.isdigit() == False) or val[0] == "0" or len(val) > 1: 
                    print('Invalid column. Please enter a column value from 1 to 9.')
                    val = input('Column: ')

                val = int(val[0])
                
                user_board[row-1][col-1] = val
                self.print(user_board)

            #if find_next_unsolved:
            continu = input('Keep playing? [Y/N] : ')
            continu = continu.upper()
            while (continu != 'Y' and continu != 'N'):
                print('Invalid selection. Please enter the letter Y or N.')
                continu = input('Keep playing? [Y/N] : ')
                continu = continu.upper()

            #need code; input check. Let's assume for now that user enters only Y/N"""

        return user_board
    def play_again(self):
        play_again = True
        while (play_again):
            
            self.game_settings()
            if self.random:
                if len(self.random_list) > 0:
                    board = self.read(self.random_list.pop())
                else: 
                    print("You are out of Puzzles!")
                    sys.exit()
            else:
                board = self.read(self.textfile_name)

            self.print(board)

            user_soln = self.user_plays(board)
            soln = self.solve_sudoku(board)
            

            self.check_user_board(soln, user_soln)
            i = input('\nDo you want to play again? [Y/N]: ')
            i = i.upper()
            while (i != 'Y' and i != 'N'):
                print('Invalid selection. Please enter the letter Y or N.')
                i = input('\nDo you want to play again? [Y/N]: ')
                i = i.upper()

            if i != 'Y':
                play_again = False
    def solution(self):
        yn = input('Go to the bonus advanced mode? [Y/N] : ').capitalize()[0]
        if yn.capitalize() == 'Y':
            self.solve_to_text()
            return None

        yes_no = True
        while(yes_no):
            user_file = input('Enter your file name.txt : ')
            try:
                f = open(user_file, "r")
            except IOError:
                print("File does not exist")
            finally:
                f.close()

            with open(user_file, "r") as f:
                string_list = f.read()
            f.close()
            string_list = string_list.split()

            if len(string_list) != 81:
                print("Please enter a 9x9 board")
                exit()

            user_in_board = []
            index = 0

            for i in range(9):
                user_in_board.append([])
                for _ in range(9):
                    user_in_board[i].append(int(string_list[index]))
                    index += 1
            print("\nYour board:")
            self.print(user_in_board)
            print()
            print("\nSolution:")

            s = self.solve_sudoku(user_in_board)
            self.print(s)

            #Solution call

            yes_no_in = input(("\nUpload another file? [Y/N] : "))
            yes_no_in = yes_no_in.upper()
            while (yes_no_in != 'Y' and yes_no_in != 'N'):
                print("Invalid selection. Please enter the letter Y or N only.")
                yes_no_in = input("\nUpload another file? [Y/N] : ")
            if yes_no_in != 'Y':
                yes_no = False
                #Changed inputs (row < 0 or row < 10) to row < 1 or row > 9
                #Changed (col <= 1 or col >= 9) to col < 1 or col > 9
                #Changed (val <= 1 or val >= 9) to val < 1 or val > 9    
    #####################

    ####Morgan's Code####
    def solve_sudoku(self, puzzle):
        # Create an instance of the solver, run the solve function
        object_solver = puzzle_solver(puzzle) 

        if object_solver.solve(): # If it manages to find a solution
            soln = object_solver.board # Get the solution
            del object_solver  # Clean up

            return soln
        else:
            # A lovely error message
            print("Error: This Sudoku Puzzle is IMPOSSIBLE!")

            return None
        pass
        #returns the solved puzzle as an array
    #####################
#########################
#### Bonus Complete #####
    ####Morgan's Code####
    def graphics_settings(self):
        # Choose between colour and normal text
        print()
        print("Choose a graphics setting: ")
        print("[1] Colour")
        print("[2] Text")
        if str(input("Input : ")) == "1":
            self.normal = False
        else:
            self.normal = True
    def game_settings(self):
        # Asks if they want to choosea a level or do a random one
        print("Choose a game setting: ")
        print("[1] Select Level")
        print("[2] Random")
        if str(input("Input : ")) == "1":
            self.random = False
        else:
            self.random = True
        print()
        # Takes in a valid .txt file    
        if not self.random:
            print()
            print("Please provide a .txt file name: ")
            s_input = str(input("Input : "))

            while s_input[-4:] != ".txt" or not path.exists(s_input):     
                print("That is not a textfile, please add .txt to the end and ensure the file exists in the same folder")    
                print()
                print("Please provide a .txt file name: ")
                s_input = str(input("Input : "))

            self.textfile_name = s_input
            print()
    def print_colour(self, board): # Currently using this over Kerslee's print code for the looks, however his works 100% if you set Normal to true on self.print(board)
        # Goes from -1 to 9 in a 2d format, one extra on each side to account for the grid number display
        for y in range(-1, 10): # Messy code is creative code :p
            text = ""
            # Makes the separating horizontal lines at intervals of 3
            if y % 3 == 0 or y == 9:
                text = (Fore.WHITE + Back.BLACK + ("---" * 11 +"----"))
                print(text)
                text = ""
            # Makes the top and bottom row of numbers
            if y == -1 or y == 9:
                text += (Fore.CYAN + Back.BLACK + ("     1  2  3   4  5  6   7  8  9     "))
                print(text)
                (Back.RESET + Fore.RESET)
                continue # Because I want to skip the for x

            for x in range(-1, 10):
                 # Makes the separating vertical lines at intervals of 3
                if x % 3 == 0:
                    text += (Fore.WHITE + Back.BLACK + "|")
                    (Back.RESET + Fore.RESET)
                # Makes the side rows of numbers
                if x == -1 or x == 9:
                    text += (Fore.CYAN + Back.BLACK + (" " + str(y+1) + " "))
                # Blank Square format
                elif board[y][x] > 0:
                    text += (Fore.WHITE + Back.BLACK + (" " + str(board[y][x]) + " "))
                # Filled Square format
                else:
                    text += (Fore.RED + Back.RESET + (" _ "))  
                    
            print(text)

            (Back.RESET + Fore.RESET)
        (Back.RESET + Fore.RESET)
    def show_mistakes(self, soln, user):
        ###Ndumiso's Code####
        # I'm reusing it with some edits to print mistakes
        for check_down in range (9):    #starts by scanning array - down
            text = ""
            for colum_right in range (9):    #starts by scanning array - from left to right 
                # Red if the user is wrong, green if they're right
                if self.normal: #checking if the output can be in colour or not
                    #Text Print
                    if user [check_down] [colum_right] != soln  [check_down] [colum_right]:   #If solution doesn't match the user's board at that spot
                        text += ( "|X|") #Code to format text
                    else:
                        text += ( "|"+ str(soln  [check_down] [colum_right]) +"|") #Code to format text

                else:  
                    #Colour print
                    if user [check_down] [colum_right] != soln  [check_down] [colum_right]:   #If solution doesn't match the user's board at that spot
                        text += (Fore.CYAN + Back.RED + (" "+ str(soln  [check_down] [colum_right]) +" ")) #Code to format text
                        text += (Style.RESET_ALL + "  ")
                    else:
                        text += (Fore.BLACK + Back.GREEN + (" "+ str(soln  [check_down] [colum_right]) +" ")) #Code to format text
                        text += (Style.RESET_ALL + "  ")
            print(Style.RESET_ALL) #Otherwise the console looks gross
            print (text) # Prints the row
            
            
        print(Style.RESET_ALL)
        #####################
    #####################
    #####Keeno's Code####
    def solve_to_text(self):
        yes_no = True
        while(yes_no):
            print("Upload a file [1]")
            print("Write to a file [2]")
            option = input()
            while option != "1" and option != "2":
                print("Incorrect Input!")
                option = input()

            if (option == "1"):
                user_file_1 = input('Enter your file name.txt : ')
                try:
                    f = open(user_file_1, "r")
                except IOError:
                    print("File does not exist!")
                finally:
                    f.close()

                with open(user_file_1, "r") as f:
                    string_list = f.read()
                f.close()
                string_list = string_list.split()

                if len(string_list) != 81:
                    print("Please enter a 9x9 board")
                    exit()

                user_in_board = []
                index = 0

                for i in range(9):
                    user_in_board.append([])
                    for _ in range(9):
                        user_in_board[i].append(int(string_list[index]))
                        index += 1
                print("\nYour board :")
                self.print(user_in_board)
                print()
                print("\nSolution :")
                s = self.solve_sudoku(user_in_board)
                self.print(s)
            
            elif option == "2":
                user_file_2 = input('What do you want to call your file? name.txt : ')
                myfile = open(user_file_2, "w")
                print("Enter your row values (No comma separating vales) :")
                for i in range(1, 10):
                    line = input('Row ' + str(i) + ': ')
                    line += "\n"
                    myfile.writelines(line)
                
                myfile.close()

                #This part below is copied straight from above
                #function would be better
                #This is just a test
            
                with open(user_file_2, "r") as f:
                    string_list = f.read()
                f.close()
                string_list = string_list.split()

                if len(string_list) != 81:
                    print("Please enter a 9x9 board")
                    exit()

                user_in_board = []
                index = 0

                for i in range(9):
                    user_in_board.append([])
                    for _ in range(9):
                        user_in_board[i].append(int(string_list[index]))
                        index += 1
                print("\nYour board:")
                self.print(user_in_board)
                print()
                print("\nSolution:")
                s = self.solve_sudoku(user_in_board)
                self.print(s)
          
            

            yes_no_in = input(("\nUpload another file? [Y/N] : "))
            yes_no_in = yes_no_in.upper()
            while (yes_no_in != 'Y' and yes_no_in != 'N'):
                print('Invalid selection. Please enter either the letter Y or N only.')
                yes_no_in = input(("Upload another file? [Y/N] : "))
                yes_no_in = yes_no_in.upper()
            if yes_no_in != 'Y':
                yes_no = False
            return None
    #####################
######################### 

###Ndumiso's Code####
def Main():
    funct = levels()
    funct.graphics_settings()
    user_in = ""
    print()
    print("Do you want to play a game or build a puzzle?")  #question posed to user for either a puzzle build, or to play a game
    while (user_in != "1" and user_in != "2" and user_in != "3"): #while the user input is not equals to/ is equals to...
        print("Play the Game [1]")
        print("Solve a Puzzle [2]")
        print("Exit [3]")
        user_in = str(input("Choose [1], [2] or [3] : ")) #if the user input is not equal to either of the three choices, print "Invalid selection."
        if (user_in != "1" and user_in != "2" and user_in != "3"): #If input is out of range of provided options
            print("Invalid selection.")
            print()
            continue
        print()    
        if user_in == "1":
            funct.play_again() #if the user chooses to play the game, call given function
        elif user_in == "2":
            funct.solution() #if user chooses to play the game, call the solution function
        else:
            print("Good bye.") #User input == 3, exits and prints message
            exit()

        user_in = 0
    # Program Startup
#####################

Main()

