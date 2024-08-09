
#01
'''def area(largura, comp):
    r = largura * comp
    print(f'A largura de {largura} com o comprimento de {comp} da o resultado da area de {r}')

l = float(input("Digite a largura: "))
c = float(input("Digite o comprimento: "))
area(l, c)'''


#02

'''def lin():
    print('-' * len(msg))
def escreva(msg):
        lin()
        print(f'{msg}')
        lin()

for msg in range (3):
    msg = input('Digite algo: ')
    escreva(msg)'''

#03
'''from time import sleep
def contador(i, f, p):
    if p < 0:
        p*= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('END')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('END')



contador(1, 10, 1)
contador(10, 0, 2)
print('Agora você escolhe!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)'''
