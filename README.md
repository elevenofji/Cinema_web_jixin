

# 已完成

1.非常简单的新增了登录界面，可以注册或登录了，此外接spark；

2.配置了xadmin，可直接修改表信息，需要
   python install -r requirements.txt
   python manage.py createsuperuser
 而后直接127.0.0.1:8000/xadmin即可，建立了包括默认推荐表，电影信息表，电影相似度表，电影-用户打分评论表和用户信息表
 重新建表时参考https://github.com/JimXiongGM/MovieRecOnline
 
 3.修改了和增加了部分static和templates中的文件，并将它们放在了根目录下，方便使用
 
 4.离线推荐算法已完成（未放在cinima_pages里的models中，后续会加上）。
 
 # 未解决：
 
 1.电影信息目前只用mysql存，需要改成Hbase
 
 2.页面过于简陋，需要修改（若无对boostrap等较为熟悉的 我可以负责）
 
 3.电影信息未入库，离线推荐功能未完全测验
 
 4.在线推荐（待定）
