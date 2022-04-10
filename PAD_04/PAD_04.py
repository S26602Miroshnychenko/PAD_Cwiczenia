import numpy as np

print('Zad 1')
myarr1 = np.genfromtxt('Zadanie_1.csv',delimiter=";")[1:]
print('Ile komorek - ',myarr1.size)
num_rows, num_cols = myarr1.shape
print('Wiersze - ',num_rows,'Columny - ' ,num_cols)
print('Mean - ',np.nanmean(myarr1))
print('Median - ',np.nanmedian(myarr1))
print('Variance - ',np.nanvar(myarr1))
myarr1 = myarr1[np.logical_not(np.isnan(myarr1))]
print('Ile komorek - ',myarr1.size)

print('Zad 2')
myarr2 = np.genfromtxt('Zadanie_2.csv',delimiter=";")
print(myarr2)
print('Watrosci własne - ',np.linalg.eigvals(myarr2))
print('Wektory własne - ',np.linalg.eig(myarr2))
print('Macierz odwrotna - ',np.linalg.inv(myarr2))

print('Zad 3')
m1 = np.genfromtxt('Zadanie_3_macierz_A.csv',delimiter=",")
m2 = np.genfromtxt('Zadanie_3_macierz_B.csv',delimiter=",")
def cos_sim_2d(x, y):
    norm_x = x / np.linalg.norm(x, axis=1, keepdims=True)
    norm_y = y / np.linalg.norm(y, axis=1, keepdims=True)
    return np.matmul(norm_x, norm_y.T)
print(cos_sim_2d(m1, m2))