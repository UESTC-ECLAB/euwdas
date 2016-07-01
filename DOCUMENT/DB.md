sample
db eclab

collections:
1.user
{ 	
	"_id" : ObjectId("577105f268836322a47a5bd2"), 
	"username" : "yinruyi", 
	"verified" : 0, 
	"userid" : 0, 
	"avatar" : "/static/images/avatar/default/default_1.png", 
	"password" : "a63f88b993f9dae603b3dd2703da916e16d9ed0f", 
	"email" : "916280067@qq.com", 
	"createdAt" : "2016-06-27 18:54:42" 
}

2.news
http://forum.memect.com/page/1/
{
	"_id" : ObjectId("577105f268836322a47a5bd2"),
	"news_id" : 567,
	"title" : "用Python构建图片处理搜索引擎",
	"tag" : ["头条","Python"],
	"author" : "36大数据网"，
	"content" : "【用Python构建图片处理搜索引擎】有很多顶级的科技公司把RIQ用得很好。例如，Pinterest 2014年第一次实现视觉搜索。随后2015年它发布了一个白皮书，揭示了视觉搜索的结构。反向图片搜索使得Pinterest能够从时尚的东西中提取视觉元素，然后给消费者推荐类似的产品。",
	"url" : "http://t.cn/R5QWLSo",
	"original_url" : "http://forum.memect.com/blog/thread/py-2016-06-29-3991742447606905/",
	"image_url" : ["http://ww4.sinaimg.cn/large/cdda9064jw1f5c6ec7tzlj20hr0b6weq.jpg"],
	"news_avatar" : "/static/images/avatar/default/news_1.png"
}

3.newstag
{
	"_id" : ObjectId("577105f268836322a47a5bd2"),
	"tag" : "Python",
	"news_id" : 567
}

4.newsread
{
	"_id" : ObjectId("577105f268836322a47a5bd2"),
	"news_id" : 567,
	"ip_address" : 119.56.1.12,
	"username" : "yinruyi",
	"userid" : 0,
	"isanonymous" : 0,
}