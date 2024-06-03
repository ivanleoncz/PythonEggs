def decimal_to_binary_normal(n):

    s = ""
    while (n >= 1):
        s += str(n % 2)
        n //= 2
    
    return s[::-1].zfill(8)


print(decimal_to_binary_normal(13))
