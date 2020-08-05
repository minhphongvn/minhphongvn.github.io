import timeit
import argparse
import getpass

import h5py
import numpy as np
import cPickle as pkl
from asdf import AsdfFile

if __name__ == "__main__":
	a = np.random.random((10000,10000))

	t0 = timeit.default_timer()
	with open('data.pkl', 'wb') as f:
	    pkl.dump(a,f)
	t0 = timeit.default_timer() - t1
	print 'cPickle: {} secs'.format(t1)

	t1 = timeit.default_timer()
	np.savetxt('data.txt', a)
	t1 = timeit.default_timer() - t1
	print '.txt: {} secs'.format(t1)

	t2 = timeit.default_timer()
	h5f = h5py.File('data.hdf5','w')
	h5f.create_dataset('dataset_1', data=a)
	h5f.close()
	t2 = timeit.default_timer() - t2
	print 'hdf5: {} secs'.format(t2)

	t3 = timeit.default_timer()
	tree = {'dataset_1':a}
	ff = AsdfFile(tree)
	ff.write_to('data.asdf')
	t3 = timeit.default_timer() - t3
	print 'asdf: {} secs'.format(t3)