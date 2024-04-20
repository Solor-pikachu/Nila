import shutil
import os

import numpy as np
from numpy.fft import fftshift, ifftshift, ifft2,fft2

import h5py
from spreco.common import utils
from tqdm import tqdm
import glob

paths = sorted(glob.glob(f'/data2/fastmri/multicoil_train/*.h5'))
for current_num,path in enumerate(paths):
    print(current_num)
    name = path.split('/')[-1].replace('.h5','')
    fs = h5py.File(path, "r")
    kspace = fs['kspace']
    
    if kspace.shape[0] > 10:
        kspace = kspace[:-4,...,]
    
    kspace = np.transpose(kspace, [2,3,1,0])
    print(kspace.shape)
    
    image_shape = [kspace.shape[1],kspace.shape[1]]
    print(image_shape)
    
    coil_imgs = fftshift(ifft2(ifftshift(kspace), axes=(0,1)))
        
    coilsens = np.zeros_like(coil_imgs, dtype='complex64')

    for i in range(kspace.shape[-1]):
        s_kspace = kspace[..., i]
        coilsens[..., i] = utils.bart(1, 'ecalib -m1 -r20 -c0.001', s_kspace[np.newaxis, ...])

    rss = np.squeeze(np.sum(coil_imgs*np.conj(coilsens), axis=2))
    
    rss = utils.bart(1, 'resize -c 0 '+str(image_shape[0])+ ' 1 ' +str(image_shape[1]), rss)
    
    for i in range(rss.shape[-1]):
        tmp = rss[..., i]
        tmp = tmp.astype(np.complex64)
        np.savez(f"train_data/{name}_{i:02d}", rss=tmp)

    fs.close()
