
high_ord_func_v2 = lambda x, func: x + func(x)

print(high_ord_func_v2(2, lambda x: x +1))
print(high_ord_func_v2(2, lambda x: x + 2))
## change
print(high_ord_func_v2(2, lambda x: x * 5))