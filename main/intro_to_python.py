# First program made in python
#import numpy and assign it to np
import numpy as np

def main():

    #create the first array as an empty matrix with the dimensions 3x3. Set the type to short integer
    array1 = np.empty(shape = (3, 3), dtype = 'int16')

#nested for loop traverses array and sets value to 0 if i = j, if not sets value to 1
    for i in range(3):
        for j in range(3):
            if i == j:
                array1[i][j] = 1
            else:
                array1[i][j] = 0

    #print array
    print(array1, "\n")

#nested for loop that checks if i is not equal to j and if it is not, sets equal to 3
    for i in range(3):
        for j in range(3):
            if i != j:
                array1[i][j] += 3

    #print modified array
    print(array1, "\n")

    #create a 2nd array to copy over the data, using the same principle as earlier. Now we only need dimensions of 3x2
    array2 = np.empty(shape = (3, 2), dtype = 'int16')

    for i in range(3):
        for j in range(2):
            array2[i][j] = array1[i][j]

    #print the 2nd array
    print(array2, "\n")

#line to call main function
if __name__ == "__main__":
    main()

'''
I'm pretty sure there's a function to resize arrays manually, but since I've only done C before, I'm doing it in
a less efficient, yet logical way that should work
'''

