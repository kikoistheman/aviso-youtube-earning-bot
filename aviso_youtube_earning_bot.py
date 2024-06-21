from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Test:
    def __init__(self):
        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument("--mute-audio")
        self.driver = webdriver.Chrome(options=self.options)
        
        self.driver.get("https://aviso.bz/login")
        sleep(3)
        # put your aviso.bz username and password her
        username = "aviso_username"
        password = "aviso_pass"
        # Add the login steps
        self.login(username, password)
        self.check_code_field()
        print(self.driver.title)
    
        # Navigate to the desired page
        self.driver.get("https://aviso.bz/work-youtube")
        self.driver.get_screenshot_as_file('screenshot3.png')
        
        # Check for the code input field and ask for the code if present
        
        
        # Click on dynamic elements
        self.click_dynamic_elements()

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)

        # Locate the username and password fields by name and enter the credentials
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))  # Adjust name attribute if needed
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))  # Adjust name attribute if needed

        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the form
        password_field.send_keys(Keys.RETURN)
        sleep(5)
    
    def check_code_field(self):
        wait = WebDriverWait(self.driver, 10)
        
        try:
            # Check if the code field is present
            code_field = wait.until(EC.presence_of_element_located((By.NAME, "code")))
            if code_field:
                code = input("Enter the code sent to kzezo4919: ")
                self.code(code)
        except:
            # If the code field is not present, continue without asking for the code
            pass
        
    def code(self, code):
        wait = WebDriverWait(self.driver, 10)

        code_field = wait.until(EC.presence_of_element_located((By.NAME, "code")))
        code_field.send_keys(code)
        code_field.send_keys(Keys.RETURN)

    def click_dynamic_elements(self):
        wait = WebDriverWait(self.driver, 10)

        while True:
            # Refresh the page to get the latest elements
            self.driver.get("https://aviso.bz/work-youtube")
            sleep(2)  # Adjust the sleep time if needed

            try:
                # Find the first element with an ID that starts with 'link_ads_start_'
                element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[starts-with(@id, 'link_ads_start_')]")))
                element2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[starts-with(@id, 'new-money-ballans')]")))
                text = element2.text
                number_str = text.split(' ')[0]
                number = float(number_str)
                result = number * 0.011
                


                print("USD BALANCE IS: ", result,"","USD")

                
                sleep(2)

                if element:
                    # Click on the element
                    print(f"Clicking on element with ID: {element.get_attribute('id')}")
                    element.click()
                    print("Element clicked.")

                    sleep(4)  # Wait for the video to load, adjust if needed
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    element3 = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[starts-with(@id, 'tmr')]")))
                    time = element3.text
                    print(time)  # Switch to the last opened window

                    wait = WebDriverWait(self.driver, 50)
                    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[starts-with(@id, 'video-start')]")))
                    if element:
                        print("found")
                        print(element.get_attribute('id'))
                        element.click()
                        print(f"sleeping for {time} seconds")
                        sleep(int(time) + 5)
                    
                    self.driver.get_screenshot_as_file('screenshot4.png')
                    sleep(3)

                    # Close the tab
                    self.driver.close()

                    # Switch back to the main tab
                    self.driver.switch_to.window(self.driver.window_handles[0])

                else:
                    print("Element not found or not clickable.")

            except Exception as e:
                print(f"Could not click element: {e}")

# Initialize the Test class
Test()
