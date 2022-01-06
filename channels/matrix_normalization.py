import sys
import numpy as np
import h5py
import math

channel_sequence = h5py.File(sys.argv[1], 'r')

name = channel_sequence.filename.strip('.hdf5')

print(name)

print(channel_sequence.filename, ":")

print([key for key in channel_sequence.keys()], "\n")

H_r = channel_sequence.get('H_r')

H_i = channel_sequence.get('H_i')

print("H_r :", H_r)

print("\n")

print("H_i :", H_i)

print("\n")

H_matrix = np.array(H_r[:, :, :, :, :] + 1j*H_i[:, :, :, :, :])
print(H_matrix.shape)



H_matrix /= np.sqrt(np.sum((H_matrix*H_matrix.conjugate()).real, axis=(1, 2, 3), keepdims=True) /
                    (np.prod(H_matrix.shape[1:4])))

print(np.sum((H_matrix*H_matrix.conjugate()).real, axis=(1, 2, 3), keepdims=True) /
                    (np.prod(H_matrix.shape[1:4])))

# np.save(f'{name}.npy', H_matrix)

# print('-------finish matrix normalization and successfully save the data-------')

