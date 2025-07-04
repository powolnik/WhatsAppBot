from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import tempfile
# import winsound
import time

chrome_options = Options()
# 
user_data_dir = os.path.join(tempfile.gettempdir(), "wa_bot_data")
os.makedirs(user_data_dir, exist_ok=True)
    
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--headless=new")  # Remove if you want visible browser
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

os.system("/workspaces/WhatsAppBot/script.bat")
opt = Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
#Enter the target number in the target variable. Example +923335141414
target = "+923335141414"
string = "Testing whatsapp automation python"
x_arg = '//*[@id="side"]/div[1]/div/label/div/div[2]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
# winsound.Beep(700, 800)
group_title.click()
group_title.send_keys(target+Keys.ENTER)
inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
input_box.send_keys("Test successful" + Keys.ENTER)
time.sleep(4)
driver.close()

# # Standard library imports
# import os
# import io
# import base64
# import tempfile
# import shutil
# from time import sleep

# # Third-party imports
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from PIL import Image
# class WABot:
#     WHATSAPP_URL = "https://web.whatsapp.com"
#     QR_CODE_FILENAME = "whatsapp_qr.png"
#     DEFAULT_TIMEOUT = 5  # Increased from 3 to more realistic timeout

#     def __init__(self):
#         """Initialize WhatsApp Bot with Chrome WebDriver"""
#         chrome_options = Options()
        
#         # Create unique temporary directory
#         self.user_data_dir = os.path.join(tempfile.gettempdir(), "wa_bot_data")
#         os.makedirs(self.user_data_dir, exist_ok=True)
        
#         chrome_options.add_argument(f"--user-data-dir={self.user_data_dir}")
#         chrome_options.add_argument("--profile-directory=Default")
#         chrome_options.add_argument("--headless=new")  # Remove if you want visible browser
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-dev-shm-usage")

#         self.driver = webdriver.Chrome(options=chrome_options)

        
#     def save_qr_code(self, qr_element):
#         """Save QR code as image and display it for scanning"""
#         try:
#             # Save as file
#             qr_element.screenshot(self.QR_CODE_FILENAME)
#             print(f"QR code saved as '{self.QR_CODE_FILENAME}'")
            
#             # Display using PIL
#             qr_base64 = qr_element.screenshot_as_base64
#             qr_bytes = base64.b64decode(qr_base64)
#             img = Image.open(io.BytesIO(qr_bytes))
#             img.show()
            
#             print("Please scan the QR code with WhatsApp on your phone")
#             return True
#         except Exception as e:
#             print(f"Failed to handle QR code: {str(e)}")
#             return False

#     def _wait_for_element(self, wait, selector):
#         """Helper method to wait for and find an element"""
#         try:
#             wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
#             return True
#         except:
#             return False

#     def _handle_qr_login(self, wait):
#         """Handle QR code login process"""
#         try:
#             qr_code = wait.until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="qrcode"]'))
#             )
#             if not self.save_qr_code(qr_code):
#                 return False
                
#             # Wait for successful login after QR scan
#             if self._wait_for_element(wait, '[data-testid="chat-list"]'):
#                 print("Successfully connected after QR scan!")
#                 return True
                
#             print("QR code scan timeout or failed")
#             return False
#         except:
#             print("Failed to handle QR code login")
#             return False

#     def connect_to_whatsapp(self):
#         """Connect to WhatsApp Web and handle authentication"""
#         try:
#             print("Connecting to WhatsApp Web...")
#             self.driver.get(self.WHATSAPP_URL)
#             wait = WebDriverWait(self.driver, self.DEFAULT_TIMEOUT)
            
#             # Check for existing session
#             if self._wait_for_element(wait, '[data-testid="chat-list"]'):
#                 print("Successfully connected using existing session!")
#                 return True
                
#             # Handle new login with QR code
#             if self._handle_qr_login(wait):
#                 return True
                
#             return False
            
#         except Exception as e:
#             print(f"Connection failed: {str(e)}")
#             return False
            
#     def quit(self):
#         self.driver.quit()
   
#     def __del__(self):
#         if hasattr(self, 'driver'):
#             self.driver.quit()
#         if os.path.exists(self.user_data_dir):
#             shutil.rmtree(self.user_data_dir, ignore_errors=True)

# if __name__ == "__main__":
#     bot = WABot()
#     bot.connect_to_whatsapp()
#     # Keep the browser open for a while to see the result
#     sleep(3)
#     bot.quit()
