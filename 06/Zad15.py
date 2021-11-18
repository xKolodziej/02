colours = ["black","white","blue","red","yellow"]
content = str(colours)

f= open("plik.txt", "a")
f.write(content)
f.close()
