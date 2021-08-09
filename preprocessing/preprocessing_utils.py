import os
from shutil import copyfile
import pandas as pd
import random
# datadir = '/Users/ryan/Desktop/Capstone/yolov5/yolov5/dataset/labels/val'
# for file in os.listdir(datadir):
# 	if file != '.DS_Store'
# 		path = os.path.join(datadir,file)
# 		file_name = file[:-3] + 'png'
# 		dest = os.path.join('/Users/ryan/Desktop/Capstone/yolov5/yolov5/dataset/images/class1',file_name)
# 		dest_2 = os.path.join('/Users/ryan/Desktop/Capstone/yolov5/yolov5/dataset/images/val',file_name)
# 		copyfile(dest,dest_2)

###########################################################################################################
# Create folder with labels
# datadir = '/Users/ryan/OneDrive - Singapore University of Technology and Design/SUTD_Footage/outside_to_sch_done'
# output_dir = '/Users/ryan/OneDrive - Singapore University of Technology and Design/SUTD_Footage/outside_to_sch_label'
# for file in os.listdir(datadir):
# 	if file != '.DS_Store':
# 		path = os.path.join(datadir,file)
# 		suffix = file[-3:]
# 		if suffix == 'txt':
# 			new_path = os.path.join(output_dir,file)
# 			copyfile(path,new_path)
###########################################################################################################
# # Create folder with only images with labels
# labeldir = '/Users/ryan/OneDrive - Singapore University of Technology and Design/SUTD_Footage/combined_val_label'
# datadir = '/Users/ryan/OneDrive - Singapore University of Technology and Design/SUTD_Footage/combined_img'
# output_dir = '/Users/ryan/OneDrive - Singapore University of Technology and Design/SUTD_Footage/combined_val_img'
# label_list = []
# for label in os.listdir(labeldir):
# 	name = label[:-4]
# 	label_list.append(name)

# for file in os.listdir(datadir):
# 	if file != '.DS_Store' and file[:-4] in label_list and file[-4:] == '.jpg':
# 		path = os.path.join(datadir,file)
# 		# file_name = file[:-3] + 'png'
# 		org = os.path.join(datadir,file)
# 		dest = os.path.join(output_dir,file)
		# copyfile(org,dest)
#--------------------------------------------------------------------------------------------------------#
# label_path = '/Users/ryan/OneDrive - Singapore University of Technology and Design/SUTD_Footage/combined_label'
# training_ratio = 0.8
# combined_train = '/Users/ryan/OneDrive - Singapore University of Technology and Design/SUTD_Footage/combined_train_label'
# combined_val = '/Users/ryan/OneDrive - Singapore University of Technology and Design/SUTD_Footage/combined_val_label'
# label_list = []
# for label in os.listdir(label_path):
# 	label_list.append(label)
# random.shuffle(label_list)
# num_images = 0.8 * len(label_list)
# chosen = label_list[:int(num_images)]
# val = label_list[int(num_images):]
# for i in chosen:
# 	org = os.path.join(label_path,i)
# 	dest = os.path.join(combined_train,i)
# 	copyfile(org,dest)

# for i in val:
# 	org = os.path.join(label_path,i)
# 	dest = os.path.join(combined_val,i)
# 	copyfile(org,dest)

#This is to add a prefix to the filenames to diffenciate the video they came from
# datadir = '/Users/ryan/OneDrive - Singapore University of Technology and Design/SUTD_Footage/behind_sch_done'
# for file in os.listdir(datadir):
# 	if file != '.DS_Store':
# 		# print(file)
# 		prefix = 'behind_sch'
# 		filename = prefix + file
# 		# print(filename)
# 		org_path = os.path.join(datadir,file)
# 		new_path = os.path.join(datadir,filename)
# 		# print(org_path)
# 		# print(new_path)
# 		# file_name = file[:-3] + 'png'
# 		# dest = os.path.join('/Users/ryan/Desktop/Capstone/yolov5/yolov5/dataset/images/class1',file_name)
# 		# dest_2 = os.path.join('/Users/ryan/Desktop/Capstone/yolov5/yolov5/dataset/images/val',file_name)
# 		os.rename(org_path,new_path)


# This is to rename the files with xml.txt to .txt
# datadir = '/Users/ryan/OneDrive - Singapore University of Technology and Design/SUTD_Footage/behind_sch_done'
# for file in os.listdir(datadir):
# 	if file != '.DS_Store':
# 		# print(file)
# 		prefix = 'xml.txt'
# 		suffix = file[-7:]
# 		org = os.path.join(datadir,file)


# 		if suffix == prefix:
# 			new_file = file[:-8]+'.txt'
# 			new = os.path.join(datadir,new_file)
# 			os.rename(org,new)
			# print(file)
#---------------------------------------------------------------------------------------------------------------#
#adding background images
# img_dir = '/Users/ryan/OneDrive - Singapore University of Technology and Design/SUTD_Footage/outside_to_sch_img'
# datadir = '/Users/ryan/OneDrive - Singapore University of Technology and Design/SUTD_Footage/outside_to_sch_done'
# # prefix = 'sch_to_outside'
# prefix = 'outside_to_schframe'
# labeldir ='/Users/ryan/OneDrive - Singapore University of Technology and Design/SUTD_Footage/outside_to_sch_label'
# img_count = 0
# chosen = 0
# bg_img = []
# bg_img_full = []
# for file in os.listdir(img_dir):
# 	img_count += 1
# bg_count = int(0.15 * img_count)

# # #handling csv of all frames
# # #Converting from number to frame name
# csv_path = '/Users/ryan/OneDrive - Singapore University of Technology and Design/SUTD_Footage/outside_to_sch_unlabelled.csv'
# # csv_path = '/Users/ryan/Downloads/not_labeled.csv'
# non_frames = pd.read_csv(csv_path)
# print(non_frames)
# non_frames = non_frames['Frames'].tolist()
# print(non_frames)

# random.shuffle(non_frames)
# print(non_frames)
# bg_img = non_frames[0:bg_count]
# print(bg_img)


# # #Generating from ranges


# for name in bg_img:
# 	suffix = '.jpg'
# 	full = prefix + str(name) + suffix

# 	# labelname = prefix + name[:-3] + 'txt'
# 	labelname = prefix + str(name) + '.txt'
# 	org = os.path.join(datadir,full)
# 	dest = os.path.join(img_dir,full)
# 	txtpath = os.path.join(labeldir,labelname)
# 	print(org)
# 	print(dest)
# 	print(txtpath)
# 	copyfile(org,dest)
# 	with open(txtpath, 'w') as fp:
# 		pass
