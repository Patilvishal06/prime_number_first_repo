
num = int(input("Enter the number"))

if num > 1:
    for i in range( 2, num):
        if(num % i) == 0:
            print(i, "not prime")
            break
        else:
            print(i,"number is prime number ")


