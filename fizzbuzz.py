n=[]
f=[]
def fizzbuzz (n,f):
 
    #n = input("Enter for list n")
    #f = input("Enter for list f")
    m = len(n) + len(f)

    if m % 3 == 0 and m % 5 == 0:
        return ("fizzbuzz")
    elif m % 3 == 0:
        return ("fizz")
    elif m % 5 == 0:
        return ("buzz")
    else:
        return (m)

print(fizzbuzz(n,f))
                