#Models.
import requests as r , time , Logo , Color as c , UserAgent as users 
######
#Globals Value
url="https://Instagram.com"
########
#Inputs File
proxy=open(input(f"{c.C}Proxy{c.R}_{c.C}List {c.R}=> {c.C}{c.W}"),"r")
#######
#Check
def Check():
    try:
        for i in proxy:
            i=i.strip()
            i=i.split(":")
            ip=i[0]
            port=i[1]
            addr=dict(http=f"http://{ip}:{port}",https=f"https://{ip}:{port}")
            head={"User-Agent":users.UserAgent()}
            try:
                req=r.get(url, proxies=addr, headers=head, timeout=6)
            except Exception as e:
                if "HTTPTunel" in str(e):
                    continue
                else:
                    print(f"{c.R}Error{c.C}!!!{c.W} {e}\n")
                    exit()
            if req.status_code == 200:
                print(f"{c.C}Hit{c.R}_{c.C}Proxy {c.R}=> {c.C}{ip}:{port}{c.W}\n")
                files=open("Hit.txt","a+")
                files.write(f"{i}\n")
                files.close()
            else:
                print(f"{c.C}Not{c.R}_{c.C}Found {c.R}=> {c.C}{ip}:{port}{c.W}\n")
    except Exception as e:
        print(f"{c.R}Error{c.C}!!!{c.W} {e}\n")
        exit()
    #else:
        #print(f"{c.C}Bad Proxy{c.R}!!!{c.W}\n")

Check()
