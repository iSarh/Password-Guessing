
tries = 4

mainPassword = "Pass@word"

inputpassword = input("Enter Your Passeord: ")

while inputpassword != mainPassword:

    tries -= 1

    print(f"Wrong Password. {'Last' if tries == 0 else tries} Chances Left")

    inputpassword = input("Enter Your Passeord: ")

    if tries == 0 :

        print()
        print("All Tries Is Finished! ")

        break
else:
    print("Correct Password ")
