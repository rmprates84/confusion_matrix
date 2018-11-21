# This code plot the confusion matrix
# Copyright 2018 - Ricardo Prates

# Function to plot de CM
'''
Y_Real - True values (ARGMAX)
array([0, 0, 0, ..., 3, 3, 3], dtype=int64)


Y_Pred - Predicted values (ARGMAX)
array([0, 0, 0, ..., 2, 1, 3], dtype=int64)
'''

# Function
def conf_matrix(Y_Pred, Y_Real):
    n_clas = max(Y_Real+1) #Verifica o número de classes
    mat_conf= [[0 for i in range(n_clas + 1)] for j in range(n_clas + 1)] #Cria uma matriz M = (n_clas+1)x(n_clas+1)
    for nl in range (0,n_clas):
        for i in range (0,len(Y_Pred)):
            if(Y_Real[i] == nl):
                for nc in range (0,n_clas):
                    if(Y_Pred[i]==nc):
                        mat_conf[nl][nc] = mat_conf[nl][nc] + 1

    for cm1 in range (0,n_clas):
        for cm2 in range (0,n_clas):
            mat_conf[n_clas][cm1] = mat_conf[n_clas][cm1] + mat_conf[cm2][cm1]
        mat_conf[n_clas][cm1] = round((mat_conf[cm1][cm1]/mat_conf[n_clas][cm1]*100),2)

    for cm1 in range (0,n_clas):
        for cm2 in range (0,n_clas):
            mat_conf[cm1][n_clas] = mat_conf[cm1][n_clas] + mat_conf[cm1][cm2]
        mat_conf[cm1][n_clas] = round((mat_conf[cm1][cm1]/mat_conf[cm1][n_clas]*100),2)

    for cm1 in range(0, n_clas):
        mat_conf[n_clas][n_clas] = mat_conf[cm1][cm1] + mat_conf[n_clas][n_clas]
    mat_conf[n_clas][n_clas] = round((mat_conf[n_clas][n_clas]/len(Y_Real)*100),2)

    return mat_conf

if __name__ == '__main__':
    conf_matrix()