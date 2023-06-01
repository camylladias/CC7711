# Atividade #6: Lógica Fuzzy
##### Laboratório da disciplina Inteligência Artificial e Robótica - Ciência da Computação FEI

**Integrantes:**
Camylla Lima Dias
Patrícia Helena S. Medeiros
Evelyn Santana de Brito

## Código do sistema de cálculo obesidade
**Obs:** Para testar as distribuições com diferentes formatos *(trapezoidal (trapezio), triangular (triângulo) e gaussiana)* é necessidade que retire o código do bloco de comentário. Caso contrário o código irá compilar apenas no formato *gaussiano*. 

Recomenda-se que seja compilado apenas um formato por vez para melhor visualização dos gráficos e compará-los entre si.

**Código fonte:**
```python
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

#Variaveis de Entrada (Antecedent)
calorias = ctrl.Antecedent(np.arange(0, 9, 1), 'calorias')
TAtividade = ctrl.Antecedent(np.arange(0,11, 1), 'TAtividade')
#Variaveis de saída (Consequent)
peso = ctrl.Consequent(np.arange(0, 11, 1), 'peso')


calorias['pouco'] = fuzz.trapmf(calorias.universe, [-1,0,2,4])
calorias['razoavel'] = fuzz.trapmf(calorias.universe,[ 2,4,6,8])
calorias['bastante'] = fuzz.trapmf(calorias.universe, [4,6,8,9])

TAtividade['pouco'] = fuzz.gaussmf(TAtividade.universe, 0,1)
TAtividade['razoavel'] = fuzz.gaussmf(TAtividade.universe,5,2)
TAtividade['bastante'] = fuzz.gaussmf(TAtividade.universe, 10,2)
'''
#triangulo
TAtividade['pouco'] = fuzz.trimf(TAtividade.universe, 1, 4,6)
TAtividade['razoavel'] = fuzz.trimf(TAtividade.universe, 4, 7, 10)
TAtividade['bastante'] = fuzz.trimf(TAtividade.universe, 8, 10,11)
'''
'''
#trapesio
TAtividade['pouco'] = fuzz.trapmf(TAtividade.universe, 1,3,4,6)
TAtividade['razoavel'] = fuzz.trapmf(TAtividade.universe, 4, 6, 8, 10)
TAtividade['bastante'] = fuzz.trapmf(TAtividade.universe, 8, 9, 10,11)
'''

peso['peso pena'] = fuzz.gaussmf(peso.universe, 0,2)
peso['peso medio'] = fuzz.gaussmf(peso.universe, 7, 2)
peso['peso pesado'] = fuzz.gaussmf(peso.universe, 10,1)

'''
#triangulo
peso['peso pena'] = fuzz.trimf(peso.universe, [1, 4,6])
peso['peso medio'] = fuzz.trimf(peso.universe, [4, 7, 10])
peso['peso pesado'] = fuzz.trimf(peso.universe, [8, 10,11])


#trapesio
peso['peso pena'] = fuzz.trapmf(peso.universe, [1,3,4,6])
peso['peso medio'] = fuzz.trapmf(peso.universe, [4, 6, 8, 10])
peso['peso pesado'] = fuzz.trapmf(peso.universe, [8, 9, 10,11])
'''
#Visualizando as variáveis
calorias.view()
TAtividade.view()
peso.view()

#Criando as regras
regra_1 = ctrl.Rule(calorias['pouco'] & (TAtividade['pouco'] | TAtividade['razoavel']), peso['peso pena'])
regra_2 = ctrl.Rule(calorias['pouco'] & TAtividade['bastante'], peso['peso medio'])
regra_3 = ctrl.Rule(calorias['razoavel'] & (TAtividade['razoavel'] | TAtividade['bastante']), peso['peso pena'])
regra_4 = ctrl.Rule(calorias['razoavel'] & TAtividade['pouco'], peso['peso medio'])
regra_5 = ctrl.Rule(calorias['bastante'] & TAtividade['pouco'], peso['peso pesado'])
regra_6 = ctrl.Rule(calorias['bastante'] & (TAtividade['razoavel']| TAtividade['bastante']), peso['peso medio'])


controlador = ctrl.ControlSystem([regra_1, regra_2, regra_3,regra_4,regra_5,regra_6])

#Simulando
calculoPeso = ctrl.ControlSystemSimulation(controlador)

notaCalorias =int(input("calorias: "))
calculoPeso.input['calorias'] =notaCalorias
notaAtv = int(input('Tempo de atividade: '))
calculoPeso.input['TAtividade'] = notaAtv
calculoPeso.compute()

valorpeso = calculoPeso.output['peso']

print("\ncalorias %d \nTempo de de atividade %d \npeso de %5.2f" %(
        notaCalorias,
        notaAtv,
        valorpeso))


calorias.view(sim=calculoPeso)
TAtividade.view(sim=calculoPeso)
peso.view(sim=calculoPeso)

plt.show()
```
## Saídas para diferentes tipos de função de pertinência
Para avaliar as diferenças das diferentes funções de pertinência demos as mesmas entradas, `calorias = 5` e tempo de `atividade = 5`, para monitorar a diferença entre as saídas em cada formato de gráfico.

