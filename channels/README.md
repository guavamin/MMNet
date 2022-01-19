We need ``QuaDriGa`` and ``Matlab`` to run ``generate.m``.

The channel data "*.hdf5" generated from the MATLAB contains 'H_r' and 'H_i' part of the H matrix.

### Normalize the channel data based on the formula on the paper at page 6: 
```sh
$ python3 matrix_normalization.py *.hdf5
```
The result of this part of code is normalized channel data and you can save it in "H_matrix.npy". 
