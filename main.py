import os
import random
from bubblesort import bubble_sort
from insertionsort import insertion_sort
from selectionsort import selection_sort

# original list of 10 random numbers

def clear():
    if os.name == 'nt':  #windows
        _ = os.system('cls')
    else:  #macOS
        _ = os.system('clear')

def main_menu():

    #data checking
    def restart():
        clear()
        print("Invalid input, try again. \n" \
        "Remember: \n" \
        "- Ranges cannot be negative\n" \
        "- Integer inputs only")
        main_menu()

    def original():
        print("\nUnsorted: " , nums)

    def ask():
        try:
            print("\n Range? \n")
            range1 = int(input("From: "))
            if range1 >= 0:
                try:  
                    range2 = int(input("To:"))
                    if range2 <= range1 or ((range2-range1 > 100)):
                        restart()
                except ValueError:
                    restart()
            global nums
            nums = [random.randint(1,100) for x in range(range1,range2)]
            original()
        except ValueError:
            restart()

    try:
        option = int(input("------------------------------\n"
                        "| [*] Choose Your Algorithm. |\n"
                        "| [1] Bubble Sort            |\n"
                        "| [2] Insertion Sort         |\n"
                        "| [3] Selection Sort         |\n" 
                        "  [4] Exit                   |\n"
                        "------------------------------\n"
                        "\n [*] Your Choice: "))
        if option == 1:
            ask()
            bubble_sort(nums)
        elif option == 2:
            ask()
            insertion_sort(nums)
        elif option == 3:
            ask()
            selection_sort(nums)
        elif option == 4:
            print("Exiting Program.")
            exit()
        else:
            restart()
    except ValueError:
        restart()


main_menu()
