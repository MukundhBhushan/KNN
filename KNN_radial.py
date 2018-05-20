import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

data={'dog':[[13,4],[19,10],[12,5],[1,1],[16,17],[33,9]],
      'cat': [[30, 40], [22, 52], [45, 50], [50, 34], [43, 44], [44, 33]]}




def eucliDist(p1,p2):
    return np.linalg.norm(np.array(p1)-np.array(p2))

def data_plot():
    for i in data:
        for j in data[i]:
            plt.scatter(j[0], j[1], color=['b' if i == 'dog' else 'g'])

def draw_cicle(x,y,r):
    circle = plt.Circle((x, y), radius=r, color='red', fill=False)
    ax = plt.gca()
    ax.add_patch(circle)



def knn(data,k=3):

    x,y=int(input('enter the value of x ')),int(input('enter the value y '))
    r=0
    pre=[[x,y]]

    if len(data)>=k:
        print("no!!!!")
        quit()
    else:

        final = {}
        final['dog'] = [[eucliDist(j, pre), j] for j in data['dog']]
        final['cat'] = [[eucliDist(j, pre), j] for j in data['cat']]

        final['dog']=sorted(final['dog'])
        final['cat'] = sorted(final['cat'])



        print(final)
        __knn=min(final, key=final.get)


        print(final[__knn][0][1])

        min_point=final[__knn][0][1]

        def plt_s():
            return(plt.draw())

        while r<=eucliDist(min_point,pre)+0.1:
            plt.clf()
            data_plot()
            plt.scatter(x, y, color='r')
            if r>eucliDist(min_point,pre):
                plt.scatter(min_point[0], min_point[1], color='r')

            draw_cicle(x,y,r)
            plt_s()
            plt.pause(0.0000005)

            r +=0.1
        plt.show(plt_s())


knn(data)
