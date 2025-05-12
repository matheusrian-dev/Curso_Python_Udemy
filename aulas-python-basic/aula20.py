"""
Constantes = objetos que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

# velocidade atual do carro
velocidade = 60
# local em que o carro está na estrada
local_carro = 101
# velocidade máxima do radar 1
RADAR_1 = 60
# local onde o radar 1
LOCAL_1 = 100
# A distância onde o radar pega
RADAR_RANGE = 1

# if velocidade > RADAR_1:
#     print('Velocidade do carro ultrapassou o limite do radar 1.')

# if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
#     local_carro <= (LOCAL_1 + RADAR_RANGE) and \
#     velocidade > RADAR_1: #método rústico e não tão legível
#     print('Veículo foi multado em radar 1.')

verificar_local_carro = local_carro >= (
    LOCAL_1 - RADAR_RANGE
) and local_carro <= (LOCAL_1 + RADAR_RANGE)

verificar_velocidade_carro_no_radar = velocidade > RADAR_1

verificar_carro_multado_radar_1 = (
    verificar_local_carro and verificar_velocidade_carro_no_radar
)

# método mais limpo e legível
if verificar_carro_multado_radar_1:
    print('Veículo foi multado em radar 1.')
else:
    print('Veículo não foi multado no radar 1.')
