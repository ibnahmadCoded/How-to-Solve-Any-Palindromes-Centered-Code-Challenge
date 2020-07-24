def sum_numeric_palindromes_less_than(N):
    """ This fucntion returns the sum of all numeric palindromes less than
        a number passed as N in the argument """

    return sum([n for n in range(N) if str(n) == str(n)[::-1]])

print(sum_numeric_palindromes_less_than(10))
