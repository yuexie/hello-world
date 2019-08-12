import sys
import urllib.request
import json

url = 'http://jinxuliang.com/openservice/api/courseservice'
req = urllib.request.Request(url)

content = urllib.request.urlopen(req).read()
res = content.decode('utf-8')

courseJson = json.loads(res)

#print(type(resJson))
#print(len(courseJson))
print(courseJson)

courseNum = 1
for course in courseJson:
	print("Lession." + str(courseNum) + " 课程名称: " + course['courseName'])
	courseNum = courseNum + 1


#课程详细
url = 'http://jinxuliang.com/openservice/api/courseservice/course/54004d84137e45731c99035b'
req = urllib.request.Request(url)

content = urllib.request.urlopen(req).read()
res = content.decode('utf-8')

contentJson = json.loads(res)

print(contentJson)


url = 'http://jinxuliang.com/openservice/api/courseservice/course/54004d84137e45731c99035b/description?needTxt=true'

#test print
print(url)




