#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

a = 10
b = 5

return_add = add(a, b)
return_sub = sub(a, b)
return_mul = mul(a, b)
return_div = div(a, b)

print("{} + {} = {}".format(a, b, return_add))
print("{} - {} = {}".format(a, b, return_sub))
print("{} * {} = {}".format(a, b, return_mul))
print("{} / {} = {}".format(a, b, return_div))
