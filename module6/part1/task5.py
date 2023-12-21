def rangeProduct(a,b):
    product = 1
    if a > b:
        for i in range(b,a):
            product *= i
    else:
        for i in range(a, b):
            product *= i
    return product

print(rangeProduct(1,10))


# The code below is experimental and made only for debug
# If you wish to test it uncomment it :)

# product = 1
# for i in range(1,10):
#         print(f"I: {i}; Product: {product}. Q: {i}*{product}")
#         product *= i

# print(f" Product: {product} ".center(50, "@"))