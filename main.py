import time

from dotenv import load_dotenv
from DrissionPage import ChromiumPage, ChromiumOptions
import os
import git

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

        time.sleep(5)

        commit_file()
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

            commit_file()


def commit_file():
    os.replace(r'C:\Users\aayus\Downloads\UW_Resume___v1_0.pdf', r'C:\Users\aayus\Development\aayushsood-v2\public\assets\resume\resume.pdf')

    time.sleep(2)

    repo = git.Repo(r'C:\Users\aayus\Development\aayushsood-v2')

    repo.git.add(A=True)

    repo.index.commit("Updated resume")

    origin = repo.remote(name="origin")
    origin.push()


if __name__ == "__main__":
    main()
