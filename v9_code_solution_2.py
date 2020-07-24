def sum_numeric_palindromes_less_than(N):
    """ This fuction returns the sum of all numeric palindromes less than
        a number passed as N in the function argument
    """
    palindromes = []
    for n in range (N):
        if str(n) == str(n)[::-1]:
            palindromes.append(n)

    return sum(palindromes)

print(sum_numeric_palindromes_less_than(10))
    
