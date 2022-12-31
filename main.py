import sys , os , random , requests , time , pyperclip
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy , ProxyType
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#color

class color:
   PURPLE = '\033[95m'
   GREEN = '\033[92m'
   BOLD = '\033[1m'
   CWHITE  = '\33[37m'
   
print(color.BOLD)
         
#Fake useragent
options = Options()
ua = UserAgent()
userAgent = ua.random

options.add_argument(f'user-agent={userAgent}')

#Headless mode (set as true to use)
options.headless = False

#Don't close the browser
options.add_experimental_option("detach", True)

#Proxy (highly required)

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL

prox.http_proxy = "138.36.180.9:9292"
prox.socks_proxy = ""
prox.ssl_proxy = ""

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities) # Remove '#' to use proxy


#webdriver

url = "https://www.instagram.com/accounts/emailsignup/"
CHROME_DIR = ""
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"   # Do not wait for full page load

browser = webdriver.Chrome(desired_capabilities=caps)

print()
print( color.GREEN + "[+] " + color.CWHITE + "Using useragent as : " + userAgent)

#Open ig signup url

url = "https://www.instagram.com/accounts/emailsignup/"
browser.get(url)

#elements

time.sleep(3.517)
email = browser.find_element(By.NAME, 'emailOrPhone')
fullname = browser.find_element(By.NAME, 'fullName')
username = browser.find_element(By.NAME, 'username')
Password = browser.find_element(By.NAME, 'password')
signup_button = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/button')

# Create temporary email

browser.execute_script("window.open('');")

browser.switch_to.window(browser.window_handles[1])

browser.get("https://mail.tm/ko/")
time.sleep(7)

copy_button = browser.find_element(By.ID, "DontUseWEBuseAPI")

copy_button.click()

generated_email = pyperclip.paste()

print()
print( color.GREEN + "[!] " + color.CWHITE + "Generated Email : " + generated_email)

browser.switch_to.window(browser.window_handles[0])

#Create Random username

time.sleep(0.500)

username_file = open(os.getcwd() + '/usernames.txt', "r")

lines_read = username_file.readlines()

lines = [line.rstrip('\n') for line in lines_read]

chose_random_username_list = random.sample(lines, k=1)

random_username_string = ''.join(chose_random_username_list)

random_username_number = str(random.randint(100000, 200000))

generated_random_username = random_username_string + random_username_number

print( color.GREEN + "[!] " + color.CWHITE +"Generated username = " + generated_random_username)

#Create random password to avoid detection (not really required)

time.sleep(0.500)

chose_random_password_list = random.sample(lines, k=1)

random_password_string = ''.join(chose_random_password_list)

random_password_number = str(random.randint(10000, 20000))

generated_random_password = random_password_string + random_password_number

print( color.GREEN + "[!] " + color.CWHITE +"Generated password = " + generated_random_password)

#Fields to use 

my_email = generated_email
my_fullname = 'BOT KILLER'
my_username = generated_random_username
my_password = generated_random_password

#Fill the page

email.send_keys(my_email)
time.sleep(0.517)
fullname.send_keys(my_fullname)
time.sleep(0.312)
username.send_keys(my_username)
time.sleep(0.125)
Password.send_keys(generated_random_password)
time.sleep(2)
Password.send_keys(Keys.ENTER)
time.sleep(5)

#elements next page

birthday_month = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[5]')
birthday_day = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]')
birthday_year = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[35]')
birthday_next_button = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[6]/button')

#Fill the page

birthday_month.click()
time.sleep(0.120)
birthday_day.click()
time.sleep(0.114)
birthday_year.click()
time.sleep(2)
birthday_next_button.click()

#Display countdown

browser.switch_to.window(browser.window_handles[1])
print()
print(color.GREEN + "[!] " + color.CWHITE + "Waiting for otp ")

print(color.GREEN + "[!] " + color.CWHITE + "Opening mail box in 15 seconds")

for remaining in range(15, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\rComplete!            \n")
browser.refresh()
time.sleep(2)

# otp page element

read_otp = browser.find_element(By.CSS_SELECTOR, '#__layout > div > div.flex.flex-1.flex-col.w-0.overflow-hidden > main > div > div.mt-6.dark\:bg-gray-800.bg-white.shadow.overflow-hidden.sm\:rounded-md > ul > li > a > div > div.flex.flex-1.items-center.min-w-0 > div.flex-1.px-4.min-w-0.md\:grid.md\:gap-4.md\:grid-cols-2 > div.hidden.md\:block > div > div.dark\:text-gray-300.text-gray-900.text-sm.leading-5.truncate').text

# Read otp from mail

# Save response to response.Text

with open("response.text","w") as file:
   file.write(str(read_otp))

read_otp_file = open("response.text")

lines = read_otp_file.readlines()

for line in lines:
   my_otp = str(line[0:6])

print(color.GREEN + "[!] " + color.CWHITE + "OTP Recieved : " + my_otp)

# fill otp

browser.switch_to.window(browser.window_handles[0])
time.sleep(1)
fill_otp = browser.find_element(By.NAME,'email_confirmation_code')

fill_otp.send_keys(my_otp)
time.sleep(2)
fill_otp.send_keys(Keys.ENTER)
time.sleep(4)

Terms = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[3]/div[1]/div[2]/input')
nexter = browser.find_element(By.XPATH , '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/button')

Terms.click()
nexter.click()

time.sleep(15)
# Write generated account

print(color.GREEN + '[!] ' + color.CWHITE + 'Saving account info as account_generated.txt ')
print()

with open("account_generated.txt","a+") as file:

      file.write("\n")
      file.write(my_email + " : " + my_password)
