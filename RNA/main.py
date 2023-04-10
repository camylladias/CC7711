import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

print('Carregando Arquivo de teste')
arquivo = np.load('teste4.npy')
x = arquivo[0]
y = np.ravel(arquivo[1])



media_exec = [] 
desvio_padrao_exec = [] 
iteracoes=10000
camadas=(10,10)

for i in range(10):
    regr = MLPRegressor(hidden_layer_sizes=(10,10),
                        max_iter=10000,
                        activation='relu', #{'identity', 'logistic', 'tanh', 'relu'},
                        solver='adam',
                        learning_rate = 'adaptive',
                        n_iter_no_change=50)
    print('Treinando RNA')
    regr = regr.fit(x,y)

    print('Preditor')
    y_est = regr.predict(x)
    media_exec.append(np.average(y_est))
    desvio_padrao_exec.append(np.std(y_est))

    plt.figure(figsize=[14,7])

    #plot curso original
    plt.subplot(1,3,1)
    plt.plot(x,y)

    #plot aprendizagem
    plt.subplot(1,3,2)
    plt.plot(regr.loss_curve_)

    #plot regressor
    plt.subplot(1,3,3)
    plt.plot(x,y,linewidth=1,color='yellow')
    plt.plot(x,y_est,linewidth=2)
    plt.show()

print(f'Média das médias da execução com os parametros max_iter: {iteracoes} setados e o tamanho de camadas: {camadas} é igual a: '" %.2f" %np.average(media_exec))
print(f'Média dos desvios padrões da execução com os parametros max_iter: {iteracoes} setados e o tamanho de camadas: {camadas} é igual a: '"  %.2f" %np.std(desvio_padrao_exec))

