import numpy as np

def conv2npy(file_name):
    f = open(file_name)
    for i in range(2581):
        f.readline()
    energy=np.zeros(100)
    flux = np.zeros(100)
    flux_err=np.zeros(100)
    for j in range(100):
        line=f.readline()
        energy[j]=float(line[4:14])
        flux[j]=float(line[17:28])
        flux_err[j]=float(line[30:35])
    np.save(file_name,[energy,flux,flux_err])


