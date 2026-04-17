from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

YOUR_NAME = "@T Kamanzi Herve"

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

driver.get("https://web.whatsapp.com")

print("Waiting for login...")

time.sleep(40)

def send_self_alert(group_name, message_text):

    try:

        search = driver.find_element(
            By.XPATH,
            "//div[@contenteditable='true']"
        )

        search.click()

        search.send_keys("You")

        time.sleep(2)

        chat = driver.find_element(
            By.XPATH,
            "//span[@title='You']"
        )

        chat.click()

        time.sleep(2)

        message_box = driver.find_element(
            By.XPATH,
            "//div[@contenteditable='true']"
        )

        alert_message = (
            "You were personally mentioned.\n\n"
            f"Group: {group_name}\n"
            f"Message: {message_text}"
        )

        message_box.send_keys(alert_message)
        message_box.send_keys("\n")

    except:

        pass

def check_mentions():

    messages = driver.find_elements(
        By.CSS_SELECTOR,
        "span.selectable-text"
    )

    for msg in messages:

        text = msg.text

        if "@" in text:

            if "@all" in text.lower():

                continue

            if YOUR_NAME in text:

                group = driver.find_element(
                    By.CSS_SELECTOR,
                    "header span"
                ).text

                send_self_alert(group, text)

while True:

    check_mentions()

    time.sleep(10)