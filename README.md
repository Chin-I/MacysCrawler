# MacysCrawler
Crawl all the product name under Macys

2017.11/13 edited.
Integrated all code to jupyter version.
file name:/MacysCrawler/tutorial/tutorial/spiders/MacysSpider.ipynb
product name Result:/MacysCrawler/tutorial/tutorial/spiders/out-macys-productname.txt


(..)  Crawling Result (..)
Crawl Product Numeber: #25,631  2% (I was banned by Macys.com)
Rough answer is  1,248,000 = 13(Big Category-fob)*40(small category-header)*2400(60item*40pages)
Crawl Hierarchyly from top to down. 
Only problem is the spider, robot, internet issue.

(..)  Crawling Analysis  (..)
Level 1  main url,ex: http://www.macys.com
Level 2  fobs url (13 main category),ex:https://www.macys.com/shop/womens-clothing 
Level 3  headers url (`0~100 detail category of main category),ex:https://www.macys.com/shop/womens-clothing/womens-activewear
Level 4  product url(with category ID,and product ID),ex:https://www.macys.com/shop/product/ideology-cowl-neck-pullover-created-for-macys?ID=4812536&CategoryID=29891
PS:the class productName is unique and only in the product url

(..)Executeive Process(..)
Tool:https://scrapy.org/ , Python3
Create a folder
>> scrapy startproject tutorial
Put this ipnnb unter ~//MacysCrawler/tutorial/tutorial/spiders/
Execute!

(..)Futher Improvement(..)
1.Using Parallel Idea speedup the result.Easy idea is separate 13 crawler for big category link.
2.Using DataBase avoid duplicate result. To avoid racing condition problem.
3.To scalable to other websites. May simply search all html but without duplicate.
4.Optimized the crawler config. To avoid denied access, using differen user agent.
5.Solve duplicate issue.For this version, simple python set is a good idea.

2017.11/10 edited
(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)
(..)             Crawling Analysis                      (..)
(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)

Level 1  main url,ex: http://www.macys.com
Level 2  fobs url (13 main category),ex:https://www.macys.com/shop/womens-clothing 
Level 3  headers url (`0~100 detail category of main category),ex:https://www.macys.com/shop/womens-clothing/womens-activewear
Level 4  product url(with category ID,and product ID),ex:https://www.macys.com/shop/product/ideology-cowl-neck-pullover-created-for-macys?ID=4812536&CategoryID=29891
PS:the class productName is unique and only in the product url

(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)
(..)              Executeive Process                    (..)
(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)
Tool:https://scrapy.org/
Create a folder
>> scrapy startproject tutorial
Use this spider folder to replace the old spider folder.

Filse Path: ~//MacysCrawler/tutorial/tutorial/spiders
All files are commented.
Please execute file at a time.

Step 1    Get All Product Links.
Step 1-1  Get 13 Fob links form https://www.macys.com/
>> scrapy crawl fobs -o fobs.json
get output fobs.json

Step 1-2  Get all header links from Fob links
>> scrapy crawl headers -o headers.json
get output headers.json

Step 1-3  Get all category links from header links 
>> scrapy crawl links -o links.json
get output links.json

ToDo:Bug about next page!

Step 2    Use the products from Step1, out put all the product name.
>> scrapy crawl products -o products.json
get output products.json

(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)
(..)              Futher Improvement                    (..)
(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)(..)

1.Using Parallel Idea speedup the result.
2.Using DataBase avoid duplicate result.
3.To scalable to other websites, the Step1-1 to Step 1-3 process may be different to different websites.
