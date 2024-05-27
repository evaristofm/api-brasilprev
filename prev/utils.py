

def calcula_data_carencia(data_carencia_inicial, data_atual):
    diferenca = data_atual - data_carencia_inicial
    dias_diferenca = diferenca.days
    return dias_diferenca