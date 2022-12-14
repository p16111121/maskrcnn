import os
import os.path as osp
from shutil import copyfile,copytree,rmtree
mypath="D:/研究所/修課/ML/maskrcnn/traindata"
dir_name = ["cv2_mask","labelme_json","json","pic"]
for name in dir_name:
    if not osp.exists(mypath + "/" + name):
        os.mkdir(mypath + "/" + name)
tar_root1 = "./" + dir_name[0]
tar_root2 = "./" + dir_name[1]
tar_root3 = "./" + dir_name[2]
tar_root4 = "./" + dir_name[3]
for root, dirs ,names in os.walk(mypath):#输出在目录中的文件名
    #root 當前路徑 dir當前路徑下資料夾name names 檔案名稱
    i=1
    for dr in dirs:
        
        if dr.endswith("_json") and dr!="labelme_json": 
            file_dir = osp.join(mypath,dr)#路徑+資料夾 #join連結字串
            
            file_name = dr.split('_j',1)[0]
            ori_pic = osp.join(root,file_name)+'.jpg'
            ori_json = osp.join(root,file_name)+'.json'
            ori_file = osp.join(file_dir,'label.png')
            
            new_id = f"{i}"
            new_name = new_id +'.png'
            
            copyfile(ori_file,osp.join(tar_root1,new_name))

            new_pic = new_id +'.jpg'
            copyfile(ori_pic,osp.join(tar_root4,new_pic))

            new_json = new_id +'.json'
            copyfile(ori_json,osp.join(tar_root3,new_json))

            new_labelme_json = new_id +'_json'
            destination = osp.join(tar_root2,new_labelme_json)
            if osp.exists(destination):
                rmtree(destination)
            copytree(file_dir, destination)

            i+=1
            
"""
i=1
for dir_name in os.listdir(mypath):
    # construct full file path
    if dir_name.endswith("_json") and dir_name!="labelme_json":
        source = osp.join(mypath,dir_name)
        #print(source)
        destination = tar_root2
        # copy only files
        new_id = f"{i}"
        new_labelme_json = new_id +'_json'
        print(new_labelme_json)
        copytree(source, osp.join(destination,new_labelme_json))
        print(i)
        #os.rename(osp.join(destination,dir_name),osp.join(destination,new_labelme_json))
        i+=1
            #print('copied', file_name) """
print("Done")