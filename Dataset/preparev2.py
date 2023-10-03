import os
import numpy as np
from shutil import copyfile
from shutil import move
import random

# You only need to change this line to your dataset download path
download_path = 'D:/College/TA/vehicleReidTraining/VRIC'

if not os.path.isdir(download_path):
    print('please change the download_path')

save_path = download_path + '/pytorch'
if not os.path.isdir(save_path):
    os.mkdir(save_path)

rename_path = download_path + '/rename'
if not os.path.isdir(rename_path):
    os.mkdir(rename_path)

#-----------------------------------------
#train
train_path = download_path + '/train_images'
train_save_path = save_path + '/train'
train_text = open(download_path + '/vric_train.txt', 'r') #open file txt
read_train_text = train_text.read() #read file txt
split_data_train_text = read_train_text.split() #split the string inside file txt

length = len(split_data_train_text)
length_int = int(length) #amount of dataset

if not os.path.isdir(train_save_path):
    os.mkdir(train_save_path)

for root, dirs, files in os.walk(train_path, topdown = True):
    print("\npreparing train dataset")
    for name in files:
        if not name[-3:]=='jpg':
            continue
        for x in range (0,length_int, 3):
            if name == split_data_train_text[x]:
                # print(name)
                src_path = train_path + '/' + name
                dst_path = train_save_path + '/' + split_data_train_text[x+1] 
                if not os.path.isdir(dst_path):
                    os.mkdir(dst_path)
                copyfile(src_path, dst_path + '/' + name)
            else :
                continue

#-----------------------------------------
#rename train
rename_train_save_path = rename_path + '/train'

length = len(split_data_train_text)
length_int = int(length) #amount of dataset
id_list = os.listdir(train_save_path)

image_count_per_id = 0

if not os.path.isdir(rename_train_save_path):
    os.mkdir(rename_train_save_path)

print("\nrenaming train dataset")

for x in id_list:
    for y in range(1, length_int, 3):
        if x == split_data_train_text[y]:
            src_path = train_save_path + '/' + x + '/' + split_data_train_text[y-1]
            dst_path = rename_train_save_path + '/' + x
            if not os.path.isdir(dst_path):
                    os.mkdir(dst_path)
            
            if int(split_data_train_text[y]) > 0 and int(split_data_train_text[y]) < 10:
                    new_id = '0000' + split_data_train_text[y]
            elif int(split_data_train_text[y]) >=10 and int(split_data_train_text[y]) < 100:
                    new_id = '000' + split_data_train_text[y]
            elif int(split_data_train_text[y]) >=100 and int(split_data_train_text[y]) <1000:
                    new_id = '00' + split_data_train_text[y]
            elif int(split_data_train_text[y]) >=1000:
                    new_id = '0' + split_data_train_text[y]
            if int(split_data_train_text[y+1]) > 0 and int(split_data_train_text[y+1]) <10:
                    new_cam = '000' + split_data_train_text[y+1]
            elif int(split_data_train_text[y+1]) >=10 and int(split_data_train_text[y+1]) <100:
                    new_cam = '00' + split_data_train_text[y+1]
            elif int(split_data_train_text[y+1]) >=100 and int(split_data_train_text[y+1]) <1000:
                    new_cam = '0' + split_data_train_text[y+1]
            
            old_name = split_data_train_text[y-1]
            copyfile(src_path, dst_path + '/' + old_name)
            new_name = new_id + '_' + new_cam + '_' + str(image_count_per_id) + '.jpg'
            os.rename(dst_path + '/' + old_name, dst_path + '/' + new_name)
            # print(new_name)
            image_count_per_id = image_count_per_id + 1
        else:
            continue
    image_count_per_id = 0

#-----------------------------------------
#val
rename_val_save_path = rename_path + '/val'
id_list = os.listdir(train_save_path)
val_image_count_per_id = 0

if not os.path.isdir(rename_val_save_path):
    os.mkdir(rename_val_save_path)

print("\npreparing val dataset")

for x in range(0, 5660):
    if not os.path.isdir(rename_train_save_path + '/' + str(x)):
        continue
    else:
        print(x)
        src_path = rename_train_save_path + '/' + str(x) + '/'
        dst_path = rename_val_save_path + '/' + str(x)
        if not os.path.isdir(dst_path):
            os.mkdir(dst_path)

        file_list = os.listdir(src_path)
        print(file_list)

        if len(file_list) < 2:
             continue
        else:
            random_image = random.choice(file_list)
            move(os.path.join(src_path, random_image), os.path.join(dst_path, random_image))

#-----------------------------------------
#query
query_path = download_path + '/probe_images'
query_save_path = save_path + '/query'
query_text = open(download_path + '/vric_probe.txt', 'r') #open file txt
read_query_text = query_text.read() #read file txt
split_data_query_text = read_query_text.split() #split the string inside file txt

length = len(split_data_query_text)
length_int = int(length) #amount of dataset

if not os.path.isdir(query_save_path):
    os.mkdir(query_save_path)

for root, dirs, files in os.walk(query_path, topdown = True):
    print("\npreparing query dataset")
    for name in files:
        if not name[-3:]=='jpg':
            continue
        for x in range (0,length_int, 3):
            if name == split_data_query_text[x]:
                print(name)
                src_path = query_path + '/' + name
                dst_path = query_save_path + '/' + split_data_query_text[x+1] 
                if not os.path.isdir(dst_path):
                    os.mkdir(dst_path)
                copyfile(src_path, dst_path + '/' + name)
            else :
                continue

