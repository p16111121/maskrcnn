import os
import os.path as osp
from shutil import copyfile
mypath=""
dir_name = ["cv2_mask","labelme_json","json","pic"]
for name in dir_name:
    if not osp.exists(mypath + "/" + name):
        os.mkdir(mypath + "/" + name)
for root, dirs ,names in os.walk(mypath):#输出在目录中的文件名
    for dr in dirs:
        if dr.endswith("_json"):
            tar_root = mypath + "/" + dir_name[0]
            file_dir = os.path.join(root,dr)

            file = os.path.join(file_dir,'label.png')

            new_name = dr.split('_j',1)[0] + '.png'
            new_file_name = os.path.join(tar_root,'label.png')

            tar_file = os.path.join(tar_root,new_name)
            copyfile(file,new_file_name)
            os.rename(new_file_name,tar_file)
print("Done")