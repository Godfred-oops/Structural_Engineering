# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 17:25:08 2022

@author: Quophi_ababio
"""
import numpy as np 
import math 

#node positions 
node_num = int(input("Specify the number of nodes: "))

while node_num <= 1:
    node_num = int(input("Specify number of nodes greater than 1: "))

node_x_list = []
for n in range(node_num):
    x_cord = float(input("Specify the x_coordinate for node " + str(n) + ": " ))
    node_x_list.append(x_cord)
    

#support positions 
support_num = int(input("Specify the number of supports: "))

support_x_position_list, support_type_list = [], []

supports = ['fixed', 'pin', 'roller', 'internal_hinge']

for s in range(support_num): 
    support_type = input("Specify support type for support " + str(s) + 
                         " (fixed, pin, roller, internal_hinge): ")
    while support_type not in supports:
        support_type = input("Please Specify support type (fixed, pin, roller, internal_hinge) " 
                             "for support " + str(s) + " : ")
    support_x_position = float(input("Specify the x_coordinate for support "+ str(s)+ ": "))
    support_x_position_list.append(support_x_position)
    support_type_list.append(support_type)

    
#moments on the beam
moment_num = int(input("Specify the number of additional moments: "))

moment_value_list, moment_x_position_list = [], []

for m in range(moment_num): 
    moment_value = float(input("Specify the moment clockwise (+), anticlockwise (-) " + str(m) + ": "))
    moment_x_position = float(input("Specify the x_coordinate for moment " + str(m) + ": "))
    moment_value_list.append(moment_value)
    moment_x_position_list.append(moment_x_position)             
    
#loadings 
loading_num = int(input("Specify the number of loading cases: "))

Point_list, angle_list, Point_x_cord= [], [], []
Distributed_1_list, Distributed_1_x_cord = [], []
Distributed_2_list, Distributed_2_x_cord = [], []

loadings = ["Point_load","Distributed"]
loading_types = []
for l in range(loading_num):
    loading_type = input("Specify the loading type " + str(l) + 
                         " (Point_load, Distributed): ")
    while loading_type not in loadings:
        loading_type = input("Please Specify (Point_load or Distributed) "
                             " for the loading type " + str(l) + " : ")
    loading_types.append(loading_type)
    if (loading_type == "Point_load"):
        Point_load_1 = float(input("Specify the point load: "))
        angle = float(input("Specify the angle of inclination, if vertical, angle = 90: "))
        x_cord_load = float(input("Specify the x_coordinate for the point load " + 
                                  str(l) + ": " ))
        Point_list.append(Point_load_1)
        angle_list.append(angle)
        Point_x_cord.append(x_cord_load)
    elif (loading_type == "Distributed"): 
        Distributed_1 = float(input("Specify the Distributed load (P1): "))
        x_cord_distributed = float(input("Specify the x_coordinate for the distributed load " + 
                                  str(l) + "(P1): " ))
        Distributed_1_list.append(Distributed_1)
        Distributed_1_x_cord.append(x_cord_distributed)
    
        Distributed_2 = float(input("Specify the Distributed load (P2): "))
        x_cord_distributed_1=float(input("Specify the x_coordinate for the distributed load " + 
                                  str(l) + " (P2): " ))
        Distributed_2_list.append(Distributed_2)
        Distributed_2_x_cord.append(x_cord_distributed_1)
        
Distributed_list = Distributed_1_list + Distributed_2_list
Distributed_x_cord = Distributed_1_x_cord + Distributed_2_x_cord


#storing the input values in a form of matrix
from itertools import zip_longest

a = zip_longest(Point_list, angle_list, Point_x_cord, 
                         Distributed_list, Distributed_x_cord,
                         support_x_position_list, 
                         node_x_list,  
                         moment_value_list, moment_x_position_list, 
                         fillvalue = 0)
e = 9    #number of parameter for point load and distributed loading
    

t = list(a)

force_matrix = []
for x in t:
    for y in x:
        force_matrix.append(y)
            

n = len(force_matrix)/e
forces_matrix = np.array(force_matrix).reshape(int(n),e)
print(forces_matrix)


#forces and moment calculations 
# fixed support with uniformly distributed load and point loads

if support_type_list == ['fixed']:
    moment1_list = []
    vertical_list = []
    horizontal_list = []
    Distributed_moment, centroid_moment, distance_moment = [], [], []
    for f in range(len(forces_matrix)):
        moment1 = -forces_matrix[:,0][f] * (forces_matrix[:,2][f] - 
                                           forces_matrix[:,5][0]) * np.sin(np.radians(forces_matrix[:,1][f])) 
        
        """
        moment2 = -forces_matrix[:,4][0] * (0.5* (forces_matrix[:,4][1] - forces_matrix[:,4][0]) +
                                            forces_matrix[:,4][0]-forces_matrix[:,5][0]) * (
                                                forces_matrix[:,4][1]-forces_matrix[:,4][0]) 
        """
        if f % 2 == 0: 
            dm = forces_matrix[:,3][f] + forces_matrix[:,3][f+1]
            cm = -forces_matrix[:,4][f] + forces_matrix[:,4][f+1]
            dm_m = forces_matrix[:,4][f]
            Distributed_moment.append(dm)
            centroid_moment.append(cm)
            distance_moment.append(dm_m)
        elif f > len(forces_matrix):
            break 
        else:
            pass
        
        distance_moment_new = []
        for r in range(len(distance_moment)):
            zz = distance_moment[r] - forces_matrix[:,5][0]
            distance_moment_new.append(zz)
        
        Multiply_moment = np.multiply(0.5*np.array(Distributed_moment), np.array(centroid_moment))
        re = 0.5*np.array(centroid_moment) + np.array(distance_moment_new)
        fe = np.multiply(Multiply_moment, re)
                                                
        vertical_force_A_1 = -forces_matrix[:,0][f] * np.sin(np.radians(forces_matrix[:,1][f]))
        horizontal_force_A = -forces_matrix[:,0][f] * np.cos(np.radians(forces_matrix[:,1][f]))                                                   

        
        moment1_list.append(moment1)
        vertical_list.append(vertical_force_A_1)
        horizontal_list.append(horizontal_force_A)
        
        
    moment = sum(moment1_list) + -sum(fe) + sum(moment_value_list)
    vertical_1 = sum(vertical_list) + -sum(Multiply_moment)
    horizontal_force = sum(horizontal_list)
    vertical_force_B = 0.
    final_vector = np.array([moment, vertical_1, horizontal_force, vertical_force_B])
    print(final_vector)

elif [element == 'pin' and 'roller' for element in support_type_list]:
    p = 0
    vertical_force_list = []
    sum_vertical = []
    sum_horizontal = []
    Distributed_moment, centroid_moment, distance_moment = [], [], []
    for p in range(len(forces_matrix)):
        y = 1/(forces_matrix[:,5][1] - forces_matrix[:,5][0])
        moment1 =  y * (-forces_matrix[:,0][p] * np.sin(np.radians(forces_matrix[:,1][p]))) * (forces_matrix[:,2][p] - 
                                               forces_matrix[:,5][0]) 
                                                        
        """
        moment2  = y * (-forces_matrix[:,3][0] * (0.5* (forces_matrix[:,4][1] - forces_matrix[:,4][0]) +
                                            forces_matrix[:,4][0]-forces_matrix[:,5][0]) * (
                                                forces_matrix[:,4][1]-forces_matrix[:,4][0]))
        """
        if p % 2 == 0: 
            dm = forces_matrix[:,3][p] + forces_matrix[:,3][p+1]
            cm = -forces_matrix[:,4][p] + forces_matrix[:,4][p+1]
            dm_m = forces_matrix[:,4][p]
            Distributed_moment.append(dm)
            centroid_moment.append(cm)
            distance_moment.append(dm_m)
        elif p > len(forces_matrix):
            break 
        else:
            pass
        
        distance_moment_new = []
        for r in range(len(distance_moment)):
            zz = distance_moment[r] - forces_matrix[:,5][0]
            distance_moment_new.append(zz)
        
        Multiply_moment = np.multiply(0.5*np.array(Distributed_moment), np.array(centroid_moment))
        re = 0.5*np.array(centroid_moment) + np.array(distance_moment_new)
        fe = -y * np.multiply(Multiply_moment, re)
        
        sum_of_vertical_forces = -forces_matrix[:,0][p] * np.sin(np.radians(forces_matrix[:,1][p]))
        
        horizontal_force_A = -forces_matrix[:,0][p] * np.cos(np.radians(forces_matrix[:,1][p]))
        p = p + 1
        
        vertical_force_list.append(moment1)
        sum_vertical.append(sum_of_vertical_forces)
        sum_horizontal.append(horizontal_force_A)
        
    vertical_force_B = sum(vertical_force_list) + sum(fe) + sum(moment_value_list)
    
    vertical_force_A = sum(sum_vertical) + -sum(Multiply_moment) - vertical_force_B
        
    horizontal_force = sum(sum_horizontal)
    
    final_vector = np.array([ vertical_force_A, horizontal_force,vertical_force_B])
    print(final_vector)
                                                                            
    