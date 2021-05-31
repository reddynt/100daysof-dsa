def eucledian_gcd(a, b):
    if b == 0:
        return a
    # else:
        # a, b = max([a, b]), min([a, b])
    a_ = a % b
    return eucledian_gcd(b, a_)

print(eucledian_gcd(357, 234))
print(eucledian_gcd(273, 100))
