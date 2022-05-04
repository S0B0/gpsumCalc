gpsums = {

"F"   : 2,
"U"   : 3,
"TH"  : 5,
"O"   : 7,
"R"   : 11,
"C"   : 13,
"K"   : 13,
"G"   : 17,
"W"   : 19,
"H"   : 23,
"N"   : 29,
"I"   : 31,
"J"   : 37,
"EO"  : 41,
"P"   : 43,
"X"   : 47,
"S"   : 53,
"Z"   : 53,
"T"   : 59,
"B"   : 61,
"E"   : 67,
"M"   : 71,
"L"   : 73,
"NG"  : 79,
"ING" : 79,
"OE"  : 83,
"D"   : 89,
"A"   : 97,
"AE"  : 101,
"Y"   : 103,
"IA"  : 107,
"IO"  : 107,
"EA"  : 109

}


def menu():

    print()
    print()

    print("<============ [ GPSUM ] ============>")
    print("                                     ")
    print(" gematria primus sum in the terminal ")
    print("                                     ")
    print("<============= [ wip ] =============>")
    print("            # by S0B0 #")

    print()
    print()



def func(word, n):
    return [''.join(item) for item in zip(*[word[n:] for n in range(n)])]


def gepsum():

    
    print("Please input numeric value: ")
    print("[1] Start")
    print("[0] Exit")
        
    option = int(input(">: "))
    
    while option!=0:
        if(option == 1):

            sum=0
            word = input("Word: ").upper()

# =============  searching for  ============= 
#                     ING

            for item in func(word, 3):
                for key,value in gpsums.items():
                    if key == item:
                        sum = sum + value
                        word = word.replace(item,'#')
                        print(f"==== key: {key} ===== value: {value}")
            print(f"^^^^^^^^^^^^^^^^^  DEBUG INFO  ^^^^^^^^^^^^^^^^^^^^\nnew word is {word} and ----> sum ={sum}")

# =============  searching for  ============= 
#           EA,IO,IA,AE,OE,NG,EO,TH

            sum2 = sum
            for item in func(word, 2):
                for key,value in gpsums.items():
                    if key == item:
                        sum2 = sum2 + value
                        word = word.replace(item,'#')
                        print(f"==== key: {key} ===== value: {value}")
            print(f"new word is {word}  and ----> sum2 ={sum2}")

# =============  searching for  ============= 
#            REMAINING SINGLE LETTERS

            sum1 = sum2
            for item in func(word, 1):
                for key,value in gpsums.items():
                    if key == item:
                        sum1 = sum1 + value
                        word = word.replace(item,'#')
                        print(f"==== key: {key} ===== value: {value}")
            print(f"new word is {word} and sum3  = {sum1}\n ^^^^^^^^^^^^^^^^^  DEBUG INFO  ^^^^^^^^^^^^^^^^^^^^ \n   !!----> FINAL SUM  = {sum1} <----!!")
            print("\nwant to sum another input? Y/ N")
            q = input(">: ")
            if q == "y" or q =="Y" or q == "yes" or q == "YES" or q == "Yes":
                gepsum()
            elif q == "n" or q =="N" or q == "no" or q == "NO" or q == "No":
                print("exiting...farewell...")
                break
         
        elif (option == 0):
            print("Exiting...Farewell...")
        else:
            print("Invalid input!!!")
            gepsum()

menu()
gepsum()