#!/usr/bin/env python

import pandas
import pickle
import feather
import h5py
import numpy as np
import scipy.io as sio
import os
import sys

def convert_feather(df, output_filename):
    feather.write_dataframe(df, output_filename)

def convert_hdf5(df, output_filename):
    X = df.values
    f = h5py.File(output_filename, "w")
    ds=f.create_dataset("mydataset", X.shape, dtype=X.dtype)
    ds[...] = X

def convert_npy(df, output_filename):
    X = df.values
    np.save(output_filename, X)

def convert_pkl(df, output_filename):
    fid = open(output_filename, "wb")
    pickle.dump(df, fid)
    fid.close()

def convert_mat(df, output_filename):
    dd = {key: df[key].values.flatten() for key in df.keys()}
    sio.savemat(output_filename, dd)

input_filename = sys.argv[1]
output_filenames = sys.argv[2:]

if not input_filename.endswith(".csv"):
    print "input must be a CSV file (by extension)"
    sys.exit(1)

df = paratext.load_csv_to_pandas(input_filename, allow_quoted_newlines=True)

for output_filename in output_filenames:
    _, extension = os.path.splitext(output_filename)
    if extension == ".hdf5":
        convert_hdf5(df, output_filename)
    elif extension == ".feather":
        convert_feather(df, output_filename)
    elif extension == ".pkl":
        convert_pkl(df, output_filename)
    elif extension == ".npy":
        convert_npy(df, output_filename)
    elif extension == ".mat":
        convert_mat(df, output_filename)
    else:
        print "skipping '%s'; invalid output format '%s'" % (output_filename, extension)
