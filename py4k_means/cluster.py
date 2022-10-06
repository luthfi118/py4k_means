import numpy as np
import pandas as pd
class k_means:
    def __init__(self):
        pass
    def __init_centroid(self,x,k):
        minx=x.min()
        maxx=x.max()
        self.__centroid=np.array([np.random.uniform(minx,maxx,len(x[0])) for i in range(k)])
        self.__check=False

    def __distance(self,x,k):
        self.__cluster=[[] for i in range(k)]
        for i in range(len(x)):
            dist=[]
            for j in range(len(self.__centroid)):
                dist.append(np.linalg.norm(self.__centroid[j]-x[i]))
            mindis=min(dist)
            self.__cluster[dist.index(mindis)].append(i)

    def __update(self,x):
        prev_centroid=self.__centroid.copy()
        clustered_data=[]
        for i in range(len(self.__cluster)):
            clustered_data.append([])
            for j in self.__cluster[i]:
                clustered_data[i].append(x[j])
            clustered_data[i]=np.array(clustered_data[i])
        for i in range(len(self.__centroid)):
            self.__centroid[i]=clustered_data[i].mean(0)
        temp=np.zeros(len(self.__centroid))
        for i in range(len(self.__centroid)):
            temp[i]=np.linalg.norm(prev_centroid[i]-self.__centroid[i])
        if(temp.sum()==0):
            self.__check=True

    def __label(self,x):
        label=np.zeros(len(x))
        for i in range(len(x)):
            for j in range(len(self.__cluster)):
                try:
                    self.__cluster[j].index(i)
                    label[i]=j
                except:
                    pass
        #temp=pd.DataFrame(x,columns=['x'+str(i) for i in range(len(x[0]))])
        #temp['label']=label
        print(label)
        label = label.reshape(len(label),1)
        x = np.append(x,label,axis=1)
        return x

    def cluster(self,x,k,max_iter=20):
        x=np.array(x)
        self.__init_centroid(x,k)
        i=0
        while(not self.__check):
            self.__distance(x,k)
            self.__update(x)
            i=i+1
            if(i==max_iter):
                break
        return self.__label(x)

    def predict(self,x):
        x = x.reshape(1,len(x))
        for i in range(len(x)):
            dist=[]
            for j in range(len(self.__centroid)):
                dist.append(np.linalg.norm(self.__centroid[j]-x[i]))
            mindis=min(dist)
            print(mindis)
        return dist.index(mindis)

import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
#x = [np.random.uniform(-5,5 ,2) for i in range(500)]
x,_ = make_moons(n_samples=1000)
km = k_means()
y = km.cluster(x,2,20)

plt.scatter(y[:,0],y[:,1],c=y[:,2],cmap='rainbow')
plt.show()
