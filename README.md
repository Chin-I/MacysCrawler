# MacysCrawler
Crawl all the product name under Macys

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
