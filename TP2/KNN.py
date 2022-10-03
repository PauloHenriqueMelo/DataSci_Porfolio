import pandas as pd
import numpy as np
from collections import Counter
def distancia_euclidiana(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


class KNN:
    def __init__(self, k=3):
        self.k = k

    def ler_dados(self, X, y):
        self.X_train = X
        self.y_train = y

    def prever(self, X):
        y_pred = [self.preveja(x) for x in X]
        return np.array(y_pred)

    def preveja(self, x):
        distancias = [distancia_euclidiana(x, x_train) for x_train in self.X_train]
        k_idx = np.argsort(distancias)[: self.k]
        k_rotulos = [self.y_train[i] for i in k_idx]
        mais_comum = Counter(k_rotulos).most_common(1)
        return mais_comum[0][0]

def estatistica(y_true,y_pred):
    
    acuracia = len([y_true[i] for i in range(len(y_pred)) if y_true[i]==y_pred[i]])/len(y_pred)
    
    precisao_setosa= len([y_pred[i] for i in range(len(y_pred)) if y_true[i]==y_pred[i] and y_pred[i]==0])/len([y_pred[i] for i in range(len(y_pred)) if y_pred[i]==0])
    precisao_virginica=len([y_pred[i] for i in range(len(y_pred)) if y_true[i]==y_pred[i] and y_pred[i]==1])/len([y_pred[i] for i in range(len(y_pred)) if y_pred[i]==1])
    precisao_versicolor= len([y_pred[i] for i in range(len(y_pred)) if y_true[i]==y_pred[i] and y_pred[i]==2])/len([y_pred[i] for i in range(len(y_pred)) if y_pred[i]==2])
    
    revocacao_setosa=len([y_pred[i] for i in range(len(y_pred)) if y_true[i]==y_pred[i] and y_pred[i]==0])/len([y_true[i] for i in range(len(y_pred)) if y_true[i]==0])
    revocacao_virginica=len([y_pred[i] for i in range(len(y_pred)) if y_true[i]==y_pred[i] and y_pred[i]==1])/len([y_true[i] for i in range(len(y_pred)) if y_true[i]==1])
    revocacao_versicolor=len([y_pred[i] for i in range(len(y_pred)) if y_true[i]==y_pred[i] and y_pred[i]==2])/len([y_true[i] for i in range(len(y_pred)) if y_true[i]==2])
    
    f1_setosa= 2* (precisao_setosa*revocacao_setosa)/(precisao_setosa+revocacao_setosa)
    f1_virginica=2* (precisao_virginica*revocacao_virginica)/(precisao_virginica+revocacao_virginica)
    f1_versicolor=2* (precisao_versicolor*revocacao_versicolor)/(precisao_versicolor+revocacao_versicolor)
    
    
    return acuracia, [[precisao_setosa, revocacao_setosa ,f1_setosa],[precisao_virginica, revocacao_virginica, f1_virginica],[precisao_versicolor, revocacao_versicolor,f1_versicolor]]

def rotulos_para_numeros(mylist):
    returnlist=[]
    for n in mylist:
        if n== 'Iris-setosa':
            returnlist.append(0)
        elif n== 'Iris-virginica':
            returnlist.append(1)
        elif n== 'Iris-versicolor':
            returnlist.append(2)
        else:
            print("error")
    return returnlist
treino=pd.read_csv('treino.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'],sep=";")
treino=np.array(treino)

teste = pd.read_csv('teste.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'],sep=";")
teste=np.array(teste)

def matriz_de_confusao(realidade,previsao):
    matriz=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(realidade)):
        matriz[realidade[i]][previsao[i]]+=1
    return matriz

x_teste= np.delete(teste, 4, 1)
x_treino= np.delete(treino, 4, 1)
x,y,z,t,s= teste.T
a,b,c,d,e= treino.T
y_teste=rotulos_para_numeros(s)
y_treino=rotulos_para_numeros(e)