**Triangular:**
```python
calorias 5 
Tempo de de atividade 5 
peso de  5.26
```
Peso:
![pesoTriangulo.png](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Sa%C3%ADdas%20em%20diferentes%20pertinencias/pesoTriangulo.png?raw=true)

**Gaussiana:**
```python
calorias 5 
Tempo de de atividade 5 
peso de  4.48
```
Tempo de atividade com valor de entrada = 5
![TAtividade5.png](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Sa%C3%ADdas%20em%20diferentes%20pertinencias/TAtividade5.png?raw=true)

Peso:
![pesoGauss.png](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Sa%C3%ADdas%20em%20diferentes%20pertinencias/pesoGauss.png?raw=true)

**Trapezoidal:**
```python
calorias 5 
Tempo de de atividade 5 
peso de  5.10
```
Caloria com valor de entrada = 5
![Caloria5.png](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Sa%C3%ADdas%20em%20diferentes%20pertinencias/Caloria5.png?raw=true)

Peso
![pesoTrapezio.png](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Sa%C3%ADdas%20em%20diferentes%20pertinencias/pesoTrapezio.png?raw=true)
## Análise de sensibilidade entre as variáveis de entrada e de saída
*Explorando os valores limites de entrada e saída:*

**A menor entrada/saída:**
Para analisar o menor peso que podemos atingir, adicionamos o menor tempo de atividade e o menor consumo de calorias: ambos em zero (de acordo com a escala). Como nas imagens a seguir:

1. tempo de atividade mínima ![TAtividadesMin.png](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Analise%20de%20sensibilidade/Minimo/TAtividadesMin.png?raw=true)

2. calorias mínimas
![CaloriasMin.png](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Analise%20de%20sensibilidade/Minimo/CaloriasMin.png?raw=true)

3. peso
![PesoMin.png](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Analise%20de%20sensibilidade/Minimo/PesoMin.png?raw=true)

 **Resultado:**
```python
calorias 0 
Tempo de de atividade 0 
peso de  1.63
```

**A maior saída:**
Para analisar a maior saída que podemos atingir, adicionamos o menor tempo de atividade e o maior consumo de calorias. Como no exemplo a seguir:
1. atividade mínima
![AtividadeMin.png](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Analise%20de%20sensibilidade/M%C3%A1ximoSaida/AtividadeMin.png?raw=true)

2. calorias máximo
![CaloriasMax.png](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Analise%20de%20sensibilidade/M%C3%A1ximoSaida/CaloriasMax.png?raw=true)

3. peso máx![PesoMax.png](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Analise%20de%20sensibilidade/M%C3%A1ximoSaida/PesoMax.png?raw=true)

