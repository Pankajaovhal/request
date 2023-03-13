import requests
import json
url1=requests.get('https://api.merakilearn.org/courses')
var1=json.loads(url1.text)
with open("parent.json","w") as f:
    json.dump(var1,f,indent=4)
i=0
while i<len(var1):
    print(i,var1[i]["name"],var1[i]["id"])
    i+=1
course_no=int(input("Enter which course you want:"))
print(var1[course_no-1]["name"],var1[course_no-1]["id"])
id=(var1[course_no-1]["id"])
url2=requests.get("http://api.merakilearn.org/courses/"+str(id)+"/exercises")
var2=url2.json()
print(var2)
with open("data.json","w") as a:
   file_2= json.dump(var2,a,indent=4)
# print(var[course_no-1]["name"],"-",var[course_no-1]["id"])
serial1=1
serial2=1
main_point=[]
sub_point=[]
n=1
for j in var2["course"]["exercises"]:
    if j["parent_exercise_id"]==None:
        print(serial1,j["name"])
        print(" ",serial1,j["slug"])
        serial2+=1
        main_point.append(j)
        sub_point.append(j)
        continue
    if j["parent_exercise_id"]==j["id"]:
        print(serial2,j["name"])
        serial1+=1
        # new_number=1
        main_point.append(j)
        # n=1
    if j["parent_exercise_id"]!=j["id"]:
        print(" ",n,j["name"])
        n+=1
        sub_point.append(j)
        break
with open("point.json","w") as q:
    json.dump(main_point,q,indent=3)
with open("point2.json","w") as r:
    json.dump(sub_point,r,indent=4)
topic_no=int(input("choose topic:"))
for k in range(0,len(main_point)):
    if topic_no==k+1:
        print(topic_no,main_point[k]["name"])
        print(" ",main_point[k]["content"])
        id=main_point[k]["parent_exercise_id"]
        