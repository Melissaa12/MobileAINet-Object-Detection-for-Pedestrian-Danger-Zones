# MobileAINet-Object-Detection-for-Pedestrian-Danger-Zones

## Preprocessing
In preprocessing folder, there are scripts that preps the data for training

- SplitVid.py:
This script will split the video into frames and save them every 10 frames
- preprocessing_utils.py:
This script contains miscellaneous parts of codes that were used for different uses such as splitting the images into datasets and shifting of images into different folders

## Model
This folder is containing scripts edited from Ultralytics repo and data generated from it. Run YOLOv5_Code_final.ipynb to see usages of the code repo like traning and evaluation on models.

This read me includes the important parts of the repository that we edited or is relevant

- test.py:
script to run evaluation for model on dataset
- detect.py:
script to do inference for model on dataset
- Adam.pt:
model weights for configuration using Adam optimiser on mix_dataset
- best_NTU.pt:
model weights after training on NTU dataset
- mix50:
model weights for configuration using SGD optimiser on mix_dataset

python scripts for training model
- all_train_freeze.py:
script to train model that freezes weights in all layers except the final layer for transfer learning
- backbone_train_freeze.py:
script to train model that freezes weights in layers in model backbone for transfer learning
- train.py:
script that trains model finetuning all weights
### Model/runs
output and results from training and detecting, there is Adam_50 for example of output from training model.

### Model/data
- coco128_mix.yaml:
config file for data training where we will specify the path for the mix_data and the classes for object detection
- coco128_aug.yaml:
config file for data training where we will specify the path for the mix_data with augmentation and the classes for object detection
- coco128.yaml:
config file for data training where we will specify the path for the split_dataset configuration and the classes for object detection
- hyps/hyp.scratch.yaml:
config file stating default initial hyperparameters values using SGD optimiser
- hyps/hyp.test1.yaml:
config file stating default initial hyperparameters values using Adam optimiser

Note: Dataset is not provided in repo, for example dataset can look at this link https://drive.google.com/drive/folders/1ZCeKRX5lIT3uJJV7YViME_I0zZd0nfwS?usp=sharing for dataset with augmented images

