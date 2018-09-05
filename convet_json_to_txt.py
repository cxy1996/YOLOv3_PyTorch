from pycocotools.coco import COCO
from numpy import *
import os
import pdb
import json

data_dir = '/data1/cxy/coco/annotations/instances_val2017.json'
output_caronly_dir = '/home/cxy/yolov3/data/coco/labels/val2017'

if not os.path.exists(output_caronly_dir):
    os.makedirs(output_caronly_dir)

# initialize COCO api for instance annotations
coco = COCO(data_dir)

index2category = json.load(open("./evaluate/coco_index2category.json"))
c2ind = {}
for i in range(len(index2category)):
    c2ind[str(index2category[str(i)])] = int(i)

imgs = coco.loadImgs(list(coco.imgs.keys()))
for k, img in enumerate(imgs):
    print('[%6d/%6d] %s' % (k, len(imgs), img['file_name']))
    h = img['height']
    w = img['width']
    anns = coco.loadAnns(coco.getAnnIds(imgIds=img['id']))

    image_name, image_ext= os.path.splitext(img['file_name'])

    if anns != []:
        result_file_car_only = open(
            os.path.join(output_caronly_dir,
                    img['file_name'].replace(image_ext, '.txt')), 'w')


    for ann in anns:
        category = ann['category_id']
        bbox = ann['bbox']
        result_file_car_only.write(
            "%d %.6f %.6f %.6f %.6f\n"
            % (c2ind[str(category)], (bbox[0]+bbox[2]/2)/w, (bbox[1]+bbox[3]/2)/h, bbox[2]/w, bbox[3]/h))
