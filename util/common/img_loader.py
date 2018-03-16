# -*- coding: utf-8 -*-
# 加载房源图片

import os
from PIL import Image

class ImgLoader():
    '''图片加载器'''

    def __init__(self, path="/data/imgs/总门店/1"):
        self.path = path
        self.room_imgs = list()     # 向外输送的图片列表
        self.__load_imgs__          # 图片初始化加载
        self.__check_imgs__         # 检查图片像素大小是否符合要求

    @property
    def __load_imgs__(self):
        
        # 遍历目录下的房源信息图片
        room_imgs_unsorted = list()
        for root, dirs, files in os.walk(self.path):
            for file in files:
                room_imgs_unsorted.append(os.path.abspath(os.path.join(os.getcwd(), root, file)))

        if len(room_imgs_unsorted) == 0:
            raise RuntimeError("图片仓库中没有对应的图片文件，请检查！")

        # 按照 封面图 - 1..6 - 户型图 的顺序对图片列表进行排序
        room_cover_image = str()
        house_type_image = str()

        for img in room_imgs_unsorted:
            if os.path.basename(img).startswith(u"封面图"):
                room_cover_image = img
                continue
            if os.path.basename(img).startswith(u"户型图"):
                house_type_image = img
                continue
            self.room_imgs.append(img)
        if len(room_cover_image) == 0 or len(room_cover_image) == 1:
            raise RuntimeError("图片仓库中没有对应的封面图和户型图")
            
        self.room_imgs.insert(len(self.room_imgs), house_type_image)
        self.room_imgs.insert(0, room_cover_image)

    @property
    def __check_imgs__(self):
        '''检查照片是否符合600x600的像素要求 如果没有则按比例放大像素至最短边为800px'''
        for room_img in self.room_imgs:
            abspath = room_img.split("/")[-1]
            img = Image.open(room_img)
            if img.width <= 600 or img.height <= 600:
                w = img.width
                h = img.height
                t = 0
                if w < h:
                    t = 800/w
                else:
                    t = 800/h
                out = img.resize((int(t*w),int(t*h)),Image.ANTIALIAS)
                out.save(room_img)
            img.close()

if __name__ == "__main__":
    img = ImgLoader()
    print(img.room_imgs)