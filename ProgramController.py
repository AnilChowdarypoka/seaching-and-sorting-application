import random

from searching import LinearSearch as ls
from searching import BinarySearchTree as bst
from sorting import QuickSort as QS
from sorting import InsertionSort as IS

print("Hello.... Please make your choice", end="\n\n")

print("1.Searching")
print("2.Sorting", end="\n\n")

choice = int(input("please enter your selection here : "))

try:
    if choice not in [1, 2]:
        raise Exception("Invalid Choice")

    if choice == 1:
        data = []
        print("Working on Searching...")
        list_size = int(input("Enter the size of the data you wish to : "))
        random_list = input("Do you want to work on random list ? Y/n : ")

        if random_list not in ('Y', 'y', 'N', 'n'):
            random_pick = True
            print("Invalid choice, taking random list")
            for _ in range(list_size):
                data.append(random.randint(0, 1000))

        if random_list.lower() == 'n':
            random_pick = False
            for i in range(list_size):
                data.append((input(f"Enter your {i + 1}  element : ")))
        else:
            random_pick = True
            print("Generating random data")
            for _ in range(list_size):
                data.append(random.randint(0, 500))

        search_element = int(input("Enter your search number: ")) if random_pick else input(
            "Enter your search element: ")

        searching_algo = bst.BinarySearchTree(data) if list_size > 50 else ls.LinearSearch(data)

        if searching_algo.search_element(search_element):
            print("There is a match of given search element in main data")
        else:
            print("There is no match of given search element in main data")
            review = input("Do you want to see the data Y/n: ")
            if review.lower() == 'y':
                print(data)
    else:
        print("Working on Sorting...")
        list_size = int(input("Enter the size of the data you wish to : "))
        random_list = input("Do you want to work on random data ? Y/n : ")
        data = []

        if random_list not in ('Y', 'y', 'N', 'n'):
            print("Invalid choice, taking random data")
            for _ in range(list_size):
                data.append(random.randint(0, 500))

        if random_list.lower() == 'n':
            random_pick = False
            type_check = input("do you want to work on integers Y/n : ")
            for i in range(list_size):
                if type_check == 'Y':
                    data.append(int(input(f"Enter your {i + 1}  element : ")))
                else:
                    data.append((input(f"Enter your {i + 1}  element : ")))
        else:
            random_pick = True
            print("Generating random data")
            for _ in range(list_size):
                data.append(random.randint(0, 500))

        print("Data before sorting : ", data)

        sorted_data = IS.InsertionSort().sort_data(data) if list_size < 100 else QS.QuickSort().sort_data(data)

        print("Data after sorting : ", sorted_data)

except Exception as e:
    print(e)
