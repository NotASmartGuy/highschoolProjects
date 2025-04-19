#sorting algorithm
print("Add the array\nJust leave nothing once the list is completed")
count = 1
arr = []
while True: #loop that keeps on adding to the error
    
    user = input("Enter the element:") #asks for the number
    if user == "": #checks if they want to exit
        print("sorting started for\n")
        break #kaboom
    print(count, "element entered") #shows how many elements have been entered
    arr.append(user) #adds it to the end of the list
    count = count + 1 #keeps count of the number of elements
    
     

n = len(arr) #finds the length of the array

def selectionSort():
    print("The list ", arr, "\nwill be SELECTION sorted")

    for i in range(n-1):
        print(arr)
        mindex = i
        print("Searching for a number smaller than", arr[mindex])

        for j in range(i+1,n):
            print("Searched", arr[j])

            if arr[j] < arr[mindex]:
                print(arr[j], "is the smallest")
                mindex = j

        arr[i], arr[mindex] = arr[mindex], arr[i]

def insertionSort():
    print("The list ", arr, "\nwill be INSERTION sorted")
    for i in range(1,n):
        print(arr)
        j = i-1
        
        key = arr[i]
        print("j =",arr[j],"comparing:", key)

        while j >= 0 and key < arr[j]:
            
            arr[j+1] = arr[j]
            j-=1 
            
            print("searching", arr[j])

        arr[j+1] = key
    
typeSort = int(input("For  Insertion Sort enter 1\nFor Selection Sort enter 2\n"))

if typeSort == 1:
    insertionSort()
elif typeSort == 2:
    selectionSort()
else:
    print("wrong input")


print("The sorted", arr)
