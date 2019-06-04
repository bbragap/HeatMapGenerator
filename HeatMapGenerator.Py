import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

fileName = input("Type the file name with .'txt': \n")

#Initializing the file reading
f = open(fileName, "r")
rmax = 10
rl = f.readlines()


#Define the mobile device dimensions
oldx = int(input("Enter the dimension of the horizontal axis: \n")) #720
oldy = int(input("Enter the dimension of the verical axis: \n")) #1280

#Define the Gesture
choose = input("Type what kind of gesture do you want to analyze: (Ex: Tap, Swipe, Scroll, Unidentified, TwoFingers, LongPress, All)")
aux_choose = choose

#Create de matrix used on the plot
matriz = np.zeros((70,145))
ntouchs = 0

#Reading each line and spliting on ';'
for i in range(len(rl)):
    line = rl[i].split(";")
    t = len(line)
    ntouchs = ntouchs + 1

    if (aux_choose == "All"):
        choose = line[0]

    if(line[0] == choose):

        #print(line)
        for j in range(2,t-2,2):

            if (line[j] != "null") and (line[j+1] != "null"):
                try:
                    #Resizing the Matrix
                    a = int((int(line[j])*70)/oldx)
                    b = int((int(line[j + 1])*145)/oldy)


                    r = 0
                    x = 0
                    EPSILON = 2.2

                    #Using the equation of the circle in the plane to normalize the plot
                    for r in range(0, rmax):
                        for x in range(a - r, a + r + 1):

                            y = int(b + np.sqrt(r ** 2 - (x - a) ** 2))
                            matriz[x][y] = matriz[x][y] + rmax - r

                            y = int(b - np.sqrt(r ** 2 - (x - int(a)) ** 2))
                            matriz[x][y] = matriz[x][y] + rmax - r

                except IndexError:
                    pass
                continue

print("Number of Touchs: ", ntouchs)
f.close()

fig = plt.figure(figsize=(5,10))
#Ploting the Heatmap
ax = sns.heatmap(matriz,cmap="jet",cbar=True,square=False, xticklabels=False,yticklabels=False)
ax.invert_yaxis()
ax.invert_xaxis()

plt.show()






