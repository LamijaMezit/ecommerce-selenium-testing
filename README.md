 # E-commerce Website Test Script
 This repository contains a Python script for testing an e-commerce website using Selenium WebDriver.

 # Test Description
 The test script navigates through an e-commerce website, performs various actions such as clicking on links, adding items to the cart, and interacting with form elements. It validates that certain elements are present and performs actions based on specific conditions.

 # Test cases covered
 - Open the web page "https://tutorialsninja.com/demo/" and maximize the window.

 - Verify the page title. It should be "Your Store".

 - Click on the "Cameras" link on the page.

 - Click on the link for "Nikon D300" camera.

- Click on the first product image.

 - Click on the next picture button five times.

 - Close the image by clicking on the "Close" button.

- Click on the quantity input field.

 - Clear the quantity input field.

 - Enter the quantity "3" in the input field.

 - Click on the "Add to Cart" button to add the product to the cart.

 - Click on the "Desktops" link on the page.

 - Hover over "Desktops" to display the submenu.

 - Click on the "Show All Desktops" link.

 - Click on the link for "Apple Cinema 30" monitor.

- Scroll to the "Add to Cart" button.

- Click on the calendar icon.

 - Scroll to the next month until December 2022 is displayed.

 - Click on the day "31" on the calendar.

 - Click on the "Add to Cart" button to add the product to the cart.

 - Close the browser.

 # Setup
  1. Python Installation: Make sure you have Python installed on your system. You can download it from python.org.

 2. Install Dependencies: Install the required Python dependencies using pip:
```bash
 pip install selenium webdriver-manager
```


3. WebDriver Setup: This script uses Chrome WebDriver. WebDriver Manager will automatically download the appropriate ChromeDriver for your system. You can also manually download ChromeDriver and specify its path in the script if needed.

# Running the Test

Clone the project:

```bash
  git clone https://github.com/LamijaMezit/ecommerce-selenium-testing.git
```

Run the Test Script: Execute the test script using Python:

```bash
  python test_ecommerce.py
```
