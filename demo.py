def count_vowels():
    x = ['a','e','i','o','u']
    m = ""
    #m = input("enter a sentence")
    count=0
    tuple(x)
    tuple(m)
    dup_x = set(m)
    dup = len(m)-len(dup_x)
    count = ""
    for char in x:
        if char in m:
            count += str(char)

    print((count, dup))
count_vowels()