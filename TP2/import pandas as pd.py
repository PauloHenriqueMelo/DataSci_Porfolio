import pandas as pd
import numpy as np

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        # Compute distances between x and all examples in the training set
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        # Sort by distance and return indices of the first k neighbors
        k_idx = np.argsort(distances)[: self.k]
        # Extract the labels of the k nearest neighbor training samples
        k_neighbor_labels = [self.y_train[i] for i in k_idx]
        # return the most common class label
        most_common = Counter(k_neighbor_labels).most_common(1)
        return most_common[0][0]

  def estatistica(y_true,y_pred):
        
        accuracy = len([y_true[i] for i in range(len(y_pred)) if y_true[i]==y_pred[i]])/len(y_pred)
        
        precisao_setosa= len([y_pred[i] for i in range(len(y_pred)) if y_true[i]==y_pred[i] and y_pred[i]==0])/len([y_pred[i] for i in range(len(y_pred)) if y_pred[i]==0])
        precisao_virginica=len([y_pred[i] for i in range(len(y_pred)) if y_true[i]==y_pred[i] and y_pred[i]==1])/len([y_pred[i] for i in range(len(y_pred)) if y_pred[i]==1])
        precisao_versicolor= len([y_pred[i] for i in range(len(y_pred)) if y_true[i]==y_pred[i] and y_pred[i]==2])/len([y_pred[i] for i in range(len(y_pred)) if y_pred[i]==2])
        
        revocacao_setosa=len([y_pred[i] for i in range(len(y_pred)) if y_true[i]==y_pred[i] and y_pred[i]==0])/len([y_true[i] for i in range(len(y_pred)) if y_true[i]==0])
        revocacao_virginica=len([y_pred[i] for i in range(len(y_pred)) if y_true[i]==y_pred[i] and y_pred[i]==1])/len([y_true[i] for i in range(len(y_pred)) if y_true[i]==1])
        revocacao_versicolor=len([y_pred[i] for i in range(len(y_pred)) if y_true[i]==y_pred[i] and y_pred[i]==2])/len([y_true[i] for i in range(len(y_pred)) if y_true[i]==2])
        
        f1_setosa= 2* (precisao_setosa*revocacao_setosa)/(precisao_setosa+revocacao_setosa)
        f1_virginica=2* (precisao_virginica*revocacao_virginica)/(precisao_virginica+revocacao_virginica)
        f1_versicolor=2* (precisao_versicolor*revocacao_versicolor)/(precisao_versicolor+revocacao_versicolor)
        
        
        return accuracy, [[precisao_setosa, revocacao_setosa ,f1_setosa],[precisao_virginica, revocacao_virginica, f1_virginica],[precisao_versicolor, revocacao_versicolor,f1_versicolor]]

    def turnable(mylist):
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


x_teste= np.delete(teste, 4, 1)  # delete second column of C
x_treino= np.delete(treino, 4, 1)  # delete second column of C
x,y,z,t,s= teste.T
a,b,c,d,e= treino.T
y_teste=turnable(s)
y_treino=turnable(e)

k = 2
clf = KNN(k=k)
clf.fit(x_treino, y_treino)
predictions = clf.predict(x_teste)
predictions = list(predictions)
print("KNN classification accuracy", accuracy(y_teste, predictions))
acuracia, array = estatistica(y_teste,predictions)
print(array)

print("KNN com K=2")


df = pd.DataFrame(array, index =['iris setosa', 'iris virginica', 'iris versicolor'],
                                              columns=['precisao','revocacao','f1'])
df