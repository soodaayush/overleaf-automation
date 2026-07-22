from dotenv import load_dotenv
from DrissionPage import ChromiumPage, ChromiumOptions
import os

load_dotenv()

def main():
    co = ChromiumOptions()
    co.set_browser_path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    page = ChromiumPage(co)

    page.get("https://overleaf.com/login")

    if "project" in page.url:
        pdf_btn = page.ele("tag:a@text():UW Resume")
        pdf_btn.click()

        page.wait(5)

        pdf_link = page.ele("tag:a@class:pdf-toolbar-btn")
        pdf_link.click()
    else:
        if page.ele('@name=email') and page.url == "https://overleaf.com/login":
            email_input = page.ele('css:input[name="email"]')

            email_input.input(os.getenv("EMAIL"))

            pass_input = page.ele('css:input[name="password"]')

            pass_input.input(os.getenv("PASSWORD"))

            submit_btn = page.ele('css:button[type="submit"]')
            submit_btn.click()

            page.wait(5)

            pdf_btn = page.ele("tag:a@text():UW Resume")
            pdf_btn.click()

            page.wait(5)

            pdf_link = page.ele("tag:a@class:pdf-toolbar-btn")
            pdf_link.click()


if __name__ == "__main__":
    main()
