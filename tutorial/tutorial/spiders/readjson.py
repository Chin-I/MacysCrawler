"""
# readjson.py
import json
print("hom!!!!!!!!!!!!!!!!!!!!")
a =json.load(open('fobsextract.json'))
# #print (a)
# print (type(a))
# #print (a[0])
# print (type(a[0]))
# # print len(a)
# print (type(a[0]['fob']))
# print (a[0]['fob'])

start_urls = json.load(open('fobsextract.json'))[0]['fob']
print (start_urls)

for i in range(len(start_urls)):
	start_urls[i] = 'https://www.macys.com'+start_urls[i]
	print(i)
	# print(type(i))
print("!!!!!!!!!!!!!!!!!!!!")

print (start_urls)
"""