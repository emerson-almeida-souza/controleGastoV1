from FONTES.coresTerminal import cores

categorias = ["\b1 - BANCOS", "\b2 - DOMÉSTICO"]

def menuCategoriaGasto():
    print(cores.yellow, 'DIGITE UMA OPÇÃO PARA CATEGORIA [PADRÃO: OUTROS]', cores.reset_color)
    for categoria in categorias:
        print(cores.blue, categoria, cores.reset_color)