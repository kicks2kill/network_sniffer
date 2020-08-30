import http.cookiejar
import urllib
URL = input("Please enter a URL that begins with Http:// --> ")

def extract_cookie_info():
    #setup the cookie jar
    cookie_j = http.cookiejar.CookieJar()
    #create url opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_j))
    #now access without any login info
    resp = opener.open(URL)
    for cookie in cookie_j:
        print("Cookie: %s --> %s" %(cookie.name, cookie.value))
    print("Headers: %s" %resp.headers)

if __name__ == '__main__':
    extract_cookie_info()