txt = """
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
txt2 = txt.strip()
txt2 = txt2.lower()
txt2 = txt2.replace("!", ".")
txt2 = txt2.split('.')

print(txt2)

txt2[0] = txt2[0].split(' ')

def clean_text(text):
    text = text.strip()
    text = text.lower()
    text = text.replace('!', '.   ')
    text = text.replace('.', '')
    print(text)

text4 = txt2[0].count('python')
bruh = {}
for i in txt2[0]:
    bruh[i] = txt2[0].count(i)
txt2[0] = '-'.join(txt2[0])

print(txt2[0], text4, txt2[0].startswith('python'), txt2[0].startswith('python'), len(txt2[0]), txt2[0].count('a'), txt2[0].find("data"))
print(bruh)
print(txt2[0])
clean_text(txt)
