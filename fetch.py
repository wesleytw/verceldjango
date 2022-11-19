import requests
local = "http://127.0.0.1:3000/api?age=6&gender=1&bp=2&cholesterol=2&salt=7"
replit = "https://verceldjango.wesleyliu4.repl.co/api?age=6&gender=1&bp=2&cholesterol=1&salt=70"

predict = [print(x) for x in requests.post(local)]
predict = [print(x) for x in requests.get(local)]
# predict = [print(x) for x in requests.post(replit)]
