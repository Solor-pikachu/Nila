MODEL_FLAGS="--image_size 256 --num_channels 128 --num_res_blocks 2 --num_heads 4 --learn_sigma True"
DIFFUSION_FLAGS="--diffusion_steps 1000 --noise_schedule linear"
TRAIN_FLAGS="--lr 1e-4 --batch_size 8"

mpiexec -n 8 python scripts/image_train.py --data_dir data/fastmri_complex_value/ --log_dir log_DIT $MODEL_FLAGS $DIFFUSION_FLAGS $TRAIN_FLAGS
