N=100
i=1
for i in range(1,N+1):
    if(i%3!=0 and i%5!=0): #not multiples of 3 and 5
        print(i)
    elif(i%3==0 and i%5==0): #multiples of 3 and 5
        print("FizzBuzz")
    elif(i%3==0):            #multiples of 3
        print("Fizz")
    else:                    #multiples of 5
        if(i%5==0):
            print("Buzz")