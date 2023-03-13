import requests
import json
url=requests.get("https://api.merakilearn.org/courses")
var=json.loads(url.text)
with open("course.json","w") as f:
    json.dump(var,f,indent=4)
sr=1
while sr<len(var):
    print(sr,var[sr]["name"],var[sr]["id"])
    sr+=1
cnum=int(input("enter course number you want:"))
print(var[cnum-1]["name"],var[cnum-1]["id"])
id=(var[cnum-1]["id"])
url2=requests.get("http://api.merakilearn.org/courses/"+str(id)+"/exercises")
var2=url2.json()
print(var2)
with open("sub_courses.json","w") as f:
    json.dump(var2,f,indent=4)
s_no=1
main_point=[]
sub_point=[]
n=1
for i in var2["course"]["exercises"]:
    if i["parent_exercise_id"]==None:
        print(s_no,i["name"])
        print(" ",s_no,i["slug"])
        s_no+=1
        main_point.append(i)
        sub_point.append(i)
        continue
    if i["parent_exercise_id"]==i["id"]:
        print(s_no,i["name"])
        main_point.append(i)
    if i["parent_exercise_id"]!=i["id"]:
        print(" ",n,i["name"])
        n+=1
        break
with open("main.json","w") as q:
    json.dump(main_point,q,indent=4)
with open("sub.json","w") as r:
    json.dump(sub_point,r,indent=4)
c=int(input("enter choosen topic number:"))
