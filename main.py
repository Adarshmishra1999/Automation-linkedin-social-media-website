from selenium import webdriver
import pandas as pd

var = webdriver.Chrome(executable_path="C:\\Users\\shivm\\PycharmProjects\\pythonProject\\pythonProject3\\chromedriver.exe")
df = pd.read_csv("autolinkdin.csv", encoding="utf-8")

myuser = df.username[0]
mypass = df.password[0]
mypost = df.posts[0]

print(mypost)


var.get("https://www.linkedin.com/login?")

##############################################################

#locate user from id#
#user = var.find_element_by_id("username")
#locate user bfrom by_name#
user = var.find_element_by_name("session_key")
user.send_keys(myuser)

############################################################

#locate pass from id#
#pwd = var.find_element_by_id("password")
#locate pass from by_name#
pwd = var.find_element_by_name("session_password")
pwd.send_keys(mypass)

#############################################################

#locate submit button from x_path#
#log_in_button = var.find_element_by_xpath("//*[@type='submit']")
#locate submit button by_class_name#
log_in_button = var.find_element_by_class_name("btn__primary--large")
log_in_button.click()

##################################################################

# List of user, pass, post #
myuser = ["abc@gmail.com"]
mypass = ["abcpass"]
mypost = ["hello everyone,"
          "this is a automation linkdin project using selenium and chrome web driver"]
# dictionary of the lists #
dict = {"username":myuser, "password":mypass, "posts":mypost}

df = pd.DataFrame(dict)

# saving the dataframe #
df.to_csv("autolinkdin.csv",index=False)

#######################################################################################

post_button = var.find_element_by_id("ember808")
post_button.click()

#make_post = var.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]')
#make_post.send_keys(mypost)




