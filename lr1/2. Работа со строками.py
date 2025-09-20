# 2. работа со строками

text = " Hello Python! "

t1 = text.strip().replace('!', "?").upper()
t2 = t1.lower().strip()

print(t1, t2)