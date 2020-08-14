'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Base case
    if n == 0:
        return 1

    elif n < 0:
        return 0

    else: 
        # make 3 recursive calls
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
