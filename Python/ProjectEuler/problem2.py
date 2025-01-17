""" Even Fibonacci
    Each new term in the Fibonacci sequence is generated by adding the previous two terms.
    By starting with 1 and 2, the first 10 terms will be:
      1,2,3,5,8,13,21,34,55,89,...
    By considering the terms in the Fibonacci sequence whose values do not exceed four
    million, find the sum of the even-valued terms.
"""

"""
   make a list
   go through the list one by one
     add to the total
     check that the total isn't past 4,000,000
   find the sum of the even-valued terms
"""

def fibonacci(number):
    
    index=0
    total=0
    mylist=[1,2] #start off the list
    while(mylist[index]<number):
        if(mylist[index]%2==0): #check if even, if so, then add to the sum
            total = total + mylist[index]
        if(mylist[index]<number):
            index = index + 1
            mynewvalue = mylist[index] + mylist[index-1]
            mylist.append(mynewvalue)

    return total


if __name__ == "__main__":
    #print fibonacci(20)
    print fibonacci(4000000)