lst = ['madam','Python',"malayalam",12321]

s_pal = list(filter(lambda x: isinstance(x, str) and x == x[::-1], lst))

print(s_pal)
