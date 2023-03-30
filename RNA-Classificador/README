# Atividade #4: RNA Classificador de Padrões
##### Laboratório da disciplina Inteligência Artificial e Robótica - Ciência da Computação FEI

## Iris sem PCA

Código:
``` python
from  sklearn.datasets  import  load_iris
from  sklearn.neural_network  import  MLPClassifier
from  sklearn.metrics  import plot_confusion_matrix
import  matplotlib.pyplot  as  plt

data = load_iris()
features =data.data
target = data.target

plt.figure(figsize=(16,8))
plt.subplot(2,2,1)
plt.scatter(features[:,0], features[:,1], c=target,marker='o',cmap='viridis')

Classificador = MLPClassifier(hidden_layer_sizes = (10), alpha=1, max_iter=1000)
Classificador.fit(features,target)
predicao = Classificador.predict(features)

plt.subplot(2,2,3)
plt.scatter(features[:,0], features[:,1], c=predicao,marker='d',cmap='viridis',s=150)
plt.scatter(features[:,0], features[:,1], c=target,marker='o',cmap='viridis',s=15)

plot_confusion_matrix(Classificador, features, target,include_values=True,display_labels=data.target_names)
plt.show()
```
## Resultados

Matriz confusão:

![fg1-sempca.png](https://github.com/camylladias/CC7711/blob/main/RNA-Classificador/img/fg1-sempca.png?raw=true)

 ![fg2-sempca.png](https://github.com/camylladias/CC7711/blob/main/RNA-Classificador/img/fg2-sempca.png?raw=true)

## Iris com PCA
``` python
from  sklearn.datasets  import  load_iris
from  sklearn.neural_network  import  MLPClassifier
from  sklearn.metrics  import plot_confusion_matrix
from  sklearn.decomposition  import  PCA
import  matplotlib.pyplot  as  plt

data = load_iris()
features =data.data
target = data.target

plt.figure(figsize=(16,8))
plt.subplot(2,2,1)
plt.scatter(features[:,0], features[:,1], c=target,marker='o',cmap='viridis')

Classificador = MLPClassifier(hidden_layer_sizes = (10), alpha=1, max_iter=100)
Classificador.fit(features,target)
predicao = Classificador.predict(features)

plt.subplot(2,2,3)
plt.scatter(features[:,0], features[:,1], c=predicao,marker='d',cmap='viridis',s=150)
plt.scatter(features[:,0], features[:,1], c=target,marker='o',cmap='viridis',s=15)  

pca = PCA(n_components=2, whiten=True, svd_solver='randomized')
pca = pca.fit(features)
pca_features = pca.transform(features)

print('Mantida %5.2f%% da informação do conjunto inicial de dados'%(sum(pca.explained_variance_ratio_)*100))

plt.subplot(2,2,2)
plt.scatter(pca_features[:,0], pca_features[:,1], c=target,marker='o',cmap='viridis')  

ClassificadorPCA = MLPClassifier(hidden_layer_sizes = (10), alpha=1, max_iter=1000)
ClassificadorPCA.fit(pca_features,target)
predicao = ClassificadorPCA.predict(pca_features)

plt.subplot(2,2,4)
plt.scatter(pca_features[:,0], pca_features[:,1], c=predicao,marker='d',cmap='viridis',s=150)
plt.scatter(pca_features[:,0], pca_features[:,1], c=target,marker='o',cmap='viridis',s=15)
plt.show()

plot_confusion_matrix(Classificador, features, target,include_values=True,display_labels=data.target_names)
plt.show()

plot_confusion_matrix(ClassificadorPCA, pca_features, target,include_values=True,display_labels=data.target_names)
plt.show()
```
## Resultados
Matriz confusão 1:

![fg1-compca.png](https://github.com/camylladias/CC7711/blob/main/RNA-Classificador/img/fg1-compca.png?raw=true)

Matriz confusão 2:

![fg2-compca.png](https://github.com/camylladias/CC7711/blob/main/RNA-Classificador/img/fg2-compca.png?raw=true)

![fg3-compca.png](https://github.com/camylladias/CC7711/blob/main/RNA-Classificador/img/fg3-compca.png?raw=true)
##  Integrantes 

<div align="center">

| <img src="https://avatars.githubusercontent.com/evesantana" alt="Evelyn" width="50"/> | <img src="https://avatars.githubusercontent.com/camylladias" alt="Camylla" width="50"/> | <img src="https://avatars.githubusercontent.com/patriciamed" alt="Patricia" width="50" width="50"/>
|:------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------:|
| [Evelyn Santanna](https://github.com/evesantana)| [Camylla Dias](https://github.com/camylladias)| [Patrícia Medeiros](https://github.com/patriciamed)                          
</div>
