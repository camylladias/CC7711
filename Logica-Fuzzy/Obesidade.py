import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

#Variaveis de Entrada (Antecedent)
calorias = ctrl.Antecedent(np.arange(0, 9, 1), 'calorias')

#Variaveis de saída (Consequent)
peso = ctrl.Consequent(np.arange(0, 11, 1), 'peso')

# automf -> Atribuição de categorias automaticamente
calorias['pouco'] = fuzz.trapmf(calorias.universe, [-1,0,2,4])
calorias['razoavel'] = fuzz.trapmf(calorias.universe,[ 2,4,6,8])
calorias['bastante'] = fuzz.trapmf(calorias.universe, [4,6,8,9])

#calorias.automf(names=['pouco','razoável','bastante'])

# atribuicao sem o automf
peso['peso pena'] = fuzz.gaussmf(peso.universe, 1,6)
peso['peso medio'] = fuzz.gaussmf(peso.universe, 4, 10)
peso['peso pesado'] = fuzz.gaussmf(peso.universe, 8,11)


#Visualizando as variáveis
calorias.view()
peso.view()



#Criando as regras
regra_1 = ctrl.Rule(calorias['pouco'], peso['peso pena'])
regra_2 = ctrl.Rule(calorias['razoavel'], peso['peso medio'])
regra_3 = ctrl.Rule(calorias['bastante'], peso['peso pesado'])

controlador = ctrl.ControlSystem([regra_1, regra_2, regra_3])


#Simulando
Calculopeso = ctrl.ControlSystemSimulation(controlador)

notacalorias = int(input('calorias: '))
Calculopeso.input['calorias'] = notacalorias
Calculopeso.compute()

valorpeso = Calculopeso.output['peso']

print("\ncalorias %d \nServiço %d \npeso de %5.2f" %(
        notacalorias,
        valorpeso))


calorias.view(sim=Calculopeso)
peso.view(sim=Calculopeso)

plt.show()