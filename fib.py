def fib_generator(stop,start=1,step=1):
    x,y=0,1
    num = start

    while num <= stop:
        x,y = y,x+y
        yield y
        num += step


results = ([turn for turn in fib_generator(10000)])[-1] #it is really fast(really !!!!!!!)
print(results)