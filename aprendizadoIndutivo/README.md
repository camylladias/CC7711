# Árvore de Decisão - Atividade 2
##### Disciplina Inteligência Artificial e Robótica - Ciência da Computação FEI

## Base de Dados
Utilizamos a base de dados ``CriterioProva.arff`` que dispõe dos atributos:

 - P1 (primeira prova)
 - P2 (segunda prova)
 - PercFalta (percentual de falta)
 - resultado (aprovado ou reprovado)

Pela regra da base, a aprovação depende que a média >= 5 seja alcançada e que o percentual de falta seja inferior a 25.
 
 A base contém 307 exemplos para análise, onde obtivemos o resultado de *73 aprovados* e *234 reprovados*, gerando a seguinte entropia (critério de classificação): 
 
$$Entropia(73,-234) =  -(73/307)log2 (73/307) - (234/307)log2 (234/307) = 0.791$$
 
 
No contexto das Árvores de Decisão, a entropia é uma medida de desordem ou impureza em um nó.  Assim, um nó com composição mais variável, seria considerado de maior Entropia do que um nó que só passa ou só falha.  O nível máximo de entropia ou desordem é dado por 1 e a entropia mínima é dada por um valor 0.

###### +informações: [1.10. Decision Trees — scikit-learn 1.2.2 documentation](https://scikit-learn.org/stable/modules/tree.html#tree-mathematical-formulation)
 

## Árvore de Decisão
As Árvores de Decisão são um método de aprendizado supervisionado não paramétrico usado para classificação e regressão. O objetivo é criar um modelo que preveja o valor de uma variável de destino aprendendo regras de decisão simples inferidas dos recursos de dados. Uma árvore pode ser vista como uma aproximação constante por partes.

Árvore gerada pelo arquivo ``At3.py`` utilizando a base ``CriterioProva.arff``:

![arvore-decisao.png](https://github.com/camylladias/CC7711/blob/main/aprendizadoIndutivo/img/arvore-decisao.png?raw=true)
## Matriz de Confusão
Matriz de confusão é uma medida de desempenho para classificação de aprendizado de máquina. É extremamente útil para medir Recall, Precisão, Especificidade, Exatidão e curvas AUC-ROC.

Ao obter uma entropia de *0.0* nos resultados finais da árvore de decisão, a matriz de confusão formada trás precisão nos dados como podemos observar abaixo:

![matriz-confusao.png](https://github.com/camylladias/CC7711/blob/main/aprendizadoIndutivo/img/matriz-confusao.png?raw=true)
##  Integrantes 

<div align="center">

| <img src="https://avatars.githubusercontent.com/evesantana" alt="Evelyn" width="50"/> | <img src="https://avatars.githubusercontent.com/camylladias" alt="Camylla" width="50"/> | <img src="https://avatars.githubusercontent.com/patriciamed" alt="Patricia" width="50" width="50"/>
|:------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------:|
| [Evelyn Santanna](https://github.com/evesantana)| [Camylla Dias](https://github.com/camylladias)| [Patrícia Medeiros](https://github.com/patriciamed)                          
</div>