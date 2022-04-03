from PIL import Image
import os.path
import glob


def convertjpg(jpgfile, outdir, width=224, height=224):
    img = Image.open(jpgfile)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        if new_img.mode == 'P':
            new_img = new_img.convert("RGB")
        if new_img.mode == 'RGBA':
            new_img = new_img.convert("RGB")
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    except Exception as e:
        print(e)


for jpgfile in glob.glob("G:/+1/22毕设/image/未处理/_mask/normal/*.png"):
    print(jpgfile)
    convertjpg(jpgfile, "G:/+1/22毕设/image/TrainData/Decision_TrainData/normal")
