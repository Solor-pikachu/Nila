# Nila
Noise Level Adaptive Diffusion Model for Robust Reconstruction of Accelerated MRI


## data preprocess
All the npz data should contain ['rss'] key.
├── fastmri_complex_value/
│   ├──...
│   ├── file_brain_AXT2_201_2010466_01.npz
│   ├── file_brain_AXT2_201_2010466_02.npz
│   ├── file_brain_AXT2_201_2010466_03.npz
│   ├── file_brain_AXT2_201_2010466_04.npz
│   ├── file_brain_AXT2_201_2010466_05.npz
│   ├── file_brain_AXT2_201_2010466_06.npz
│   ├── file_brain_AXT2_201_2010466_07.npz
│   ├── file_brain_AXT2_201_2010466_08.npz
│   ├── file_brain_AXT2_201_2010466_09.npz
│   ├── file_brain_AXT2_201_2010466_10.npz
│   ├──...

## Train
```
cd Nila/nila_training
sh train.sh
```
