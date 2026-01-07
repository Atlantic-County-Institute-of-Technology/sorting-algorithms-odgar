import os
import random
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort

# original list of 10 random numbers

def clear():
    if os.name == 'nt':  #windows
        _ = os.system('cls')
    else:  #macOS
        _ = os.system('clear')

def restart():
    clear()
    input("Invalid input, try again. \n" \
    "Remember: \n" \
    "- Ranges cannot be negative or greater than 100\n" \
    "- Integer inputs only \n"
    "\n Click any key to continue..."
    )
    clear()

    def original():
        print("\nUnsorted: " , nums)    

def ask():
    range1 = int(input("\n Range? \n""From:"))
    if range1 <= 0: 
        restart()
    range2 = int(input("To: "))
    if range2 <= 0: restart
    if range2 <= range1: restart
    if range2-range1 > 100: restart()

    try:
        nums = [random.randint(1,100) for x in range(range1,range2)]
    except Exception:
        nums = "Error"
    return nums

    # def ask():
    #     try:
    #         print("\n Range? \n")
    #         range1 = int(input("From: "))
    #         if range1 >= 0:
    #             try:  
    #                 range2 = int(input("To:"))
    #                 if range2 <= range1 or ((range2-range1 > 100)) or range >= 0:
    #                     restart()
    #             except ValueError:
    #                 restart()
    #         nums = [random.randint(1,100) for x in range(range1,range2)]
    #         original()
    #     except ValueError:
    #         restart()
    #     return nums


def main_menu():
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
            try: 
                clear()
                print("[Bubble Sort]")
                bubble_sort(nums=ask())
            #accounts for non-numerical exceptions
            except Exception: restart()
        elif option == 2:
            clear()
            print("[Insertion Sort]")
            insertion_sort(nums=ask())
        elif option == 3:
            clear()
            print("[Selection Sort]")
            selection_sort(nums=ask())
        elif option == 4:
            print("Exiting Program.")
            exit()
        else:
            restart()
    except ValueError:
        restart()


while True:
    main_menu()
