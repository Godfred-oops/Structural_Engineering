# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 16:12:32 2022

@author: Quophi_ababio
"""
import numpy as np 
import math 

span_num = int(input("Specify the number of span in the continuous beam: "))

while span_num < 1 or span_num > 3:
    span_num = int(input("Specify the number of spans either 1, 2 or 3: "))


support_x_position_list, support_type_list = [], []
Point_list, angle_list, Point_x_cord= [], [], []
Distributed_1_list, Distributed_1_x_cord = [], []
loading_types = []
span_length_list = []
rigidities = []


for x in range(span_num):
    
    span_length = float(input("Specify the span length for the beam - span " + str(x)+ ": "))
    span_length_list.append(span_length)

    #support positions  
    support_num = 2
    supports = ['fixed', 'pin', 'roller']
    
    for s in range(support_num): 
        support_type = input("Specify support type for support " + str(s) + 
                             " (fixed, pin, roller) for span " + str(x) + ": ")
        while support_type not in supports:
            support_type = input("Please Specify support type (fixed, pin, roller) " 
                                 "for support " + str(s) + " for span " + str(x) + ": ")
        support_x_position = float(input("Specify the x_coordinate for support "+ str(s)+ " for span " + str(x) +": "))
        support_x_position_list.append(support_x_position)
        support_type_list.append(support_type)
             
    
    rigidity = float(input("Specifiy the rigidity for span " + str(x) + ": "))
    rigidities.append(rigidity)
    
    #loadings 
    loading_num = int(input("Specify the number of loading cases for span " + str(x) +": "))
    
    loadings = ["Point_load","Distributed"]
    for l in range(loading_num):
        loading_type = input("Specify the loading type " + str(l) + 
                             " (Point_load, Distributed) for span " + str(x) +": ")
        while loading_type not in loadings:
            loading_type = input("Please Specify (Point_load or Distributed) "
                                 " for the loading type " + str(l) + " for span " + str(x) +" : ")
        loading_types.append(loading_type)
        if (loading_type == "Point_load"):
            Point_load_1 = float(input("Specify the point load for span " + str(x) +": "))
            angle = float(input("Specify the angle of inclination, if vertical, angle = 90, for span " + str(x) +": "))
            x_cord_load = float(input("Specify the x_coordinate for the point load " + 
                                      str(l) + " for span " + str(x) +": " ))
            if span_num == 2:
                
                if (loading_type == ["Point_load"]):
                    Distributed_1_list.append(0)
                    Distributed_1_x_cord.append(0)
            
            elif span_num == 3:
                if (loading_num == 1 and loading_type == "Point_load"):
                    Distributed_1_list.append(0)
                    Distributed_1_x_cord.append(0)
                elif loading_num == 2:
                    pass
                    
            Point_list.append(Point_load_1)
            angle_list.append(angle)
            Point_x_cord.append(x_cord_load)
        elif (loading_type == "Distributed"): 
            Distributed_1 = float(input("Specify the Distributed load for span " + str(x) +": "))
            x_cord_distributed = float(input("Specify the x_coordinate for the distributed load " + 
                                      str(l) + " for span " + str(x) +": " ))
            if span_num == 2:
                
                if (loading_num == 1 and loading_type == "Distributed"):
                    Point_list.append(0)
                    angle_list.append(0)
                    Point_x_cord.append(0)
                else:
                    pass
            elif span_num == 3:
                if (loading_num ==1 and loading_type == "Distributed"):
                    Point_list.append(0)
                    angle_list.append(0)
                    Point_x_cord.append(0)
                elif loading_num == 2:
                    pass
            
            Distributed_1_list.append(Distributed_1)
            Distributed_1_x_cord.append(x_cord_distributed)

#overhang computations 
overhang_answers = ['Yes', 'No']
overhang_loading_answers = ['Point_load', 'moment', 'Distributed','combined']
overhang_check = input("Is there an overhang in the continuous beam-(Yes or No): ")
while overhang_check not in overhang_answers:
    overhang_check = input("Please specify (Yes or No) for the presence of free end in the beam: ")

overhang_load_list = []
overhang_moment_list = []
overhang_udl_list = []
if overhang_check == "Yes":
    overhang_loadings = input("Specify the type of load at the free end-(Point_load, moment, Distributed, combined): ")
    while overhang_loadings not in overhang_loading_answers:
        overhang_loadings = input("Please specify (Point_load, moment or combined) at the free end of the beam: ")
    if overhang_loadings == 'Point_load':
        overhang_load = float(input("Specify the load on the free end: "))
        overhang_length = float(input("Specify the distance of the load on the free end: "))
    elif overhang_loadings == 'moment':
        overhang_moment = float(input("specify the moment at the free end clockwise (-), anticlockwise (+): "))
    elif overhang_loadings == 'Distributed':
        overhang_udl = float(input("Specify the load intensity on the free end: "))
        overhang_udl_length = float(input("Specify the length of the free end: "))
    elif overhang_loadings == 'combined':
        overhang_combinations = input("Specify the number of load combinations on the free end: ")
        
        for h in range(int(overhang_combinations)):
            overhang_cases = input("Specify the load cases " + str(h) + " on the free end -(Point_load, moment, Distributed): ")
            if overhang_cases == 'Point_load':
                overhang_load = float(input("Specify the load on the free end: "))
                overhang_length = float(input("Specify the distance of the load on the free end: "))
                overhang_load_list.append(overhang_load)
                overhang_load_list.append(overhang_length)
            elif overhang_cases == 'Distributed':
                overhang_udl = float(input("Specify the load intensity on the free end: "))
                overhang_udl_length = float(input("Specify the length of the load intensity on the free end: "))
                overhang_udl_list.append(overhang_udl)
                overhang_udl_list.append(overhang_udl_length)
            elif overhang_cases == 'moment':
                overhang_moment = float(input("specify the moment at the free end clockwise (-), anticlockwise (+): "))
                overhang_moment_list.append(overhang_moment)
        
else:
    
    pass

#storing the input values in a form of matrix
from itertools import zip_longest

a = zip_longest(Point_list, angle_list, Point_x_cord, 
                         Distributed_1_list, Distributed_1_x_cord,
                         span_length_list,rigidities ,  
                         fillvalue = 0)
e = 7   #number of parameter for point load and distributed loading
    

t = list(a)

force_matrix = []
for x in t:
    for y in x:
        force_matrix.append(y)
            

n = len(force_matrix)/e
forces_matrix = np.array(force_matrix).reshape(int(n),e)
print(forces_matrix, "\n")


        
#moment calculations
if span_num == 1:
        span_moment_1 = (2/3 * forces_matrix[0][5]*forces_matrix[0][3]*(forces_matrix[0][5] ** 3))/16 + ((
            0.5*forces_matrix[0][5]*forces_matrix[0][0]*np.sin(np.radians(forces_matrix[0][1]))*(forces_matrix[0][2]* (forces_matrix[0][5] - forces_matrix[0][2])))*(
                2*(forces_matrix[0][5] - forces_matrix[0][2]) + forces_matrix[0][2])) / (3*forces_matrix[0][5])
        
        span_1_moment_1 = (2/3 * forces_matrix[0][5]*forces_matrix[0][3]*(forces_matrix[0][5] ** 3))/16 + ((
            0.5*forces_matrix[0][5]*forces_matrix[0][0]*np.sin(np.radians(forces_matrix[0][1]))*(forces_matrix[0][2]* (forces_matrix[0][5] - forces_matrix[0][2])))*(
                2*(forces_matrix[0][2]) + (forces_matrix[0][5] -forces_matrix[0][2]))) / (3*forces_matrix[0][5])        
                
        if support_type_list == ['fixed', 'fixed']:
            
            moments_matrix = np.array([[(2*forces_matrix[0][5]/forces_matrix[0][6]), (forces_matrix[0][5]/forces_matrix[0][6])],
                                      [(forces_matrix[0][5]/forces_matrix[0][6]), 2*(forces_matrix[0][5]/forces_matrix[0][6])]])
            
            equation1_0_y = -6*((-span_moment_1/(forces_matrix[0][5]*forces_matrix[0][6])))
            
            equation2_0_y = -6*((-span_1_moment_1/(forces_matrix[0][5]*forces_matrix[0][6])))
            
            y_0_component = np.array([equation1_0_y, equation2_0_y])
            
            [m1,m2] = np.matmul(np.linalg.inv(moments_matrix), y_0_component)
            
        elif [i == "fixed" or "pin" or "roller" for i in support_type_list]:
            if overhang_check == 'Yes':
                if overhang_loadings == 'Point_load':
                    m2 = overhang_load * overhang_length
                elif overhang_loadings == 'moment':
                    m2 = overhang_moment
                elif overhang_loadings == 'Distributed':
                    m2 = (overhang_udl* (overhang_udl_length**2))/2
                elif overhang_loadings == 'combined':
                    moment_moment = sum(overhang_moment_list)
                    if overhang_load_list !=[] or overhang_moment_list != [] or overhang_udl_list != []:
                        load_moment = 0
                        for t in range(len(overhang_load_list)):
                            if t % 2 == 0:
                                load_moment = load_moment + overhang_load_list[t]* overhang_load_list[t+1]
                        udl_moment = 0
                        for p in range(len(overhang_udl_list)):
                            if  p % 2 == 0:
                                udl_moment = udl_moment + ( overhang_udl_list[p]* (overhang_udl_list[p+1] ** 2))/2
                    else:
                        load_moment = 0
                        udl_moment = 0
                        moment_moment = 0
                    m2 = load_moment + udl_moment + moment_moment
            else:
                m2 = 0
        
            equation1_0_y = -6*((-span_moment_1/(forces_matrix[0][5]*forces_matrix[0][6])))
        
        
            m1 = (equation1_0_y - (forces_matrix[0][5]*m2)/forces_matrix[0][6])/(2*forces_matrix[0][5])
            
            
if span_num == 2:
    span_moment_list = []
    span_1_moment_list = []
    for k in range(len(forces_matrix)):
        span_moment = (2/3 * forces_matrix[k][5]*forces_matrix[k][3]*(forces_matrix[k][5] ** 3))/16 + ((
            0.5*forces_matrix[k][5]*forces_matrix[k][0]*np.sin(np.radians(forces_matrix[k][1]))*(forces_matrix[k][2]* (forces_matrix[k][5] - forces_matrix[k][2])))*(
                2*(forces_matrix[k][5] - forces_matrix[k][2]) + forces_matrix[k][2])) / (3*forces_matrix[k][5])
        
        span_1_moment = (2/3 * forces_matrix[k][5]*forces_matrix[k][3]*(forces_matrix[k][5] ** 3))/16 + ((
            0.5*forces_matrix[k][5]*forces_matrix[k][0]*np.sin(np.radians(forces_matrix[k][1]))*(forces_matrix[k][2]* (forces_matrix[k][5] - forces_matrix[k][2])))*(
                2*(forces_matrix[k][2]) + (forces_matrix[k][5] -forces_matrix[k][2]))) / (3*forces_matrix[k][5])        
        span_moment_list.append(span_moment)
        span_1_moment_list.append(span_1_moment)
    if "fixed" not in support_type_list:
        m1 = 0
        if overhang_check == 'Yes':
            if overhang_loadings == 'Point_load':
                m3 = overhang_load * overhang_length
            elif overhang_loadings == 'moment':
                m3 = overhang_moment
            elif overhang_loadings == 'Distributed':
                m3 = (overhang_udl* (overhang_udl_length**2))/2
            elif overhang_loadings == 'combined':
                moment_moment = sum(overhang_moment_list)
                if overhang_load_list !=[] or overhang_moment_list != [] or overhang_udl_list != []:
                    load_moment = 0
                    for t in range(len(overhang_load_list)):
                        if t % 2 == 0:
                            load_moment = load_moment + overhang_load_list[t]* overhang_load_list[t+1]
                    udl_moment = 0
                    for p in range(len(overhang_udl_list)):
                        if  p % 2 == 0:
                            udl_moment = udl_moment + ( overhang_udl_list[p]* (overhang_udl_list[p+1] ** 2))/2
                else:
                    load_moment = 0
                    udl_moment = 0
                    moment_moment = 0
                m3 = load_moment + udl_moment + moment_moment
        else:
            m3 = 0
        m2 = (-6*((-span_1_moment_list[0]/(forces_matrix[0][5]*forces_matrix[0][6]))+ (-span_moment_list[1]/(forces_matrix[1][5]*forces_matrix[1][6])))+(-m3*forces_matrix[1][5]/(forces_matrix[1][5])))/(
            2*((forces_matrix[0][5]/forces_matrix[0][6]) + (forces_matrix[1][5]/forces_matrix[1][6])))
    
    else:
        if overhang_check == 'Yes':
            if overhang_loadings == 'Point_load':
                m3 = overhang_load * overhang_length
            elif overhang_loadings == 'moment':
                m3 = overhang_moment
            elif overhang_loadings == 'Distributed':
                m3 = (overhang_udl* (overhang_udl_length**2))/2
            elif overhang_loadings == 'combined':
                moment_moment = sum(overhang_moment_list)
                if overhang_load_list !=[] or overhang_moment_list != [] or overhang_udl_list != []:
                    load_moment = 0
                    for t in range(len(overhang_load_list)):
                        if t % 2 == 0:
                            load_moment = load_moment + overhang_load_list[t]* overhang_load_list[t+1]
                    udl_moment = 0
                    for p in range(len(overhang_udl_list)):
                        if  p % 2 == 0:
                            udl_moment = udl_moment + ( overhang_udl_list[p]* (overhang_udl_list[p+1] ** 2))/2
                else:
                    load_moment = 0
                    udl_moment = 0
                    moment_moment = 0
                m3 = load_moment + udl_moment + moment_moment
        else:
            m3 = 0 
        moment_matrix = np.array([[(2*forces_matrix[0][5]/forces_matrix[0][6]), (forces_matrix[0][5]/forces_matrix[0][6])],
                                  [(forces_matrix[0][5]/forces_matrix[0][6]), 2*((forces_matrix[0][5]/forces_matrix[0][6])+(forces_matrix[1][5]/forces_matrix[1][6]))]])
        
        
        span_moment_list_2 = [0, span_moment_list[0]]
        
        equation1_y = -6*((-span_moment_list_2[0]/(forces_matrix[0][5]*forces_matrix[0][6])) + (
            -span_moment_list_2[1]/(forces_matrix[0][5]*forces_matrix[0][6])))
        
        equation2_y = -6*((-span_1_moment_list[0]/(forces_matrix[0][5]*forces_matrix[0][6])) + (
            -span_moment_list[1]/(forces_matrix[1][5]*forces_matrix[1][6])))+(-m3*forces_matrix[1][5]/forces_matrix[1][6])
        
        y_component = np.array([equation1_y, equation2_y])
        
        [m1,m2] = np.matmul(np.linalg.inv(moment_matrix), y_component)

if span_num == 3:
     span_3_moment_list = []
     span_3_moment_list_0 = []
     for j in range(len(forces_matrix)):
         span_3_moment = (2/3 * forces_matrix[j][5]*forces_matrix[j][3]*(forces_matrix[j][5] ** 3))/16 + ((
             0.5*forces_matrix[j][5]*forces_matrix[j][0]*np.sin(np.radians(forces_matrix[j][1]))*(forces_matrix[j][2]* (forces_matrix[j][5] - forces_matrix[j][2])))*(
                 2*(forces_matrix[j][5] - forces_matrix[j][2]) + forces_matrix[j][2])) / (3*forces_matrix[j][5])
         
         span_3_moment_0 = (2/3 * forces_matrix[j][5]*forces_matrix[j][3]*(forces_matrix[j][5] ** 3))/16 + ((
             0.5*forces_matrix[j][5]*forces_matrix[j][0]*np.sin(np.radians(forces_matrix[j][1]))*(forces_matrix[j][2]* (forces_matrix[j][5] - forces_matrix[j][2])))*(
                 2*(forces_matrix[j][2]) + (forces_matrix[j][5] - forces_matrix[j][2]))) / (3*forces_matrix[j][5])       
         span_3_moment_list.append(span_3_moment) 
         span_3_moment_list_0.append(span_3_moment_0)
    
    
    
     if "fixed" not in support_type_list:
         m1 = 0
         if overhang_check == 'Yes':
             if overhang_loadings == 'Point_load':
                 m4 = overhang_load * overhang_length
             elif overhang_loadings == 'moment':
                m4 = overhang_moment
             elif overhang_loadings == 'Distributed':
                m4 = (overhang_udl* (overhang_udl_length**2))/2
             elif overhang_loadings == 'combined':
                 moment_moment = sum(overhang_moment_list)
                 if overhang_load_list !=[] or overhang_moment_list != [] or overhang_udl_list != []:
                     load_moment = 0
                     for t in range(len(overhang_load_list)):
                         if t % 2 == 0:
                             load_moment = load_moment + overhang_load_list[t]* overhang_load_list[t+1]
                     udl_moment = 0
                     for p in range(len(overhang_udl_list)):
                         if  p % 2 == 0:
                             udl_moment = udl_moment + ( overhang_udl_list[p]* (overhang_udl_list[p+1] ** 2))/2
                 else:
                     load_moment = 0
                     udl_moment = 0
                     moment_moment = 0
                 m4= load_moment + udl_moment + moment_moment
         else:    
             m4 = 0
         moment_3_matrix = np.array([[2*((forces_matrix[0][5]/forces_matrix[0][6])+(forces_matrix[1][5]/forces_matrix[1][6])), forces_matrix[1][5]/forces_matrix[1][6]],
                                   [forces_matrix[1][5]/forces_matrix[1][6], 2*((forces_matrix[1][5]/forces_matrix[1][6])+(forces_matrix[2][5]/forces_matrix[2][6]))]])
         
         equation1_3_y = -6*((-span_3_moment_list_0[0]/(forces_matrix[0][5]*forces_matrix[0][6])) + (
             -span_3_moment_list[1]/(forces_matrix[1][5]*forces_matrix[1][6])))
         
         equation2_3_y = -6*((-span_3_moment_list_0[1]/(forces_matrix[1][5]*forces_matrix[1][6])) + (
             -span_3_moment_list[2]/(forces_matrix[2][5]*forces_matrix[2][6])))+(-m4*forces_matrix[2][5]/forces_matrix[2][6])
         
         y_3_component = np.array([equation1_3_y, equation2_3_y])
         
         [m2,m3] = np.matmul(np.linalg.inv(moment_3_matrix), y_3_component)
    
        
        
         
         
         
         
      
        
    
    

        
    
    
    
        

