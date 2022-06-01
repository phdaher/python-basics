from curses.ascii import isalnum


variable = input("Digite algo aqui: ")
print("Qual o tipo dessa variável", type(variable))
print("Tem espaços?", variable.isspace()) 
print("É um número?", variable.isnumeric())
print("É alfabético?", variable.isalpha())
print("É alfanumerico?", variable.isalnum())
print("Está em maiusculo?", variable.isupper())
print("Está em minusculo?", variable.islower())
print("Está capitalizado?", variable.istitle())