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

    x,y=int(input('enter the value of x: ')),int(input('enter the value y: '))
    r=0
    pre=[[x,y]]

    if len(data)>=k:
        print("no!!!!")
        quit()
    else:

        final = {}
        final['dog'] = [[round(eucliDist(j, pre)), j] for j in data['dog']]
        final['cat'] = [[round(eucliDist(j, pre)), j] for j in data['cat']]

        final['dog']=sorted(final['dog'])
        final['cat'] = sorted(final['cat'])

        def bigpoint(x,y):
            plt.scatter(x,y, color='r', s=200)



        print(final)
        __knn=min(final, key=final.get)

        def plt_s():
            return (plt.draw())

        big_point=[]
        for i in range(k):
            min_point = final[__knn][i][1]
            big_point.append(min_point)
            print(big_point)

            while r <= eucliDist(min_point, pre) + 0.5:
                plt.clf()
                data_plot()
                plt.scatter(x, y, color='r')#ref point
                if r > eucliDist(min_point, pre):
                    bigpoint(min_point[0], min_point[1])

                draw_cicle(x, y, r)
                plt_s()
                plt.pause(0.000000001)

                r += 0.5

        for i in big_point:
            bigpoint(i[0],i[1])
            #print(i)
        plt.show(plt_s())


k=int(input('enter the value of k: '))
knn(data,k=k)
