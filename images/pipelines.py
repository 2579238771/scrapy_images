# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.media import MediaPipeline

class OverFilePipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        filename = request.url.split('/')[-1]
        if '.' not in filename:
            filename = filename + '.png'
            print(filename,'***'*30)
        return 'pexels/%s'%filename

class ImagesPipeline(object):
    def process_item(self, item, spider):
        # tmp = item['image_urls']
        # item['image_urls'] = []
        # for i in tmp:
        #     if '?' in i:
        #         item['image_urls'].append(i.split('?')[0])
        #     else:
        #         item['image_urls'].appen(i)
        # print(item['image_urls'])
        tmp = item['file_urls']
        item['file_urls'] = []
        for i in tmp:
            if '?' in i:
                item['file_urls'].append(i.split('?')[0])
            else:
                item['file_urls'].appen(i)
        print(item['file_urls'])
        return item