#-----------------------------------------
#rename query
rename_query_save_path = rename_path + '/query'

length = len(split_data_query_text)
length_int = int(length) #amount of dataset
id_list = os.listdir(query_save_path)

image_count_per_id = 0

if not os.path.isdir(rename_query_save_path):
    os.mkdir(rename_query_save_path)

print("\nrenaming query dataset")

for x in id_list:
    for y in range(1, length_int, 3):
        if x == split_data_query_text[y]:
            src_path = query_save_path + '/' + x + '/' + split_data_query_text[y-1]
            dst_path = rename_query_save_path + '/' + x
            if not os.path.isdir(dst_path):
                    os.mkdir(dst_path)
            
            if int(split_data_query_text[y]) > 0 and int(split_data_query_text[y]) < 10:
                    new_id = '0000' + split_data_query_text[y]
            elif int(split_data_query_text[y]) >=10 and int(split_data_query_text[y]) < 100:
                    new_id = '000' + split_data_query_text[y]
            elif int(split_data_query_text[y]) >=100 and int(split_data_query_text[y]) <1000:
                    new_id = '00' + split_data_query_text[y]
            elif int(split_data_query_text[y]) >=1000:
                    new_id = '0' + split_data_query_text[y]
            if int(split_data_query_text[y+1]) > 0 and int(split_data_query_text[y+1]) <10:
                    new_cam = '000' + split_data_query_text[y+1]
            elif int(split_data_query_text[y+1]) >=10 and int(split_data_query_text[y+1]) <100:
                    new_cam = '00' + split_data_query_text[y+1]
            elif int(split_data_query_text[y+1]) >=100 and int(split_data_query_text[y+1]) <1000:
                    new_cam = '0' + split_data_query_text[y+1]
            
            old_name = split_data_query_text[y-1]
            copyfile(src_path, dst_path + '/' + old_name)
            new_name = new_id + '_' + new_cam + '_' + str(image_count_per_id) + '.jpg'
            os.rename(dst_path + '/' + old_name, dst_path + '/' + new_name)
            print(new_name)
            image_count_per_id = image_count_per_id + 1
        else:
            continue
    image_count_per_id = 0

#-----------------------------------------
#gallery
gallery_path = download_path + '/gallery_images'
gallery_save_path = save_path + '/gallery'
gallery_text = open(download_path + '/vric_gallery.txt', 'r') #open file txt
read_gallery_text = gallery_text.read() #read file txt
split_data_gallery_text = read_gallery_text.split() #split the string inside file txt

length = len(split_data_gallery_text)
length_int = int(length) #amount of dataset

if not os.path.isdir(gallery_save_path):
    os.mkdir(gallery_save_path)

for root, dirs, files in os.walk(gallery_path, topdown = True):
    print("\npreparing gallery dataset")
    for name in files:
        if not name[-3:]=='jpg':
            continue
        for x in range (0,length_int, 3):
            if name == split_data_gallery_text[x]:
                print(name)
                src_path = gallery_path + '/' + name
                dst_path = gallery_save_path + '/' + split_data_gallery_text[x+1] 
                if not os.path.isdir(dst_path):
                    os.mkdir(dst_path)
                copyfile(src_path, dst_path + '/' + name)
            else :
                continue

#-----------------------------------------
#rename gallery
rename_gallery_save_path = rename_path + '/gallery'

length = len(split_data_gallery_text)
length_int = int(length) #amount of dataset
id_list = os.listdir(gallery_save_path)

image_count_per_id = 0

if not os.path.isdir(rename_gallery_save_path):
    os.mkdir(rename_gallery_save_path)

print("\nrenaming gallery dataset")

for x in id_list:
    for y in range(1, length_int, 3):
        if x == split_data_gallery_text[y]:
            src_path = gallery_save_path + '/' + x + '/' + split_data_gallery_text[y-1]
            dst_path = rename_gallery_save_path + '/' + x
            if not os.path.isdir(dst_path):
                    os.mkdir(dst_path)
            
            if int(split_data_gallery_text[y]) > 0 and int(split_data_gallery_text[y]) < 10:
                    new_id = '0000' + split_data_gallery_text[y]
            elif int(split_data_gallery_text[y]) >=10 and int(split_data_gallery_text[y]) < 100:
                    new_id = '000' + split_data_gallery_text[y]
            elif int(split_data_gallery_text[y]) >=100 and int(split_data_gallery_text[y]) <1000:
                    new_id = '00' + split_data_gallery_text[y]
            elif int(split_data_gallery_text[y]) >=1000:
                    new_id = '0' + split_data_gallery_text[y]
            if int(split_data_gallery_text[y+1]) > 0 and int(split_data_gallery_text[y+1]) <10:
                    new_cam = '000' + split_data_gallery_text[y+1]
            elif int(split_data_gallery_text[y+1]) >=10 and int(split_data_gallery_text[y+1]) <100:
                    new_cam = '00' + split_data_gallery_text[y+1]
            elif int(split_data_gallery_text[y+1]) >=100 and int(split_data_gallery_text[y+1]) <1000:
                    new_cam = '0' + split_data_gallery_text[y+1]
            
            old_name = split_data_gallery_text[y-1]
            copyfile(src_path, dst_path + '/' + old_name)
            new_name = new_id + '_' + new_cam + '_' + str(image_count_per_id) + '.jpg'
            os.rename(dst_path + '/' + old_name, dst_path + '/' + new_name)
            print(new_name)
            image_count_per_id = image_count_per_id + 1
        else:
            continue
    image_count_per_id = 0