def number_generator(stop,start=1,step=1):
    num = start
    while num<=stop:
        yield num
        num = num + step

result = number_generator(12)
print(result) # you will get a generator object,you will have to typecast it using next() function like in the next statement
print(next(result))

for num in number_generator(10):
    print(num) #here the for loop implicitly uses next() ,we don't have to do anything