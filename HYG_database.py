# read HYG database
import csv
from math import sqrt
with open("hygxyz.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    data = [r for r in csv_reader]
print("Reading HYG formatted CSV file named 'hygxyz.csv'.")

# create two dictionaries which contain stars' coordinates and stars' ID and name
star_ID={}
star_Name={}
for index in range(len(data)):
    star_ID[(int(data[index]['StarID']))]=[float(data[index]['X']),float(data[index]['Y']),float(data[index]['Z'])]
    if not (data[index]['ProperName']==''):
        star_Name[(int(data[index]['StarID']))]=data[index]['ProperName']
        continue
    elif not (data[index]['BayerFlamsteed']==''):
        star_Name[(int(data[index]['StarID']))] = data[index]['BayerFlamsteed']
        continue
    elif not data[index]['Gliese']=='':
        star_Name[(int(data[index]['StarID']))] = "Gliese "+data[index]['Gliese']
        continue
    else:
        star_Name[(int(data[index]['StarID']))] = "Unnamed star "+data[index]['StarID']
# pre-screen the stars that is within a certain radius(10 parsecs) of our solar system
dist_from_sol={}
sol_10_parsec=[]
sol_10_parsec_no_sol=[]
for r in star_ID:
    dist_from_sol[r]=sqrt(star_ID[r][0]**2+star_ID[r][1]**2+star_ID[r][2]**2)
    if dist_from_sol[r]<=10:
        sol_10_parsec.append(r)
        if dist_from_sol[r]!=0:
            sol_10_parsec_no_sol.append(r)
print("Found %d stars within a radius of 10.0 parsecs from Sol."%len(sol_10_parsec))
# use the greedy algorithm to find a path to jump cross these pre-selected stars
sum_distance=0
next_starID=0
next_list=sol_10_parsec_no_sol
path_list=[]
print("Computing a star traversal using a greedy method.")
for count in range(len(sol_10_parsec_no_sol)):
    distance_min = 10000000
    path_list.append(next_starID)
    for star_ID_10parsec in next_list:
        distance_temp=sqrt((star_ID[star_ID_10parsec][0]-star_ID[next_starID][0])**2+(star_ID[star_ID_10parsec][1]-star_ID[next_starID][1])**2+(star_ID[star_ID_10parsec][2]-star_ID[next_starID][2])**2)
        if distance_min>distance_temp:
            distance_min=distance_temp
            next_starID_temp=star_ID_10parsec
    next_list_temp=[]
    for r in next_list:
        if r!=next_starID_temp:
            next_list_temp.append(r)
    next_list=[]
    next_list=next_list_temp
    sum_distance+=distance_min
    print("..",star_Name[next_starID],"->",star_Name[next_starID_temp],": distance = ",'%.2f'%distance_min,", total distance = "'%.2f'%sum_distance)
    next_starID=next_starID_temp
print("Total distance traversed is %.2f parsecs."%sum_distance)
path_list.append(next_starID)

# draw a 3D plot to show the path
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
x=[]
y=[]
z=[]
for index in path_list:
    x.append(star_ID[index][0])
    y.append(star_ID[index][1])
    z.append(star_ID[index][2])
ax.plot(x, y, z, label='the path of the traveral across the stars within 10 parsec from Sol',marker="o")
ax.legend()
ax.set_xlabel('X axis/ parsec')
ax.set_ylabel('Y axis/ parsec')
ax.set_zlabel('Z axis/ parsec')
plt.show()




