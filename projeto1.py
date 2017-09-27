def main():
    print ('JOGO DA VELHA \n')
    l1 = '{var1} | {var2} | {var3}'
    l2 = '{var4} | {var5} | {var6}'
    l3 = '{var7} | {var8} | {var9}'
    print('1 | 2 | 3')
    print('--+---+--')
    print('4 | 5 | 6')
    print('--+---+--')
    print('7 | 8 | 9 \n')

    player1 = input('Escolha entre X e O: ')
    if  player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    lista = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game(player1, player2, lista)
   
    
    

def game(player1, player2, lista):
    count = 1
    while not temVencedor(lista):
        print ('\n')
        posicao = pedePosicao(count, player1, player2)
        print (' ')
        while not verificarPosicao(posicao-1, lista):
            posicao = pedePosicao(count,player1, player2)
        temVencedor(lista)
        adicionarPosicao(count, player1, player2, lista, posicao-1)
        printarTabuleiro(lista)
        count += 1
    
    print ('\nFIM DO JOGO! Parabens, {var1}!\n'.format(var1 = definirVencedor(lista,posicao,player1,player2)))
    jogarNovamente()

def definirVencedor(lista,posicao,player1,player2):
    vencedor = lista[posicao-1]
    if vencedor == player1:
        return 'Player1'
    else:
        return 'Player2'

            
def printarTabuleiro(lista):
    l1 = '{var1} | {var2} | {var3}'.format(var1 = lista[0], var2 = lista[1], var3 = lista[2])
    l2 = '{var4} | {var5} | {var6}'.format(var4 = lista[3], var5 = lista[4], var6 = lista[5])
    l3 = '{var7} | {var8} | {var9}'.format(var7 = lista[6], var8 = lista[7], var9 = lista[8])
    print(l1)
    print('--+---+--')
    print(l2)
    print('--+---+--')
    print(l3)


def adicionarPosicao ( count, player1, player2, lista, posicao):
    if count%2 == 0:
        lista[posicao] = player2
    else:
        lista[posicao] = player1

def pedePosicao(count, player1, player2):
    if count%2 == 0: # PLAYER 2
        print('Ã‰ a vez do player 2 ({})'.format( player2))
        posicao = input('Escolha a posiÃ§Ã£o:')
        return int(posicao)
    else:
        print('Ã‰ a vez do player 1 ({})'.format( player1))
        posicao = input('Escolha a posiÃ§Ã£o: ')
        return int(posicao)

    
def verificarPosicao(posicao, lista):
    if lista[int(posicao)] != ' ':
        print('PosiÃ§Ã£o jÃ¡ foi ocupada anteriormente. Tente novamente.')
        return False
    else:
        return True

def verificarLinha(lista):
    if not verificarVazia(lista):
        if lista[0] == lista[1] == lista[2] != ' ' or lista[3] == lista[4] == lista[5] != ' ' or lista[6] == lista[7] == lista[8] != ' ':
            return True
        else:
            return False
    else:
        return False

def verificarColuna(lista):
    if not verificarVazia(lista):
        if  lista[0] == lista[3] == lista[6] != ' ' or lista[1] == lista[4] == lista[6] != ' ' or lista[2] == lista[5] == lista[8] != ' ':
            return True
        else:
            return False
    else:
        return False

def verificarDiagonal(lista):
    if not verificarVazia(lista):
        if lista[0] == lista[4] == lista[8] != ' ' or lista[2] == lista[4] == lista[6] != ' ':
            return True
        else:
            return False
    else:
        return False

def verificarVazia(lista): #verifica se a lista esta vazia
    if lista == [' ',' ',' ',' ',' ',' ',' ',' ',' ']:
        return True
    else:
        False
    
def temVencedor(lista):
    if verificarDiagonal(lista) == True or verificarColuna(lista) == True or verificarLinha(lista) == True:
        return True
    else:
        return False
    
def jogarNovamente():
    x = input('Deseja jogar novamente (S/N): ')
    if x == 'S':
        main()
    else:
        print('SAIR')


main()
