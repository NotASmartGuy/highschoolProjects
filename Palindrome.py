#Start Palindrome Tester
while True:
        
    pdme = input("Enter to test the Palidinrome:")

    pdme = pdme.replace(" ", "")
    pdme = pdme.lower()

    n = len(pdme)


    for f in range(0, n//2):
        check = True
        l = -(f+1)

        if pdme[f] != pdme[l]:
            check = False
            break

    if check == True:
        print(pdme, "is a Palindrome")
    else:
        print(pdme, "is not a Palindrome")

    if pdme == " ":
        break