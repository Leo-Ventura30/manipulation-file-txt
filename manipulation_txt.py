import os

text = "Python is best language\n"
text = text + "to security and\n"
text += "datascience or JS for web"

# name = input("nome do arquivo")
# dot = "."
# ext = ['txt', 'csv', 'html', 'excel']
# name_file = name+".txt" || name_file = name+dot+ext
# file = open(os.path.join(name_file))


# se não existir oa arquivo, ele criara automaticamente
print(text)
file = open(os.path.join('test.txt'), "w")

for word in text.split():
    file.write(word+" ")

file.close()

file = open("./test.txt")
content_file = file.read()
file.close()

print(content_file)
