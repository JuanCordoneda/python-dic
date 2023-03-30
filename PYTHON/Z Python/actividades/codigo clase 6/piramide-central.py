'''
0 -> 1 -> 3
1 -> 3 -> 2
2 -> 5 -> 1
3 -> 7 -> 0
'''

for i in range(4):
    espacios = 3 - i
    asteriscos = i * 2 + 1
    print(' ' * espacios + '*' * asteriscos)