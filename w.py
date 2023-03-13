# for i in range(10,20):
#     if i%2==0:
#         print("even no.",i,"sq:",i**2)
#     elif i%2!=0:
#         print("odd no.",i,"cu:",i**3)
        

# a=[4,5,6,[3,4,5],2]
# b=[]
# i=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         c=[]
#         while j<len(a[i]):
#             d=a[i]*a[i][j]
#             c.append(d)
#         j=j+1
#     i=i+1
#     print(c)
    
            
# a=["my n@ame is# pan123@kaja","i @am in 123india "]
# b=[]
# i=0
# while i<len(a):
#     j=0
#     s=""
#     while j<len(a[i]):
#         if a[i][j]>="a" and a[i][j]<="z":
#             s=s+a[i][j]
#         elif a[i][j]==" ":
#             s+=" "
#         j=j+1
#     # print(s)
#     b.append(s)
#     i=i+1
# print(b)

  
# a=[1012,20116,5016,24131]
# i=0
# sum=0
# b=[]
# while i<len(a):
#     c=str(a[i])
#     j=0
#     sum=0
#     while j<len(c):
#         if c[j]!="1":
#             sum=sum+(int(c[j]))
#         j=j+1
#     b.append(sum)
#     i=i+1
# print(b)


# a=[1012,20116,5016,24131]
# i=0
# sum=1
# b=[]
# while i<len(a):
#     c=str(a[i])
#     j=0
#     sum=1
#     while j<len(c):
#         if c[j]!="0":
#             sum=sum*(int(c[j]))
#         j=j+1
#     b.append(sum)
#     i=i+1
# print(b)

# a=[1012,20116,5016,24131]
# i=0
# s=1
# b=[]
# while i<len(a):
#     c=str(a[i])
#     j=0
#     while j<len(c):
#         s=1
#         if c[j]!="0":
#             s=s*(int(c[j]))
#             # b.append(s)
#         j+=1
#     b.append(s)
#     i+=1
# print(b)


# request api chaya

import requests
import json
url1=requests.get("https://api.merakilearn.org/courses")
var1=url1.json()
with open("cources.json","w") as f:
    json.dump(var1,f,indent=4)
serial_no=0
for i in var1:
    print(serial_no+1,i["name"],i["id"])
    serial_no+=1
course_no=int(input("enter your course number which you want to learn:-"))
print(var1[course_no-1]["name"],var1[course_no-1]["id"])
a=var1[course_no-1]["id"]
url2=requests.get("http://api.merakilearn.org/courses/"+str(a)+"/exercises")
var2=url2.json()
with open("topic.json","w") as f:
    json.dump(var2,f,indent=4)
s_no=1
main_point=[]
sub_point=[]
for j in var2["course"]["exercises"]:
    if j["parent_exercise_id"]==None:
        print(s_no,j["name"])
        print("   ",1,j["slug"])
        s_no+=1 
        main_point.append(j)
        sub_point.append(j)
        continue    
    if j["parent_exercise_id"]==j["id"]:
        print(s_no,j["name"])
        main_point.append(j)
        s_no+=1 
        c=1
    for i in  var2["course"]["exercises"]:
        if j["parent_exercise_id"]!=j["id"]:
            print("   ",c,j["name"])
            sub_point.append(j)
            c+=1
            break
# with open("point.json","w") as q:
#     json.dump(main_point,q,indent=4)
topic_no=int(input("choose topic:-"))
for k in range(0,len(main_point)):
    if topic_no==k+1:
        print(topic_no,main_point[k]["name"])
        print(main_point[k]["content"])
        a=main_point[k]["parent_exercise_id"]
s=1
name=[]
content=[]
for d in range(0,len(sub_point)):
    if sub_point[d]["parent_exercise_id"]==a:
        print("   ",s,sub_point[d]["name"])
        name.append(sub_point[d]["name"])
        content.append(sub_point[d]["content"])
        s+=1
point=int(input("choose a point:-"))
y=1
for i in range(0,len(name)):
    if point==y:
        print(name[i])
        print(content[i])
        print()
    y+=1

# api request mm

# import requests
# import json

# url=requests.get("https://api.merakilearn.org/courses")
# data=url.json()
# with open("courses1.json","w") as file:
#     json.dump(data,file,indent=4)
# i=0
# while i<len(data):
#     print(i+1,")",data[i]["name"],":",data[i]["id"])
#     i=i+1
# user=int(input("enter which programme do you want:"))
# print(data[user-1]["name"],":",data[user-1]["id"])
# content_file=data[user-1]["name"]+"_"+data[user-1]["id"]
# link="http://api.merakilearn.org/courses/"+data[user-1]["id"]+"/exercises"
# url1=requests.get(link)
# data1=url1.json()
# with open(content_file,"w") as file1:
#     json.dump(data1,file1,indent=4)

# i=0
# while i<len(data1["course"]["exercises"]):
#     print(i+1,")",data1["course"]["exercises"][i]["name"])
#     i=i+1

# topic=int(input("Enter topic number whichever you want:"))
# topic_index=topic-1
# i=0
# while i<len(data1["course"]["exercises"][topic_index]["content"]):
#     print(data1["course"]["exercises"][topic_index]["content"][i]["value"])
#     i=i+1

# while topic_index<=len(data1["course"]["exercises"]):
#     next_privious=input("Enter Next or Privious n/p :")
#     if next_privious=="p":
#         topic_index=topic_index-1
#         if 1<=topic_index:
#             print(data1["course"]["exercises"][topic_index]["name"])
#             i=0
#             while i<len(data1["course"]["exercises"][topic_index]["content"]):
#                 print(data1["course"]["exercises"][topic_index]["content"][i]["value"])
#                 i=i+1
#         elif topic_index==0:
#             print(data1["course"]["exercises"][topic_index]["name"])
#             i=0
#             while i<len(data1["course"]["exercises"][topic_index]["content"]):
#                 print(data1["course"]["exercises"][topic_index]["content"][i]["value"])
#                 i=i+1
#         else:
#             print("finished")
#             break
#     elif next_privious=="n":
#         topic_index=topic_index+1
#         if topic_index<len(data1["course"]["exercises"]):
#             print(data1["course"]["exercises"][topic_index]["name"])
#             i=0
#             while i<len(data1["course"]["exercises"][topic_index]["content"]):
#                 print(data1["course"]["exercises"][topic_index]["content"][i]["value"])
#                 i=i+1
#         if topic_index==len(data1["course"]["exercises"]):
#             print("Topic is completed")
#             break
#     else:
#         print("user input is wrong:")
#         break