"""
# readjson.py



import json_lines


print json_lines.reader(f)
with open('fobsextract.jl', 'rb') as f:
    for item in json_lines.reader(f):
        print(item['x'])

# print((item))

# print(type(item))

	start_urls = json_lines.reader(f)
	print (start_urls)
	print (type(start_urls))

	# for i in range(len(start_urls)):
	# 	start_urls[i] = 'https://www.macys.com'+start_urls[i]
	# 	print(i)
	# print (start_urls)

"""