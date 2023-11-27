import dis

def magic_calculation(a, b):
    result = 98
    result += a ** b
    return result

# Verify that the bytecode is equivalent
print(dis.dis(magic_calculation))
