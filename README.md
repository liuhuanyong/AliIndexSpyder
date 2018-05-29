# AliIndexSpyder
self complemented AlindexSpyder based on Selenium ，阿里商品指数抓取，包括淘宝采购指数，淘宝供应指数，1688供应指数。
# AliIndexSpyder
self complemented AlindexSpyder based on Selenium ，阿里商品指数抓取，包括淘宝采购指数，淘宝供应指数，1688供应指数。

# 项目介绍
1、阿里指数 是了解电子商务平台市场动向的数据分析平台，2012年11月26日，阿里指数正式上线。根据阿里巴巴网站每日运营的基本数据包括每天网站浏览量、每天浏览的人次、每天新增供求产品数、新增公司数和产品数这5项指标统计计算得出。  
2、阿里指数对于收录的商品关键词，在指数方面提供阿里商品指数抓取，包括淘宝采购指数，淘宝供应指数，1688供应指数三个指数，基于三个指数，可以在一定程度上反映出该商品的供需行情，与商品的价格相比，能够得出一些相关性的结论。

# 项目举例
以‘连衣裙’这一商品关键词为例，要求获取连衣裙的三个指数数据。由于阿里指数至提供近一年的指数数据，因此，只能采集一年的数据，原始结果如下：  
 ![image](https://github.com/liuhuanyong/AliIndexSpyder/blob/master/img/ali_index.png)

# 实现流程
    def index_main(self, word):
        print('step1, open page....')
        #使用selenium，打开页面，获取指数数据所在页面
        page_source = self.search_index(word)
        print('step2, get data....')
        #解析原网页，获取purchase_index_1688, supply_index, purchase_index_tb
        purchase_index_1688, supply_index, purchase_index_tb = self.data_parser(page_source)
        #以本地文件的方式保存结果，分别写入到purchase_index_1688, supply_index, purchase_index_tb三个文件中
        self.output_data(word, purchase_index_1688, supply_index, purchase_index_tb)
        print('step3, %s finished....'% word)
# 执行
     def demo():
         ali = AliIndex()
         search_word = '连衣裙'
         ali.index_main(search_word)
     demo()
# 效果
将得到的数据文件，进行本地可视化，效果如下：
 ![image](https://github.com/liuhuanyong/AliIndexSpyder/blob/master/img/ali_index_local.png)

# 总结
1、阿里指数的采集较为简单，1)阿里指数直接将历时数据写在前端页面中，可以直接解析获得。2)无需用户登录。    
2、阿里指数与百度指数不同，其对应的关键词实体需要对应到具体的行业或商品上，而用户查询的关键词具有多样性，这样会导致可能无法正确获取严格的关键词商品指数，如搜索iphone，会得到电子产品的指数。  
3、比较遗憾的是，阿里指数只提供以查询当日为结束如日，往前推一年为开始日期的数据，对于历时数据的构建来说，不是太方便。  
