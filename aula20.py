"""
Constantes = objetos que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 60 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega 

# if velocidade > RADAR_1:
#     print('Velocidade do carro ultrapassou o limite do radar 1.')

# if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
#     local_carro <= (LOCAL_1 + RADAR_RANGE) and \
#     velocidade > RADAR_1: #método rústico e não tão legível
#     print('Veículo foi multado em radar 1.')

verificar_local_carro = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

verificar_velocidade_carro_no_radar = velocidade > RADAR_1

verificar_carro_multado_radar_1 = verificar_local_carro and verificar_velocidade_carro_no_radar

if verificar_carro_multado_radar_1 : #método mais limpo e legível
    print('Veículo foi multado em radar 1.')
else:
    print('Veículo não foi multado no radar 1.')