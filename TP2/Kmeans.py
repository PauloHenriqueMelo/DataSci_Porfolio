import pandas as pd
import numpy as np

iris=pd.read_csv('iris.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'],sep=";")
iris=np.array(iris)

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

x_iris= np.delete(iris, 4, 1) 

x,y,z,t,s= iris.T

y_iris=rotulos_para_numeros(s)


np.random.seed(42)


def distancia_euclidiana(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


class KMeans:
    def __init__(self, K=5, interacoes_maximas=100):
        self.K = K
        self.interacoes_maximas = interacoes_maximas


        
        self.clusters = [[] for _ in range(self.K)]
       
        self.centroides = []

    def prever(self, X):
        self.X = X
        self.n_amostras, self.n_features = X.shape
        
        
        ids_amostras_aleatorio = np.random.choice(self.n_amostras, self.K, replace=False)

        self.centroides = [self.X[idx] for idx in ids_amostras_aleatorio]

        
        for _ in range(self.interacoes_maximas):
            self.clusters = self.criar_clusters(self.centroides)


            
            centroides_antigos = self.centroides
            self.centroides = self.pegar_centroide(self.clusters)

            
            if self.sao_iguais(centroides_antigos, self.centroides):
                break

        
        
        return self.obter_rotulos_dos_clusters(self.clusters)

    def obter_rotulos_dos_clusters(self, clusters):
        
        labels = np.empty(self.n_amostras)

        for cluster_idx, cluster in enumerate(clusters):
            for sample_index in cluster:
                labels[sample_index] = cluster_idx
        return labels

    def criar_clusters(self, centroides):
        
        clusters = [[] for _ in range(self.K)]
        for idx, sample in enumerate(self.X):
            centroid_idx = self.centroid_mais_perto(sample, centroides)
            clusters[centroid_idx].append(idx)
        return clusters

    def centroid_mais_perto(self, sample, centroides):
        
        distances = [distancia_euclidiana(sample, point) for point in centroides]
        closest_index = np.argmin(distances)
        return closest_index

    def pegar_centroide(self, clusters):
        
        centroides = np.zeros((self.K, self.n_features))
        for cluster_idx, cluster in enumerate(clusters):
            cluster_mean = np.mean(self.X[cluster], axis=0)
            centroides[cluster_idx] = cluster_mean
        return centroides

    def sao_iguais(self, centroides_antigos, centroides):
        
        distances = [
            distancia_euclidiana(centroides_antigos[i], centroides[i]) for i in range(self.K)
        ]
        return sum(distances) == 0
k = KMeans(K=2, interacoes_maximas=150)
y_pred = k.prever(x_iris)
df = pd.DataFrame(k.centroides, columns=['sepal_length',' sepal_width','petal_length','petal_width'])
print("Valor dos centroides com K=2")
print(df)
k = KMeans(K=3, interacoes_maximas=150)
y_pred = k.prever(x_iris)
df = pd.DataFrame(k.centroides, columns=['sepal_length',' sepal_width','petal_length','petal_width'])

def estatistica(y_true,y_pred):
    acuracia = len([y_true[i] for i in range(len(y_pred)) if y_true[i]==y_pred[i]])/len(y_pred)
print("\n")
print("Valor dos centroides com K=3")

print(df)
print("\n agora vamos calcular os centroides de cada conjunto de dados separadamente! Primeiro o centroide da setosa, depois o centroide da virginica e depois da versicolor!")

def colocar_ordem(iris):
    x_setosa=[]
    x_virginica=[]
    x_versicolor=[]
    for array in iris:
        array=list(array)
        if array[4]=="Iris-setosa":
            x_setosa.append(array[0:4])
        elif array[4]=="Iris-virginica":
            x_virginica.append(array[0:4])
        elif array[4]=="Iris-versicolor":
            x_versicolor.append(array[0:4])
    return [np.array(x_setosa),np.array(x_virginica),np.array(x_versicolor)]

listas=colocar_ordem(iris)
for array in listas:
    k = KMeans(K=1, interacoes_maximas=150)
    y_pred = k.prever(array)
    print(k.centroides)

   


