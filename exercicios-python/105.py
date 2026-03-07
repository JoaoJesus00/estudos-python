def notas(*num, sit=False):
    """
    ->Função para analisar notas
    :param num: Notas, uma ou várias
    :param sit: visualizar situação (opcional)
    :return:retorna um dicionário com total de notas,
    maior e menor nota, média, e situação
    """
    dic = {}
    dic['Total de notas'] = len(num)
    dic['Maior nota'] = max(num)
    dic['Menor nota'] = min(num)
    dic['Média'] = sum(num) / len(num)
    if sit:
        if dic['Média'] < 5:
            dic['Situação'] = 'Ruim'
        elif dic['Média'] < 7:
            dic['Situação'] = 'Razoável'
        else:
            dic['Situação'] = 'Boa'
    return dic

resp = notas(3, 5, 2, 6.5, sit=True)
print(resp)
help(notas)