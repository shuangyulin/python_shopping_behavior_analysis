# 数据容器文件

import scrapy

class SpiderItem(scrapy.Item):
    pass

class GouwurizhiItem(scrapy.Item):
    # 购买者ID
    uid = scrapy.Field()
    # 商品ID
    goodsid = scrapy.Field()
    # 商品类目ID
    goodstypeid = scrapy.Field()
    # 行为类型
    userbehavior = scrapy.Field()
    # 时间戳
    shijianchuo = scrapy.Field()