k = 2
meu_KNN = KNN(k=k)
meu_KNN.ler_dados(x_treino, y_treino)
estimativas = meu_KNN.prever(x_teste)
estimativas = list(estimativas)
acuracia, array = estatistica(y_teste,estimativas)


df = pd.DataFrame(array, index =['iris setosa', 'iris virginica', 'iris versicolor'], columns=['precisao','revocacao','f1'])

print("com K=2")
print(df)
print("valor da acuracia:", acuracia)
matriz=matriz_de_confusao(list(y_teste),estimativas)
df = pd.DataFrame(matriz, index =['iris setosa', 'iris virginica', 'iris versicolor'], columns=['iris setosa','iris virginica','iris versicolor'])
print(df)
k = 3
meu_KNN = KNN(k=k)
meu_KNN.ler_dados(x_treino, y_treino)
estimativas = meu_KNN.prever(x_teste)
estimativas = list(estimativas)
acuracia, array = estatistica(y_teste,estimativas)




df = pd.DataFrame(array, index =['iris setosa', 'iris virginica', 'iris versicolor'], columns=['precisao','revocacao','f1'])
print("\n")
print("\n")
print("com K=3")
print(df)
matriz=matriz_de_confusao(list(y_teste),estimativas)
df = pd.DataFrame(matriz, index =['iris setosa', 'iris virginica', 'iris versicolor'], columns=['iris setosa','iris virginica','iris versicolor'])
print(df)
print("valor da acuracia:", acuracia)

k = 5
meu_KNN = KNN(k=k)
meu_KNN.ler_dados(x_treino, y_treino)
estimativas = meu_KNN.prever(x_teste)
estimativas = list(estimativas)
acuracia, array = estatistica(y_teste,estimativas)



df = pd.DataFrame(array, index =['iris setosa', 'iris virginica', 'iris versicolor'], columns=['precisao','revocacao','f1'])
print("\n")
print("\n")
print("com K=5")
print(df)
matriz=matriz_de_confusao(list(y_teste),estimativas)
df = pd.DataFrame(matriz, index =['iris setosa', 'iris virginica', 'iris versicolor'], columns=['iris setosa','iris virginica','iris versicolor'])
print(df)
print("valor da acuracia:", acuracia)




k = 8
meu_KNN = KNN(k=k)
meu_KNN.ler_dados(x_treino, y_treino)
estimativas = meu_KNN.prever(x_teste)
estimativas = list(estimativas)
acuracia, array = estatistica(y_teste,estimativas)




df = pd.DataFrame(array, index =['iris setosa', 'iris virginica', 'iris versicolor'], columns=['precisao','revocacao','f1'])
print("\n")
print("\n")
print("com K=8")
print(df)
matriz=matriz_de_confusao(list(y_teste),estimativas)
print("MATRIZ DE CONFUSAO")
df = pd.DataFrame(matriz, index =['iris setosa', 'iris virginica', 'iris versicolor'], columns=['iris setosa','iris virginica','iris versicolor'])
print(df)
print("valor da acuracia:", acuracia)

k = 32
meu_KNN = KNN(k=k)
meu_KNN.ler_dados(x_treino, y_treino)
estimativas = meu_KNN.prever(x_teste)
estimativas = list(estimativas)
acuracia, array = estatistica(y_teste,estimativas)




df = pd.DataFrame(array, index =['iris setosa', 'iris virginica', 'iris versicolor'], columns=['precisao','revocacao','f1'])
print("\n")
print("\n")
print("com K=32")
print(df)
print("MATRIZ DE CONFUSAO")
matriz=matriz_de_confusao(list(y_teste),estimativas)
df = pd.DataFrame(matriz, index =['iris setosa', 'iris virginica', 'iris versicolor'], columns=['iris setosa','iris virginica','iris versicolor'])
print(df)
print("valor da acuracia:", acuracia)