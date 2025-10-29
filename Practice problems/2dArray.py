# Example of a 2D array (list of lists) in Python

def twod_array_example():

    #2d array
    hours_flown = [
        [2,2,5,4,2],
        [2,1,4,0,1],
        [1,1,2,1,1],
        [4,3,4,3,0],
        [1,4,5]
        
    ]

    # Printing rows by index
    print(hours_flown[0])
    print(hours_flown[1])


    # Just printing rows of the 2d array in a loop
    for row in hours_flown:
        print(row)
        

    # Printing each value by itself in 2d array
    for row in hours_flown:
        for value in row:
            print(value)
    
    print(hours_flown[3][2])
    
    


def twod_array_again():
    # you can also make it like this 
    rows, cols = 3, 5

    num = [[0] * cols] * rows
    print (num)

def main():
    #twod_array_example()
    twod_array_again()
    
    
if __name__ == "__main__":
    main()