#import decimal for the precise arithmetic needed in the rounding error
from decimal import*
#Create static rounding number
ROUNDING_NUMBER = 3

def main():
    #define the length of the decimal (will be important for the rounding error)
    getcontext().prec = 28

    #First problem, input this string of characters and determine the number
    string = '010000000111111010111001'
    stringLength = len(string)


    fraction = 0.0
    exponent = 0

    #This determines the exponent
    for i in range(11):
            #We can ignore the first character until the end (when we will add the sign) (i+1)
        if (int(string[i + 1]) == 1):
            exponent += 2**(10-i)
    
    #Determining the decimal in the mantissa
    for j in range(stringLength - 12):
        if(int(string[j+12]) == 1):
            fraction += .5**(j+1)  
    
    #use the formula (-1)^s * 2^(c-1023) * (1 + f) to determine result

    result =  2**(exponent - 1023) * (1 + fraction)

    #if s = 1, then the number is negative
    if (string[0] == 1):
        result *= -1
    
    #print the number
    print ('%.4f' % result, "\n")


    #First rounding -- Declare the variables needed
    resultChop = result
    counter: int = 0

    #Convert to normalized decimal floating point form and count how many iterations to do so
    while (resultChop > 1):
        resultChop = resultChop/10
        counter += 1

    #Create a 2nd variable equal to the chop, (will perform additional operations for rounding)
    resultRound = resultChop

    #Round with chopping
    resultChop = chop(resultChop, counter)
    #Using rounding method 
    resultRound += .5 / 10**ROUNDING_NUMBER 
    resultRound = chop(resultRound, counter)
    #print results
    print(resultChop, "\n")
    print(resultRound, "\n")

    #For absolute rounding error simply subtract abs of new from initial
    roundingError = (abs(result - resultRound))
    print(roundingError)

    #For relative we need to do the same thing, but divide by the intial result
    print(Decimal(Decimal(roundingError)/Decimal(result)), "\n")


    #Determine number of iterations before under the error bound.
    counter1 = 0
    err = 1/(counter1 +1)**3
    while (err >= 10**-4):
        err = 1/(counter1+1)**3 
        counter1 += 1

    #since NEXT term is less than error bound, we know that counter - 1 is the number of terms needed
    print(counter1 - 1, "\n")

    #Declare our function to use the bisection and newton method on, as well as the accuracy desired
    function = "x**3 + 4*x**2 - 10"
    accuracy: float = 10**-4 
    
    #Declare a left and right for the bisection method
    left = -4
    right = 7

    #Call bisection function and print result
    iter: int = bisection(left, right, function, accuracy)
    print(iter, "\n")

    #call newton function and print result 
    iter = newton_raphson(right, accuracy, function)
    print(iter)



#Function for bisection method
def bisection(left: float, right: float, function: str, accuracy: float):

    #Set x equal to left and evaluate the function
    x = left
    leftfunct = eval(function) 
    #Do same for right
    x = right
    rightfunct = eval(function)
    #We need to make sure that they are on opposite sides to find the root
    if (leftfunct * rightfunct >= 0):
        return

    #Declare max iterations (not really needed here, but just good practice)
    max = 200
    #Difference is right-left 
    diff = abs(right-left)
    #Counter to track no. of iterations
    counter = 0

    #while the accuracy has not been reached and our counter is under max
    while (diff >= accuracy and counter < max):
        #Add 1 to counter 
        counter += 1
        #Create a midpoint
        midpoint = (left + right)/2
        #If the midpoint is the root, then we can just break and return it
        x = midpoint
        midfunct = eval(function)
        if (midfunct == 0):
            break
        
        #If not then set x equal to left
        x = left
        leftfunct = eval(function)

        #If the function evaluated at left is opposite side of midpoint, then set right equal to midpt
        if ((leftfunct < 0 and midfunct > 0) or (leftfunct > 0 and midfunct < 0)):
            right = midpoint
        #If not then set left 
        else: 
            left = midpoint
        #Find the difference (for error threshold)
        diff = abs(right-left) 
    #Return the counter
    return counter

#Function to round by chopping
def chop(result, counter):
    #I'm sure there is a better way to do this, but this is a way that works (Learned from c)
    #We take the desired number of digits above 1 by multiplying by rounding number
    result = result * 10**ROUNDING_NUMBER


    #by making result an int we effectively cut off any of the decimals
    result = int(result)


    #now we return the number to normalized form
    result = float(result) / 10**ROUNDING_NUMBER

    #multiply counter to get the proper place value and return the result
    result = result * 10**counter

    return result

#Is simply the derivative of ("x^3 + 4x^2 -10")
def custom_derivative(value):
    return (3 * value* value) + (2 * 4 * value)

#Function to utilize newton_raphson method
def newton_raphson(initial: float, tolerance: float, sequence: str):
    # Track iterations
    counter = 0
    # Set x to the initial approximation
    x = initial
    #Find the derivative f'
    f = eval(sequence)  

    fPrime = custom_derivative(initial) 
    
    #We get our approximation using the intial divided by the derivative
    approximation: float = f / fPrime
    #As long as it's above the tolerance
    while(abs(approximation) >= tolerance):
        #find function f
        x = initial
        f = eval(sequence)
        #find the derivative
        fPrime = custom_derivative(initial)
        
        #Find the approximation
        approximation = f / fPrime
        
        #Subtract the approximation from initial and continue
        initial -= approximation
        counter += 1

    #Return the counter because that's what we're looking for
    return counter
    
#Call main function
if __name__ == "__main__":
    main()
