def calculadora():
  '''def matriz():#codigo pra importar matrizes do sistema
    arq=open('matriz.dat')#matriz.dat e uma matriz qualquer
    content=arq.read()
    lines= content.splitlines()
    nunMatriz= content.split()
    elementos=len(nunMatriz)
    linhas=len(lines)
    coluna= int(elementos/linhas)'''

  x=['a','3','3',[1,2,3],[4,5,6],[7,8,9]]
  y=['b','3','3',[9,8,7],[6,5,4],[3,2,1]]
  print('Bem-vindo á calculadora matricial, escolha a sua opção: ')
  print('Deseja usar o banco de dados (Opção 1), criar as suas próprias matrizes(opção 2) ou ambas(oçao 3)?\n')
  opcao=int(input('Escolha a sua opção:'))
  print('')
  if opcao==1:
     a=int(input('Escolha a sua opção:\n1)Soma de matrizes.(C=A+B ou C=A-B)\n2)Multiplicação escalar.(C=aA, onde a é um número real dado)\n3)Multiplicação matricial.(C=AxB)\n4)Transposição.\n5)Permutar duas linhas ou  duas colunas de posição.\n6)Somar a uma linha outra linha ou somar a uma coluna outra coluna.\n7)Multiplicar uma única linha ou uma única coluna por uma escalar.\n8)Inverter matriz quadrada 2x2.\n'))
     if a==1:#Matriz do banco de dados x=['name','i','j',elementos por linha]
        def sum_sub ():
            q=int(input('Escolha entre soma (1) ou subtração (2). ')
            if q==1:
                  if x[1]!=y[1] or x[2]!=y[2]:
                      print('Impossível realizar operação pois suas matrizes não possuem o mesmo número de linhas/colunas.\n')
                   else:
                      tamanho=int(x[1])
                      soma=[]
                      elementos=int(x[2])
                      for i in range (tamanho):                          
                          linha=[]
                          for j in range (elementos):      
                             soma_l=float(x[i+3][j])+float(y[i+3][j])
                             linha.append(soma_l)
                             soma.append(linha)
                      print('Este e o resultado da sua soma: ')
                      print(soma)
            if q==2:
                  
                  if x[1]!=y[1] or x[2]!=y[2]:
                      print('Impossível realizar operação pois suas matrizes não possuem o mesmo número de linhas/colunas.\n')
                  else:
                      tamanho=int(x[1])
                      subtração=[]
                      elementos=int(x[2])
                      for i in range (tamanho):
                          linha=[]
                          for j in range (elementos):
                              subtração_l=float(x[i+3][j])-float(y[i+3][j])
                              linha.append(soma_l)
                              subtração.append(linha)
                      print('Este e o resultado da sua subtração: ')
                      print(subtração)
    if a==2:
         def mult_esc ():#Função p/ multiplicação, similar a soma e subtração
                   k=int(input('Digite o valor pelo qual deseja que a matriz seja multiplicada: ')
                   tamanho=int(x[1])
                   produto=[]
                   elementos=int(x[2])
                   for i in range (tamanho):                          
                       linha=[]
                       for j in range (elementos):
                            mult_=x[i+3][i]*k
                            linha.append(mult_)
                       produto.append(linha)
                   print('O resultado da sua multiplicação é: ', produto)
    if a==3                     
  if opcao==2:
        print('anything')#Essa parte n e cmg
  if opcao==3:
        print('anything')#Invenção do quedinha


