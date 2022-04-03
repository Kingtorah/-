import PIL.Image as Image
import os

path = r"G:\+1\22毕设\image\Traindata\Seg_Traindata\mask"
save_path = r"G:\+1\5"
for i in os.listdir(path):
    img = Image.open(os.path.join(path, i)).convert('RGB')
    img.save(os.path.join(save_path, i))
