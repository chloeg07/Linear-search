#Make a pyhton code for a Linear search using the simpliest form possible
#Let user input their own list and their own target value
#Start at the first element. If it is the target value then we are finished. If it id not the target value check the next value in the list. Continue until you find the value or reach the end of the list.

def linear_search(arr, target):
    #Start at the first element and go through each element in the list
    for i in range(len(arr)):
        #Check if the current element is the target
        if arr[i] == target:
            return i  #Return the index if the target is found
    return -1  #Return -1 if the target is not found

if __name__ == "__main__":
    #Get user input for the list of numbers and the target value
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    target = int(input("Enter the target value: "))

    #Perform linear search
    result = linear_search(arr, target)
    #Output the result
    if result != -1:
        print(f"Target value {target} found at index {result}.")
    else:
        print(f"Target value {target} not found in the list.")
       










            
   
            
            
            
    