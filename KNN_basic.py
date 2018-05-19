import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from scipy.spatial import Voronoi, voronoi_plot_2d

style.use('fivethirtyeight')

data={'dog':[[13,4],[19,10],[12,5],[1,1],[16,17],[33,9]],
      'cat': [[30, 40], [22, 52], [45, 50], [50, 34], [43, 44], [44, 33]]}




def eucliDist(p1,p2):
    return np.linalg.norm(np.array(p1)-np.array(p2))



def knn(data,k=3):
    x=34#input('enter x ')
    y =56 #input('enter y ')
    pre=[[x,y]]

    if len(data)>=k:
        print("no!!!!")
        quit()
    else:
        final={}
        final['dog']=[eucliDist(j,pre) for j in data['dog']]
        final['cat'] = [eucliDist(j, pre) for j in data['cat']]

        sorted(final)
        print(final)

        print(min(final, key=final.get))

        for i in data:
            for j in data[i]:
                plt.scatter(j[0],j[1],color=['b' if i=='dog' else 'g'])
        plt.scatter(x,y,color='r')

        plt.show()


knn(data)
