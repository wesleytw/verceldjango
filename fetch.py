import requests
local = "http://127.0.0.1:8000/api?age=68&gender=0&bp=2&cholesterol=2&salt=2&model=svm"
replit = "https://verceldjango.wesleyliu4.repl.co/api?age=6&gender=1&bp=2&cholesterol=1&salt=70"

predict = [print(x) for x in requests.post(local)]
predict = [print(x) for x in requests.get(local)]
# predict = [print(x) for x in requests.post(replit)]