**Resultado (gaussiana):**
```python
Entradas :
Calorias 10
Atividade 0

Saída  peso 8.28
```
**A maior entrada:**
Para analisar o *peso* para as maiores entradas que podemos atingir, adicionamos maior tempo de atividade e maior consumo de calorias: ambos em 10 (de acordo com a escala). Como no exemplo a seguir:
1. tempo de atividade máximo
![TAtividadeMax.png](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Analise%20de%20sensibilidade/MaximoEntrada/TAtividadeMax.png?raw=true)

2. calorias máximo ![CaloriasMax.png](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Analise%20de%20sensibilidade/MaximoEntrada/CaloriasMax.png?raw=true)

3. peso ![pesoMed.png](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Analise%20de%20sensibilidade/MaximoEntrada/pesoMed.png?raw=true) 

**Resultado:**
```python
calorias 10 
Tempo de de atividade 10 
peso de  6.70
```
## Nova variável de entrada e regras
Adicionamos a variável `tAtividade` (tempo de atividade)
```python
    TAtividade['pouco'] 
    TAtividade['razoavel'] 
    TAtividade['bastante']
```
Conjunto das regras:
![Regras.jpg](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Regras.jpg?raw=true)

## Comparação entre os modelos (triangular, gaussiana, trapezoidal) em relação ao peso

**Triangular:**

![pesoTriangular.jpg](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Compara%C3%A7%C3%A3o%20entre%20modelos/pesoTriangular.jpg?raw=true)

**Gaussiana:**

![pesoGaussiana.jpg](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Compara%C3%A7%C3%A3o%20entre%20modelos/pesoGaussiana.jpg?raw=true)

**Trapezoidal:**

![pesoTrapezio.jpg](https://github.com/camylladias/CC7711/blob/main/Logica-Fuzzy/img/Prints/Compara%C3%A7%C3%A3o%20entre%20modelos/pesoTrapezio.jpg?raw=true)

## Como foi a experiência?

Criar um sistema de classificação de obesidade baseado em tempo de atividade, calorias ingeridas e com a saída de peso usando lógica fuzzy e os algoritmos trapezoidal, gaussiano e triangular foi uma experiência interessante. Definir conjuntos fuzzy, explorar diferentes algoritmos e técnicas, lidar com incerteza e imprecisão dos dados e ajustar as regras de inferência foram etapas um pouco mais trabalhosas. Os algoritmos trapezoidal, gaussiano e triangular trouxeram vantagens específicas em termos de precisão, suavidade ou simplicidade. No final, o sistema ofereceu classificações intuitivas para a detecção de obesidade.

Ao utilizar o algoritmo trapezoidal, percebemos como os intervalos trapezoidais permitiram uma modelagem precisa dos conjuntos fuzzy, especialmente quando havia inclinações ou faixas específicas de classificação de obesidade.

No entanto, o algoritmo gaussiano trouxe uma suavidade e transição gradual entre os conjuntos fuzzy, o que tornou a interpretação dos resultados mais intuitiva. Através das curvas de sino suaves, capturamos as incertezas graduais.

Por outro lado, o algoritmo triangular ofereceu uma simplicidade na implementação e compreensão. Com funções triangulares, conseguimos resultados diretos e facilmente interpretáveis. Embora tenha suas limitações, especialmente quando se trata de modelar transições abruptas, foi uma alternativa útil em alguns casos.

## Outro exemplo de aplicação da Lógica Fuzzy

Outro exemplo onde a lógica fuzzy poderia ser aplicada é no controle de um sistema de climatização em um prédio. As variáveis de entrada podem ser a temperatura externa, a temperatura interna e a umidade, enquanto a variável de saída pode ser a velocidade do ventilador ou a potência do ar-condicionado. Utilizando funções de pertinência adequadas e regras de inferência fuzzy, é possível controlar o sistema de climatização de forma mais inteligente e adaptável às necessidades dos ocupantes do prédio.
