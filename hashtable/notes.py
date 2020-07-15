
    # recursive functions require
    ## base case
    ## move towards base case
    ## function has to call itself

# def slow_fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return slow_fibonacci(n-1) + slow_fibonacci(n-2)

# # complexity 2^n -- soooo slow
# print(slow_fibonacci(4))

# let's get rid of redundencies by storing results in a dict as we go so that when we can look up a calculation we've done before
# time complexity??? log n?
n = input("fibonacci count: ")
n = int(n)
cache = {}
def hash_fibonacci(n,count=0):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = hash_fibonacci(n-1) + hash_fibonacci(n-2)
        
        print(cache[n])
    return cache[n]


print("Your final, freaky-fast Fibonacci is:", hash_fibonacci(n))
