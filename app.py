import random
import math

# util helper function
def get_max_index(input_list):
    max = input_list[0]
    index = 0
    for i in range(1,len(input_list)):
        if input_list[i] > max:
            max = input_list[i]
            index = i
    return index

# Fitness function. The code maximizes the value of the fitness function
def non_linear_func(x):
    # return (math.sin(x**2))+(math.sin(x))+(math.sin(x)*math.cos(x))
    return (math.sin(x*3.1415/180.0)+(10))

#this will update the velocity of the particle based on the provided parameters
def velocity_update_func(vi,xi,p_best,g_best,c1,c2,r1,r2,w):
    return (w*vi)+((c1*r1)*(p_best-xi))+((c2*r2)*(g_best-xi))


if __name__ == "__main__":

    rounds = 4 # float number upto 4 points

    # Control parameters
    w = 0.5     # Intertial weight.
    c1 = 2.0    # constant, Weight of searching based on the optima found by a particle
    c2 = 2.0    #constant
    r1 = 0.213  #constant
    r2 = 0.816  #constant                 
    prv_vel = 0 # velocity 0 for first iterations                

    num_particle = 8     # population size (number of particles)
    max_iter = 10        # maximum number of iterations 

    x_l = -2*3.167    # lower bound  
    x_u =  2*3.167    # upper bound

    g_best = 0
    p_best = 0
    
    # list for strorig result of every iteration
    p_postions = [[0]*8]*10     #8 particle and 10
    p_bests = [[0]*8]*10        #8 particle and 10
    new_velocities = [[0]*8]*10
    func_res = [[0]*8]*10
    g_bests = []



    p_postions[0] = [6.14744,-2.73181,1.22814,5.26173,-2.63041,4.27565,4.29283,-3.08031] # first iteration positions, we can generate it randomly

    for iter in range(max_iter):

        if iter==0:
            p_bests[0] = p_postions[0]
            prv_vel = 0                 

        tmp_res = []
        tmp_p_bests = []
        for i in range(num_particle):
            # ran = round(random.uniform(x_l, x_u),4)
            # p_bests.append(ran)    
            res = round(non_linear_func(p_postions[iter][i]),rounds)
            if iter!=0:
                if res>func_res[iter-1][i]:
                    tmp_p_bests.append(p_postions[iter][i])
                else:
                    tmp_p_bests.append(p_postions[iter-1][i])
            # print(func_res[iter][i])
            tmp_res.append(res)

        func_res[iter] = tmp_res

        if iter!=0:
            p_bests[iter] = tmp_p_bests

        g_best = p_postions[iter][get_max_index(func_res[iter])]
        g_bests.append(g_best)
        print("iteratoin : ",iter)
        print("particle positions : ",p_postions)


        tmp_vel = []
        tmp_pos = []
        for i in range(num_particle):
            new_velocity = 0
            if iter==0:
                new_velocity = round(velocity_update_func(prv_vel,p_postions[iter][i],p_bests[iter][i],g_best,c1,c2,r1,r2,w),rounds)
            else:
                new_velocity = round(velocity_update_func(new_velocities[iter-1][i],p_postions[iter][i],p_bests[iter][i],g_best,c1,c2,r1,r2,w),rounds)

            tmp_vel.append(new_velocity)
            # new_position = round(new_velocity + p_postions[iter][i],4)
            tmp_pos.append(round(new_velocity + p_postions[iter][i],rounds))
            # p_postions[iter][i] = new_position
            # print("p_best: ",p_bests[iter][i]," p_position: ",str(p_postions[iter][i])," fun_res: ",str(func_res[iter][i])," new_velocity: ",str(new_velocity))
        new_velocities[iter] = tmp_vel
        if iter<=(max_iter-2):
            p_postions[iter+1] = tmp_pos


        #this prints the values of each iteration
        print("g bests : ",g_bests)
        print("function results : ",func_res)
        print("new velocities : ",new_velocities)

        print("----------------------------------")
        # if(iter==1):
        #     break



    
