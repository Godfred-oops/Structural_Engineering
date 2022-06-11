# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 16:12:32 2022

@author: Quophi_ababio
"""
import numpy as np 
import matplotlib.pyplot as plt
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
                
                if (loading_num == 1 and loading_type == "Point_load"):
                    Distributed_1_list.append(0)
                    Distributed_1_x_cord.append(0)
                elif loading_num == 2:
                    pass
            
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
            
            
            moments_list = [m1,m2]
            
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
            
            moments_list = [m1,m2]
            
        #Reactions calculations 
            
        Reaction_B =  (1/forces_matrix[0][5]) * ((-forces_matrix[0][0]*np.sin(np.radians(forces_matrix[0][1]))*forces_matrix[0][2])+ 
                                                 (-forces_matrix[0][3]*forces_matrix[0][4]*0.5*forces_matrix[0][4]) + m1 - m2)
        Reaction_A = -forces_matrix[0][0]*np.sin(np.radians(forces_matrix[0][1])) + (-forces_matrix[0][3]*forces_matrix[0][4]) - Reaction_B
                
        Reaction_C = 0
        
        Reactions_list = [Reaction_A, Reaction_B]
        
        if overhang_check == 'Yes':
            if overhang_loadings == 'Point_load':
                Reaction_C = -overhang_load 
            elif overhang_loadings == 'Distributed':
                Reaction_C = -overhang_udl* overhang_udl_length
            elif overhang_loadings == 'combined':
                
                if overhang_load_list !=[] or overhang_moment_list != [] or overhang_udl_list != []:
                    point_load = 0
                    for t in range(len(overhang_load_list)):
                        if t % 2 == 0:
                            point_load = point_load + overhang_load_list[t]
                    point_udl = 0
                    for p in range(len(overhang_udl_list)):
                        if  p % 2 == 0:
                            point_udl = point_udl + ( overhang_udl_list[p]* (overhang_udl_list[p+1]))
                else:
                    point_load = 0
                    point_udl = 0
                Reaction_C = -point_load + -point_udl 
            Reactions_list = [Reaction_A, Reaction_B, Reaction_C]
            
        #Shear forces diagram for 1-span 
        if forces_matrix[0][0] == 0:
            if overhang_check == "Yes":
                if overhang_loadings == 'Point_load':
                    plot_reaction_list = [Reaction_A,forces_matrix[0][3]*forces_matrix[0][4],Reaction_B+Reaction_C,0,-Reaction_C]
                    support_x_position_list.append(support_x_position_list[1] + overhang_length)
                    plot_length_list = np.repeat(support_x_position_list, 2)
                elif overhang_loadings == 'Distributed':
                    plot_reaction_list = [Reaction_A,forces_matrix[0][3]*forces_matrix[0][4],Reaction_B+Reaction_C,-Reaction_C]
                    support_x_position_list.append(support_x_position_list[1] + overhang_udl_length)
                    plot_length_list = np.repeat(support_x_position_list, 2)
                    plot_length_list = np.delete(plot_length_list,[len(plot_length_list)-1])
            else:
                plot_reaction_list = [Reaction_A,forces_matrix[0][3]*forces_matrix[0][4],Reaction_B+Reaction_C]
                plot_length_list = np.repeat(support_x_position_list, 2)
        elif forces_matrix[0][3] == 0:
            if overhang_check == "Yes":
                if overhang_loadings == 'Point_load':
                    plot_reaction_list = [Reaction_A,0,forces_matrix[0][0],0,Reaction_B+Reaction_C,0,-Reaction_C]
                    support_x_position_list.append(support_x_position_list[1] + overhang_length)
                    support_x_position_list.insert(1, forces_matrix[0][2])
                    plot_length_list = np.repeat(support_x_position_list, 2)
                elif overhang_loadings == 'Distributed':
                    plot_reaction_list = [Reaction_A,0,forces_matrix[0][0],0,Reaction_B+Reaction_C,-Reaction_C]
                    support_x_position_list.append(support_x_position_list[1] + overhang_udl_length)
                    support_x_position_list.insert(1, forces_matrix[0][2])
                    plot_length_list = np.repeat(support_x_position_list, 2)
                    plot_length_list = np.delete(plot_length_list,[len(plot_length_list)-1])
                elif overhang_loadings == 'moment':
                    plot_reaction_list = [Reaction_A,0,forces_matrix[0][0],0,Reaction_B+Reaction_C]
                    support_x_position_list.insert(1, forces_matrix[0][2])
                    plot_length_list = np.repeat(support_x_position_list, 2)    
            else:
                plot_reaction_list = [Reaction_A,0,forces_matrix[0][0],0,Reaction_B+Reaction_C]
                support_x_position_list.insert(1, forces_matrix[0][2])
                plot_length_list = np.repeat(support_x_position_list, 2)
                
        else:
            if overhang_check == "Yes":
                if overhang_loadings == 'Point_load':
                    plot_reaction_list = [Reaction_A,forces_matrix[0][3]*forces_matrix[0][2],forces_matrix[0][0],forces_matrix[0][3]*(forces_matrix[0][5]-forces_matrix[0][2]),Reaction_B+Reaction_C,0,-Reaction_C]
                    support_x_position_list.append(support_x_position_list[1] + overhang_length)
                    support_x_position_list.insert(1, forces_matrix[0][2])
                    plot_length_list = np.repeat(support_x_position_list, 2)
                elif overhang_loadings == 'Distributed':
                    plot_reaction_list = [Reaction_A,forces_matrix[0][3]*forces_matrix[0][2],forces_matrix[0][0],forces_matrix[0][3]*(forces_matrix[0][5]-forces_matrix[0][2]),Reaction_B+Reaction_C,-Reaction_C]
                    support_x_position_list.append(support_x_position_list[1] + overhang_udl_length)
                    support_x_position_list.insert(1, forces_matrix[0][2])
                    plot_length_list = np.repeat(support_x_position_list, 2)
                    plot_length_list = np.delete(plot_length_list,[len(plot_length_list)-1])
                elif overhang_loadings == 'moment':
                    plot_reaction_list = [Reaction_A,forces_matrix[0][3]*forces_matrix[0][2],forces_matrix[0][0],forces_matrix[0][3]*(forces_matrix[0][5]-forces_matrix[0][2]),Reaction_B+Reaction_C]
                    support_x_position_list.insert(1, forces_matrix[0][2])
                    plot_length_list = np.repeat(support_x_position_list, 2)
            else:
                plot_reaction_list = [Reaction_A,forces_matrix[0][3]*forces_matrix[0][2],forces_matrix[0][0],forces_matrix[0][3]*(forces_matrix[0][5]-forces_matrix[0][2]),Reaction_B+Reaction_C]
                support_x_position_list.insert(1, forces_matrix[0][2])
                plot_length_list = np.repeat(support_x_position_list, 2)
        

        p = 0
        e = [p]

        for i in range(len(plot_reaction_list)):
            p = p + plot_reaction_list[i]
            e.append(p)

        print(e)
        plt.plot(plot_length_list,e)
        plt.title('SHEAR FORCE DIAGRAM')
        plt.xlabel('length')
        plt.ylabel('Shear force Values')
        if overhang_check == 'Yes':
            if overhang_loadings == 'Point_load':
                plt.plot([0,plot_length_list[-1]], [0,0])
            elif overhang_loadings == 'Distributed':
                plt.plot([0,plot_length_list[-1]], [0,0])
            elif overhang_loadings == 'moment':
                plt.plot([0,plot_length_list[-1]], [0,0])
        else:
            plt.plot([0,plot_length_list[-1]], [0,0])

        for a,d in zip(plot_length_list,e):
            plt.annotate(np.round(d,2), (a,d), horizontalalignment = 'left',
                             verticalalignment = 'top', fontsize = 9)
    
            
            
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
        m2 = (-6*((-span_1_moment_list[0]/(forces_matrix[0][5]*forces_matrix[0][6]))+ (-span_moment_list[1]/(forces_matrix[1][5]*forces_matrix[1][6])))+(-m3*forces_matrix[1][5]/(forces_matrix[1][6])))/(
            2*((forces_matrix[0][5]/forces_matrix[0][6]) + (forces_matrix[1][5]/forces_matrix[1][6])))

        moments_list = [m1,m2,-m2,m3]
    
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
        
        
        moments_list = [m1,m2,-m2,m3]
    
    #Reactions calculations
    Reaction_B =  (1/forces_matrix[0][5]) * ((-forces_matrix[0][0]*np.sin(np.radians(forces_matrix[0][1]))*forces_matrix[0][2])+ 
                                             (-forces_matrix[0][3]*forces_matrix[0][4]*0.5*forces_matrix[0][4]) + m1 - m2)
    Reaction_A = -forces_matrix[0][0]*np.sin(np.radians(forces_matrix[0][1])) + (-forces_matrix[0][3]*forces_matrix[0][4]) - Reaction_B
            
    Reactions_list = [Reaction_A, Reaction_B]
    
    Reaction_B_1 =  (1/forces_matrix[1][5]) * ((-forces_matrix[1][0]*np.sin(np.radians(forces_matrix[1][1]))*forces_matrix[1][2])+ 
                                             (-forces_matrix[1][3]*forces_matrix[1][4]*0.5*forces_matrix[1][4]) + m2 - m3)
    Reaction_A_1 = -forces_matrix[1][0]*np.sin(np.radians(forces_matrix[1][1])) + (-forces_matrix[1][3]*forces_matrix[1][4]) - Reaction_B_1
            
    Reaction_C = 0
    
    Reactions_list_1 = [Reaction_A_1, Reaction_B_1]
    
    if overhang_check == 'Yes':
        if overhang_loadings == 'Point_load':
            Reaction_C = -overhang_load 
        elif overhang_loadings == 'Distributed':
            Reaction_C = -overhang_udl* overhang_udl_length
        elif overhang_loadings == 'combined':
            
            if overhang_load_list !=[] or overhang_moment_list != [] or overhang_udl_list != []:
                point_load = 0
                for t in range(len(overhang_load_list)):
                    if t % 2 == 0:
                        point_load = point_load + overhang_load_list[t]
                point_udl = 0
                for p in range(len(overhang_udl_list)):
                    if  p % 2 == 0:
                        point_udl = point_udl + ( overhang_udl_list[p]* (overhang_udl_list[p+1]))
            else:
                point_load = 0
                point_udl = 0
            Reaction_C = -point_load + -point_udl 
        Reactions_list_1 = [Reaction_A_1, Reaction_B_1, Reaction_C]
    
    #Shear forces diagram for 2-spans 
    # for first span
    support_x_position_list_1 = support_x_position_list[0:2]
    support_x_position_list_2 = support_x_position_list[2:4]
    if forces_matrix[0][0] == 0:
         plot_reaction_list = [Reaction_A,forces_matrix[0][3]*forces_matrix[0][4],Reaction_B]
         plot_length_list = np.repeat(support_x_position_list_1, 2)
    elif forces_matrix[0][3] == 0:
        plot_reaction_list = [Reaction_A,0,forces_matrix[0][0],0,Reaction_B]
        support_x_position_list_1.insert(1, forces_matrix[0][2])
        plot_length_list = np.repeat(support_x_position_list_1, 2)        
    else:
         plot_reaction_list = [Reaction_A,forces_matrix[0][3]*forces_matrix[0][2],forces_matrix[0][0],forces_matrix[0][3]*(forces_matrix[0][5]-forces_matrix[0][2]),Reaction_B]
         support_x_position_list_1.insert(1, forces_matrix[0][2])
         plot_length_list = np.repeat(support_x_position_list_1, 2)
         
    # for second span 
    if forces_matrix[1][0] == 0:
        if overhang_check == "Yes":
            if overhang_loadings == 'Point_load':
                plot_reaction_list_1 = [Reaction_A_1,forces_matrix[1][3]*forces_matrix[1][4],Reaction_B_1+Reaction_C,0,-Reaction_C]
                support_x_position_list_2.append(support_x_position_list_2[1] + overhang_length)
                plot_length_list_1 = np.repeat(support_x_position_list_2, 2)
            elif overhang_loadings == 'Distributed':
                plot_reaction_list_1 = [Reaction_A_1,forces_matrix[1][3]*forces_matrix[1][4],Reaction_B_1+Reaction_C,-Reaction_C]
                support_x_position_list_2.append(support_x_position_list_2[1] + overhang_udl_length)
                plot_length_list_1 = np.repeat(support_x_position_list_2, 2)
                plot_length_list_1 = np.delete(plot_length_list_1,[len(plot_length_list_1)-1])
        else:
            plot_reaction_list_1 = [Reaction_A_1,forces_matrix[1][3]*forces_matrix[1][4],Reaction_B_1+Reaction_C]
            plot_length_list_1 = np.repeat(support_x_position_list_2, 2)
    elif forces_matrix[1][3] == 0:
        if overhang_check == "Yes":
            if overhang_loadings == 'Point_load':
                plot_reaction_list_1 = [Reaction_A_1,0,forces_matrix[1][0],0,Reaction_B_1+Reaction_C,0,-Reaction_C]
                support_x_position_list_2.append(support_x_position_list_2[1] + overhang_length)
                support_x_position_list_2.insert(1, forces_matrix[1][2])
                plot_length_list_1 = np.repeat(support_x_position_list_2, 2)
            elif overhang_loadings == 'Distributed':
                plot_reaction_list_1 = [Reaction_A_1,0,forces_matrix[1][0],0,Reaction_B_1+Reaction_C,-Reaction_C]
                support_x_position_list_2.append(support_x_position_list_2[1] + overhang_udl_length)
                support_x_position_list_2.insert(1, forces_matrix[1][2])
                plot_length_list_1 = np.repeat(support_x_position_list_2, 2)
                plot_length_list_1 = np.delete(plot_length_list_1,[len(plot_length_list_1)-1])
            elif overhang_loadings == 'moment':
                plot_reaction_list_1 = [Reaction_A_1,0,forces_matrix[1][0],0,Reaction_B_1+Reaction_C]
                support_x_position_list_2.insert(1, forces_matrix[1][2])
                plot_length_list_1 = np.repeat(support_x_position_list_2, 2)    
        else:
            plot_reaction_list_1 = [Reaction_A_1,0,forces_matrix[1][0],0,Reaction_B_1+Reaction_C]
            support_x_position_list_2.insert(1, forces_matrix[1][2])
            plot_length_list_1 = np.repeat(support_x_position_list_2, 2)
            
    else:
        if overhang_check == "Yes":
            if overhang_loadings == 'Point_load':
                plot_reaction_list_1 = [Reaction_A_1,forces_matrix[1][3]*forces_matrix[1][2],forces_matrix[1][0],forces_matrix[1][3]*(forces_matrix[1][5]-forces_matrix[1][2]),Reaction_B_1+Reaction_C,0,-Reaction_C]
                support_x_position_list_2.append(support_x_position_list_2[1] + overhang_length)
                support_x_position_list_2.insert(1, forces_matrix[1][2] + support_x_position_list[1])
                plot_length_list_1 = np.repeat(support_x_position_list_2, 2)
            elif overhang_loadings == 'Distributed':
                plot_reaction_list_1 = [Reaction_A_1,forces_matrix[1][3]*forces_matrix[1][2],forces_matrix[1][0],forces_matrix[1][3]*(forces_matrix[1][5]-forces_matrix[1][2]),Reaction_B_1+Reaction_C,-Reaction_C]
                support_x_position_list_2.append(support_x_position_list_2[1] + overhang_udl_length)
                support_x_position_list_2.insert(1, forces_matrix[1][2] + support_x_position_list[1])
                plot_length_list_1 = np.repeat(support_x_position_list_2, 2)
                plot_length_list_1 = np.delete(plot_length_list_1,[len(plot_length_list_1)-1])
            elif overhang_loadings == 'moment':
                plot_reaction_list_1 = [Reaction_A_1,forces_matrix[1][3]*forces_matrix[1][2],forces_matrix[1][0],forces_matrix[1][3]*(forces_matrix[1][5]-forces_matrix[1][2]),Reaction_B_1+Reaction_C]
                support_x_position_list_2.insert(1, forces_matrix[1][2] + support_x_position_list[1])
                plot_length_list_1 = np.repeat(support_x_position_list_2, 2)
        else:
            plot_reaction_list_1 = [Reaction_A_1,forces_matrix[1][3]*forces_matrix[1][2],forces_matrix[1][0],forces_matrix[1][3]*(forces_matrix[1][5]-forces_matrix[1][2]),Reaction_B_1+Reaction_C]
            support_x_position_list_2.insert(1, forces_matrix[1][2] + support_x_position_list[1])
            plot_length_list_1 = np.repeat(support_x_position_list_2, 2)
    

    p = 0
    e = [p]

    for i in range(len(plot_reaction_list)):
        p = p + plot_reaction_list[i]
        e.append(p)
    
    p_1 = 0
    e_1 = [p_1]

    for i in range(len(plot_reaction_list_1)):
        p_1 = p_1 + plot_reaction_list_1[i]
        e_1.append(p_1)
    
    plot_y = e + e_1
    plot_x = np.concatenate((plot_length_list , plot_length_list_1))

    print(plot_y)
    plt.plot(plot_x,plot_y)
    plt.title('SHEAR FORCE DIAGRAM')
    plt.xlabel('length')
    plt.ylabel('Shear force Values')
    if overhang_check == 'Yes':
        if overhang_loadings == 'Point_load':
            plt.plot([0,plot_length_list_1[-1]], [0,0])
        elif overhang_loadings == 'Distributed':
            plt.plot([0,plot_length_list_1[-1]], [0,0])
        elif overhang_loadings == 'moment':
            plt.plot([0,plot_length_list_1[-1]], [0,0])
    else:
        plt.plot([0,support_x_position_list[-1]], [0,0])

    for a,d in zip(plot_x,plot_y):
        plt.annotate(np.round(d,2), (a,d), horizontalalignment = 'left',
                         verticalalignment = 'top', fontsize = 9)
        
    
    

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
         
         moments_list = [m1,m2,-m2,m3,-m3,m4]
     
    
    #Reactions calculations
     Reaction_B =  (1/forces_matrix[0][5]) * ((-forces_matrix[0][0]*np.sin(np.radians(forces_matrix[0][1]))*forces_matrix[0][2])+ 
                                              (-forces_matrix[0][3]*forces_matrix[0][4]*0.5*forces_matrix[0][4]) + m1 - m2)
     Reaction_A = -forces_matrix[0][0]*np.sin(np.radians(forces_matrix[0][1])) + (-forces_matrix[0][3]*forces_matrix[0][4]) - Reaction_B
             
     Reactions_list = [Reaction_A, Reaction_B]
     
     Reaction_B_1 =  (1/forces_matrix[1][5]) * ((-forces_matrix[1][0]*np.sin(np.radians(forces_matrix[1][1]))*forces_matrix[1][2])+ 
                                              (-forces_matrix[1][3]*forces_matrix[1][4]*0.5*forces_matrix[1][4]) + m2 - m3)
     Reaction_A_1 = -forces_matrix[1][0]*np.sin(np.radians(forces_matrix[1][1])) + (-forces_matrix[1][3]*forces_matrix[1][4]) - Reaction_B_1
             
     Reactions_list_1 = [Reaction_A_1, Reaction_B_1]
     
     Reaction_B_2 =  (1/forces_matrix[2][5]) * ((-forces_matrix[2][0]*np.sin(np.radians(forces_matrix[2][1]))*forces_matrix[2][2])+ 
                                              (-forces_matrix[2][3]*forces_matrix[2][4]*0.5*forces_matrix[2][4]) + m3 - m4)
     Reaction_A_2 = -forces_matrix[2][0]*np.sin(np.radians(forces_matrix[2][1])) + (-forces_matrix[2][3]*forces_matrix[2][4]) - Reaction_B_2
             
     Reaction_C = 0
        
     Reactions_list_1 = [Reaction_A_2, Reaction_B_2]
     
     if overhang_check == 'Yes':
         if overhang_loadings == 'Point_load':
             Reaction_C = -overhang_load 
         elif overhang_loadings == 'Distributed':
             Reaction_C = -overhang_udl* overhang_udl_length
         elif overhang_loadings == 'combined':
             
             if overhang_load_list !=[] or overhang_moment_list != [] or overhang_udl_list != []:
                 point_load = 0
                 for t in range(len(overhang_load_list)):
                     if t % 2 == 0:
                         point_load = point_load + overhang_load_list[t]
                 point_udl = 0
                 for p in range(len(overhang_udl_list)):
                     if  p % 2 == 0:
                         point_udl = point_udl + ( overhang_udl_list[p]* (overhang_udl_list[p+1]))
             else:
                 point_load = 0
                 point_udl = 0
             Reaction_C = -point_load + -point_udl 
         Reactions_list_1 = [Reaction_A_2, Reaction_B_2, Reaction_C]
         
     support_x_position_list_1 = support_x_position_list[0:2]
     support_x_position_list_2 = support_x_position_list[2:4]
     support_x_position_list_3 = support_x_position_list[4:6]
     
     # first span
     if forces_matrix[0][0] == 0:
          plot_reaction_list = [Reaction_A,forces_matrix[0][3]*forces_matrix[0][4],Reaction_B]
          plot_length_list = np.repeat(support_x_position_list_1, 2)
     elif forces_matrix[0][3] == 0:
         plot_reaction_list = [Reaction_A,0,forces_matrix[0][0],0,Reaction_B]
         support_x_position_list_1.insert(1, forces_matrix[0][2])
         plot_length_list = np.repeat(support_x_position_list_1, 2)        
     else:
          plot_reaction_list = [Reaction_A,forces_matrix[0][3]*forces_matrix[0][2],forces_matrix[0][0],forces_matrix[0][3]*(forces_matrix[0][5]-forces_matrix[0][2]),Reaction_B]
          support_x_position_list_1.insert(1, forces_matrix[0][2])
          plot_length_list = np.repeat(support_x_position_list_1, 2)
      # second span     
     if forces_matrix[1][0] == 0:
          plot_reaction_list_1 = [Reaction_A_1,forces_matrix[1][3]*forces_matrix[1][4],Reaction_B_1]
          plot_length_list_1 = np.repeat(support_x_position_list_2, 2)
     elif forces_matrix[1][3] == 0:
         plot_reaction_list_1 = [Reaction_A_1,0,forces_matrix[1][0],0,Reaction_B_1]
         support_x_position_list_2.insert(1, forces_matrix[1][2])
         plot_length_list_1 = np.repeat(support_x_position_list_2, 2)        
     else:
          plot_reaction_list_1 = [Reaction_A_1,forces_matrix[1][3]*forces_matrix[1][2],forces_matrix[1][0],forces_matrix[1][3]*(forces_matrix[1][5]-forces_matrix[1][2]),Reaction_B_1]
          support_x_position_list_2.insert(1, forces_matrix[1][2] + support_x_position_list[1])
          plot_length_list_1 = np.repeat(support_x_position_list_2, 2)
          
     if forces_matrix[2][0] == 0:
         if overhang_check == "Yes":
             if overhang_loadings == 'Point_load':
                 plot_reaction_list_2 = [Reaction_A_2,forces_matrix[2][3]*forces_matrix[2][4],Reaction_B_2+Reaction_C,0,-Reaction_C]
                 support_x_position_list_3.append(support_x_position_list_3[1] + overhang_length)
                 plot_length_list_2 = np.repeat(support_x_position_list_3, 2)
             elif overhang_loadings == 'Distributed':
                 plot_reaction_list_2 = [Reaction_A_2,forces_matrix[2][3]*forces_matrix[2][4],Reaction_B_2+Reaction_C,-Reaction_C]
                 support_x_position_list_3.append(support_x_position_list_3[1] + overhang_udl_length)
                 plot_length_list_2 = np.repeat(support_x_position_list_3, 2)
                 plot_length_list_2 = np.delete(plot_length_list_2,[len(plot_length_list_2)-1])
         else:
             plot_reaction_list_2 = [Reaction_A_2,forces_matrix[2][3]*forces_matrix[2][4],Reaction_B_2+Reaction_C]
             plot_length_list_2 = np.repeat(support_x_position_list_3, 2)
     elif forces_matrix[2][3] == 0:
         if overhang_check == "Yes":
             if overhang_loadings == 'Point_load':
                 plot_reaction_list_2 = [Reaction_A_2,0,forces_matrix[2][0],0,Reaction_B_2+Reaction_C,0,-Reaction_C]
                 support_x_position_list_3.append(support_x_position_list_3[1] + overhang_length)
                 support_x_position_list_3.insert(1, forces_matrix[2][2])
                 plot_length_list_2 = np.repeat(support_x_position_list_3, 2)
             elif overhang_loadings == 'Distributed':
                 plot_reaction_list_2 = [Reaction_A_2,0,forces_matrix[2][0],0,Reaction_B_2+Reaction_C,-Reaction_C]
                 support_x_position_list_3.append(support_x_position_list_3[1] + overhang_udl_length)
                 support_x_position_list_3.insert(1, forces_matrix[2][2])
                 plot_length_list_2 = np.repeat(support_x_position_list_3, 2)
                 plot_length_list_2 = np.delete(plot_length_list_2,[len(plot_length_list_2)-1])
             elif overhang_loadings == 'moment':
                 plot_reaction_list_2 = [Reaction_A_2,0,forces_matrix[2][0],0,Reaction_B_2+Reaction_C]
                 support_x_position_list_3.insert(1, forces_matrix[2][2])
                 plot_length_list_2 = np.repeat(support_x_position_list_3, 2)    
         else:
             plot_reaction_list_2 = [Reaction_A_2,0,forces_matrix[2][0],0,Reaction_B_2+Reaction_C]
             support_x_position_list_3.insert(1, forces_matrix[2][2])
             plot_length_list_2 = np.repeat(support_x_position_list_3, 2)
             
     else:
         if overhang_check == "Yes":
             if overhang_loadings == 'Point_load':
                 plot_reaction_list_2 = [Reaction_A_2,forces_matrix[2][3]*forces_matrix[2][2],forces_matrix[2][0],forces_matrix[2][3]*(forces_matrix[2][5]-forces_matrix[2][2]),Reaction_B_2+Reaction_C,0,-Reaction_C]
                 support_x_position_list_3.append(support_x_position_list_3[1] + overhang_length)
                 support_x_position_list_3.insert(1, forces_matrix[2][2] + support_x_position_list[3])
                 plot_length_list_2 = np.repeat(support_x_position_list_3, 2)
             elif overhang_loadings == 'Distributed':
                 plot_reaction_list_2 = [Reaction_A_2,forces_matrix[2][3]*forces_matrix[2][2],forces_matrix[2][0],forces_matrix[2][3]*(forces_matrix[2][5]-forces_matrix[2][2]),Reaction_B_2+Reaction_C,-Reaction_C]
                 support_x_position_list_3.append(support_x_position_list_3[1] + overhang_udl_length)
                 support_x_position_list_3.insert(1, forces_matrix[2][2] + support_x_position_list[3])
                 plot_length_list_2 = np.repeat(support_x_position_list_3, 2)
                 plot_length_list_2 = np.delete(plot_length_list_2,[len(plot_length_list_2)-1])
             elif overhang_loadings == 'moment':
                 plot_reaction_list_2 = [Reaction_A_2,forces_matrix[2][3]*forces_matrix[2][2],forces_matrix[2][0],forces_matrix[2][3]*(forces_matrix[2][5]-forces_matrix[2][2]),Reaction_B_2+Reaction_C]
                 support_x_position_list_3.insert(1, forces_matrix[2][2] + support_x_position_list[3])
                 plot_length_list_2 = np.repeat(support_x_position_list_3, 2)
         else:
             plot_reaction_list_2 = [Reaction_A_2,forces_matrix[2][3]*forces_matrix[2][2],forces_matrix[2][0],forces_matrix[2][3]*(forces_matrix[2][5]-forces_matrix[2][2]),Reaction_B_2+Reaction_C]
             support_x_position_list_3.insert(1, forces_matrix[2][2] + support_x_position_list[3])
             plot_length_list_2 = np.repeat(support_x_position_list_3, 2)
     

     p = 0
     e = [p]

     for i in range(len(plot_reaction_list)):
         p = p + plot_reaction_list[i]
         e.append(p)
     
     p_1 = 0
     e_1 = [p_1]

     for i in range(len(plot_reaction_list_1)):
         p_1 = p_1 + plot_reaction_list_1[i]
         e_1.append(p_1)
         
     p_2 = 0
     e_2 = [p_2]

     for i in range(len(plot_reaction_list_2)):
         p_2 = p_2 + plot_reaction_list_2[i]
         e_2.append(p_2)
     
     plot_y = e + e_1 + e_2
     plot_x = np.concatenate((plot_length_list , plot_length_list_1, plot_length_list_2))

     print(plot_y)
     plt.plot(plot_x,plot_y)
     plt.title('SHEAR FORCE DIAGRAM')
     plt.xlabel('length')
     plt.ylabel('Shear force Values')
     if overhang_check == 'Yes':
         if overhang_loadings == 'Point_load':
             plt.plot([0,plot_length_list_2[-1]], [0,0])
         elif overhang_loadings == 'Distributed':
             plt.plot([0,plot_length_list_2[-1]], [0,0])
         elif overhang_loadings == 'moment':
             plt.plot([0,plot_length_list_2[-1]], [0,0])
     else:
         plt.plot([0,support_x_position_list[-1]], [0,0])

     for a,d in zip(plot_x,plot_y):
         plt.annotate(np.round(d,2), (a,d), horizontalalignment = 'left',
                          verticalalignment = 'top', fontsize = 9)
     
     
     
     
     
     
         
     
    
    
    



        
        
        
        
         
         
         
         
      
        
    
    

        
    
    
    
        

