from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import time

class FormAutomation:
    def __init__(self):
        self.service = Service('chromedriver')  
        self.driver = webdriver.Chrome(service=self.service)
        
    def verify_email(self, expected_email):
        email_field = self.driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i11 i14']")
        actual_email = email_field.get_attribute('value')
        if actual_email != expected_email:
            print(f"Email mismatch! Fixing...")
            email_field.clear()
            email_field.send_keys(expected_email)
            time.sleep(1)
        return True

    def fill_form(self, form_data):
        try:
            # Open the Google Form
            self.driver.get("https://forms.gle/WT68aV5UnPajeoSc8")
            
            # Wait for form to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "whsOnd"))
            )
            
            # Fill Full Name
            self.driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i1 i4']").send_keys(form_data['full_name'])
            
            # Fill Contact Number
            self.driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i6 i9']").send_keys(form_data['contact'])
            
            # Fill Email ID and verify
            email_field = self.driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i11 i14']")
            email_field.send_keys(form_data['email'])
            self.verify_email(form_data['email'])
            
            # Fill Full Address
            self.driver.find_element(By.CSS_SELECTOR, "textarea[aria-labelledby='i16 i19']").send_keys(form_data['address'])
            
            # Fill Pin Code
            self.driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i21 i24']").send_keys(form_data['pin_code'])
            
            # Fill Date of Birth
            dob_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='date']")
            dob_input.send_keys(form_data['dob'])
            
            # Fill Gender
            self.driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i32 i35']").send_keys(form_data['gender'])
            
            # Fill Verification Code
            self.driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby='i37 i40']").send_keys("GNFPYC")
            
            # Final email verification before submission
            self.verify_email(form_data['email'])
            
            # Take screenshot before submission
            self.driver.save_screenshot(f"form_filled_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
            
            # Submit the form
            submit_button = self.driver.find_element(By.CSS_SELECTOR, "div[role='button'][jsname='M2UYVd']")
            submit_button.click()
            
            # Wait for submission confirmation and take screenshot
            time.sleep(2)
            self.driver.save_screenshot(f"form_submitted_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            self.driver.save_screenshot(f"error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        
        finally:
            self.driver.quit()

if __name__ == "__main__":
    form_data = {
        'full_name': 'SIMTAYA Dissima Dilaba Martin',
        'contact': '0090507983',
        'email': 'martinsimtaya@gmail.com',
        'address': 'Sanguera, Lome-Togo',
        'pin_code': '1502 Lomé 1',
        'dob': '11/11/2004',
        'gender': 'Male'
    }
    
    bot = FormAutomation()
    bot.fill_form(form_data)