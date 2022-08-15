#temporizador regressivo
import time


def temporizador(t):
    while t:
        minuto, segundo = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minuto, segundo)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('----Temporizador Esgotado!!!----')


t = input('Insira o tempo em segundos: ')
temporizador(int(t))
