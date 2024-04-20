# Nila
👏👏 Noise Level Adaptive Diffusion Model for Robust Reconstruction of Accelerated MRI


## Data preprocess
All the npz data should contain ['rss'] key.
```
cd Nila/nila_training
python preprocess.py
```

```
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
```

## Train
```
cd Nila/nila_training
sh train.sh
```

## Sampling
Some simple demo are here.
```
cd Nila/nila_sampling
```

## Citation
```
@article{huang2024noise,
  title={Noise Level Adaptive Diffusion Model for Robust Reconstruction of Accelerated MRI},
  author={Huang, Shoujin and Luo, Guanxiong and Wang, Xi and Chen, Ziran and Wang, Yuwan and Yang, Huaishui and Heng, Pheng-Ann and Zhang, Lingyan and Lyu, Mengye},
  journal={arXiv preprint arXiv:2403.05245},
  year={2024}
}
```

