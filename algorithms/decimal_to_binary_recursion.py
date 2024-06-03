def decimal_to_binary(n):

    def calc(n):

        if n == 1:
            return str(n % 2)

        return str(n % 2) + calc(n // 2)

    return calc(n)[::-1].zfill(8)

print(decimal_to_binary(13))
