from z3 import *

# Variáveis para representar as propriedades das casas
cores = ['azul', 'amarelo', 'verde', 'vermelho', 'marfim']
bebidas = ['cha', 'suco', 'cafe', 'agua', 'leite']
nacionalidades = ['nor', 'ing', 'jap', 'ucr', 'esp']
animais = ['zebra', 'caracois', 'dog', 'fox', 'cavalo']
cigarros = ['ls', 'kools', 'parl', 'oldg', 'chester']

# Criando os inteiros no solver
variaveis = {v: Int(v) for v in cores + bebidas + nacionalidades + animais + cigarros}

s = Solver()

# Função auxiliar para adicionar restrições de distinção e intervalo
def restricoes_basicas(grupo):
    s.add(Distinct([variaveis[v] for v in grupo]))
    for v in grupo:
        s.add(variaveis[v] >= 1, variaveis[v] <= 5)

# Adicionando restrições básicas para cada categoria
for grupo in [cores, bebidas, nacionalidades, animais, cigarros]:
    restricoes_basicas(grupo)

# Adicionando as restrições específicas do problema
s.add(variaveis['ing'] == variaveis['vermelho'])
s.add(variaveis['esp'] == variaveis['dog'])
s.add(variaveis['verde'] == variaveis['cafe'])
s.add(variaveis['ucr'] == variaveis['cha'])
s.add(variaveis['verde'] == variaveis['marfim'] + 1)
s.add(variaveis['oldg'] == variaveis['caracois'])
s.add(variaveis['amarelo'] == variaveis['kools'])
s.add(variaveis['leite'] == 3)
s.add(variaveis['nor'] == 1)
s.add(Or(variaveis['chester'] == variaveis['fox'] + 1, variaveis['chester'] == variaveis['fox'] - 1))
s.add(Or(variaveis['kools'] == variaveis['cavalo'] + 1, variaveis['kools'] == variaveis['cavalo'] - 1))
s.add(variaveis['ls'] == variaveis['suco'])
s.add(variaveis['jap'] == variaveis['parl'])
s.add(variaveis['nor'] == variaveis['azul'] - 1)

# Verificação de satisfiabilidade e obtenção do modelo
if s.check() == sat:
    modelo = s.model()
    for v in variaveis:
        print(f"{v}: {modelo[variaveis[v]]}")
else:
    print('Não é possível satisfazer as restrições (unsat)')
