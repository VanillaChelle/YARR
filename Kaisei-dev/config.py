# Paths
__sample_path_1__ = "../testcases/no_anno/SP_LOFI_mmexport1519399281474_WX.jpg"
__sample_path_2__ = "../testcases/STV2K_ts_0339.jpg"

demo_data_path = "../testcases/"
training_data_path = "/Users/dementia/Desktop/Research/Datasets/St2kNew/stv2k_train"
test_data_path = "/Users/dementia/Desktop/Research/Datasets/St2kNew/stv2k_test"
training_data_path_pami = "/media/data2/hcx_data/STV2K/stv2k_train"
test_data_path_pami = "/media/data2/hcx_data/STV2K/stv2k_test"
training_data_path_pami2 = "/media/data1/hcxiao/STV2K/stv2k_train"
test_data_path_pami2 = "/media/data1/hcxiao/STV2K/stv2k_test"
training_data_path_z440 = "/home/xhuang/Research/Datasets/STV2K_New/stv2k_train"
test_data_path_z440 = "/home/xhuang/Research/Datasets/STV2K_New/stv2k_test"
alphabet_filename = "stv2k_alphabet_2784_no-blank.txt"

expr_name = "Kaisei-det"
log_file_name = expr_name + "_fixlr-5e-5_run1"

# Constants
STV2K_image_width = 2448
STV2K_image_height = 3264
STV2K_train_image_num = 1215
STV2K_test_image_num = 853
STV2K_train_image_channel_means = (112.7965, 106.6500, 101.0181)
STV2K_train_image_channel_std = (19.3811, 18.2817, 19.1222)
STV2K_test_image_channel_means = (113.4384, 109.0392, 102.7425)
STV2K_test_image_channel_std = (21.3310, 20.0747, 20.0667)

# Data and Augmentation Settings
# min_crop_side_ratio = 0.2
min_text_size = 4
min_char_avgsize = 5
max_side_len = 1280
fixed_len = 640  # So we generate gt of size 400*400

# Detection Branch Settings
text_scale = 1024  # Decides the receptive field of detection branch
score_map_threshold = 0.8
box_threshold = 0.1
nms_threshold = 0.2

# GPU Training Settings
data_loader_worker_num = 4  # Setting to 0 will load data in the main process
gpu_list = [0]
batch_size = 8  # set to 16 during training
test_batch_size = 8
test_iter_num = 5
iter_num = 1000
epoch_num = 30
val_interval = 500
notify_interval = 30
ckpt_interval = 500
ckpt_path = "./save_points"
on_cuda = True
continue_train = False
ckpt_filename = ""

# Optimizer and Learning Policy
lr = 5e-5
adam = False
beta1 = 0.5
adadelta = False
rmsprop = True  # Default optimizer