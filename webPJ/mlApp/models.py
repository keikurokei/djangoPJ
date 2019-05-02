from django.db import models
import uuid,os

def get_image_path(self,filename):
    """カスタマイズした画像パスを取得する.

    :param filename: 元ファイル名
    :return: カスタマイズしたファイル名を含む画像パス
    """
    prefix = 'mlApp/'
    name = str(uuid.uuid4()).replace('-', '')
    extension = os.path.splitext(filename)[-1]
    return prefix + name + extension    

class Photo(models.Model):
    image = models.ImageField(upload_to=get_image_path)

