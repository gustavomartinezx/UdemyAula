def generator(n=0, maximum=10):
    while True:
        yield

gen = generator()
print(next(gen))
print(next(gen))