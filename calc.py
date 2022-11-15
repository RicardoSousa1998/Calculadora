import math
continuar = "S"

while continuar == "S":
    #Criando um menu de opções
    print("+ para Adição")
    print("- para Subtração")
    print("* para Multiplicação")
    print("** para Potências")
    print("/ para Divisão")
    print("% para Resto da divisão")
    print("sqr para raiz")


    op = input("\n? Operação  ")
    
    while True:
      try:
          a = float(input("\nDigite o primeiro valor: "))
          b = float(input("Digite o segundo valor: "))
          break
      except ValueError:
          print("\nPor favor insira um valor numérico")

    if op == "+":
      result = a + b
      print("\n",a,"+",b,"=",result,"\n")
      continuar = input("Gostaria de fazer outra operação?  [S]/[N]").upper()

    elif op == "-":
      result = a - b
      print("\n",a,".",b,"=",result,"\n")
      continuar = input("Gostaria de fazer outra operação? [S]/[N]").upper()

    elif op == "*":
      result = a * b
      print("\n",a,"*",b,"=",result,"\n")
      continuar = input("Gostaria de fazer outra operação? [S]/[N]").upper()

    elif op == "/":
      while b == 0:
        print("O segundo valor não pode ser zero!")
        b = float(input("\nDigite o segundo valor (diferente de zero): "))
      result = a / b
      print("\n",a,"÷",b,"=",result,"\n")
      continuar = input("Gostaria de fazer outra operação? [S]/[N]").upper()

    elif op == "**":
      result = a ** b
      print("\n",a,"^",b,"=",result,"\n")
      continuar = input("Gostaria de fazer outra operação? [S]/[N]").upper()

    elif op == "%":
      result = a % b
      print("\n",a,"%",b,"=",result,"\n")
      continuar = input("Gostaria de fazer outra operação? [S]/[N]").upper()
    
    elif op == "sqr":
      print("\n", " √", a , "= ", math.sqrt(a) ," √", b , "= ",math.sqrt(b) ,"\n")
      continuar = input("Gostaria de fazer outra operação? [S]/[N]").upper()


