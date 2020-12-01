#Models
from fake_useragent import UserAgent as u
########
#UserAgent
def UserAgent():
    ua=u()
    return ua.random
