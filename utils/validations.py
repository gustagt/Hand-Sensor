

def valHandPosition( coordinates):
    if all(coordinates[0][1] > coordinates[i][1] for i in [5,9,13,17]): return'up'
    if all(coordinates[0][1] < coordinates[i][1] for i in [5,9,13,17] ): return'down'
    if all(coordinates[0][0] > coordinates[i][0] for i in [5,9,13,17]): return'left'
    if all(coordinates[0][0] < coordinates[i][0] for i in [5,9,13,17]): return'right'   

def valFingers(coordinates,index, handPosition):
    
    if handPosition == 'up' and coordinates[index][1] < coordinates[index-2][1]: # se o indice(ponta do dedo) estiver acima de dois pontos anterior.
        return True
    elif handPosition == 'down' and coordinates[index][1] > coordinates[index-2][1]: # se o indice(ponta do dedo) estiver abaixo de dois pontos anterior.
        return True

    elif handPosition == 'left' and coordinates[index][0] < coordinates[index-2][0]: # se o indice(ponta do dedo) estiver esquerda de dois pontos anterior.
        return True
    elif handPosition == 'right' and coordinates[index][0] > coordinates[index-2][0]: # se o indice(ponta do dedo) estiver direita de dois pontos anterior.
        return True
    return False


def valThumbFinger(coordinates, handPosition):
    if (handPosition == 'down' or handPosition == 'up') and ((coordinates[4][0] < coordinates[3][0] and # o ponto 4 estiver a esquerda do ponto 3 
                                                            coordinates[1][0] < coordinates[0][0]) or # o ponto 1 estiver a esquerda do ponto 0
                                                                (coordinates[4][0] > coordinates[3][0] and # o ponto 4 estiver a direita do ponto 3
                                                                coordinates[1][0] > coordinates[0][0])): # o ponto 1 estiver a direita do ponto 0
                                                                return True
    
    elif (handPosition == 'right' or handPosition == 'left') and ((coordinates[4][1] < coordinates[3][1] and # o ponto 4 estiver a acima do ponto 3 
                                                                coordinates[1][1] < coordinates[0][1]) or # o ponto 1 estiver a acima do ponto 0
                                                                    (coordinates[4][1] > coordinates[3][1] and  # o ponto 4 estiver a abaixo do ponto 3 
                                                                    coordinates[1][1] > coordinates[0][1])): # o ponto 1 estiver a abaixo do ponto 0
                                                                    return True
                                                        
    return False