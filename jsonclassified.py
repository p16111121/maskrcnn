#放在要進行分類之資料夾底下執行
import os
import os.path as osp
from shutil import copyfile,copytree,rmtree
mypath="E:/研究所/修課/ML/maskrcnn/traindata"
dir_name = ["cv2_mask","labelme_json","json","pic"]
for name in dir_name:
    if not osp.exists(mypath + "/" + name):
        os.mkdir(mypath + "/" + name)
tar_root1 = "./" + dir_name[0]
tar_root2 = "./" + dir_name[1]
tar_root3 = "./" + dir_name[2]
tar_root4 = "./" + dir_name[3]

i=1
for dir_name in os.listdir(mypath):
    # construct full file path
    if dir_name.endswith("_json") and dir_name!="labelme_json":
        source = osp.join(mypath,dir_name)
        file_name = dir_name.split('_j',1)[0]
        ori_pic = osp.join(mypath,file_name)+'.jpg'
        ori_json = osp.join(mypath,file_name)+'.json'
        ori_file = osp.join(source,'label.png')

        # copy only files
        new_id = f"{i}"
        new_labelme_json = new_id +'_json'
        destination = osp.join(tar_root2,new_labelme_json)
        if osp.exists(destination):
            rmtree(destination)
        copytree(source, destination)
        
        new_name = new_id +'.png'
        
        copyfile(ori_file,osp.join(tar_root1,new_name))

        new_pic = new_id +'.jpg'
        copyfile(ori_pic,osp.join(tar_root4,new_pic))

        new_json = new_id +'.json'
        copyfile(ori_json,osp.join(tar_root3,new_json))
        i+=1
            
print("Done")
