import time
from pathlib import Path
import glob
from dotenv import load_dotenv
from DrissionPage import ChromiumPage
import os
import git

load_dotenv()

page = ChromiumPage()

LOGIN_URL = "https://overleaf.com/login"
BASE_PATH = Path.home()
REPO_PATH = BASE_PATH / "Development" / "aayushsood-v2"
DESTINATION_PATH = REPO_PATH / "public" / "assets" / "resume" / "resume.pdf"
RESUME_LINK_TEXT = "UW Resume"


def log_in():
    email_input = page.ele('css:input[name="email"]')

    email_input.input(os.getenv("EMAIL"))

    pass_input = page.ele('css:input[name="password"]')

    pass_input.input(os.getenv("PASSWORD"))

    submit_btn = page.ele('css:button[type="submit"]')
    submit_btn.click()

    page.wait(5)

def find_resume():
    pdf_btn = page.ele(f"tag:a@text():{RESUME_LINK_TEXT}")
    pdf_btn.click()

    page.wait(5)

    pdf_link = page.ele("tag:a@class:pdf-toolbar-btn")
    pdf_link.click()

    time.sleep(5)

def commit_file():
    repo = git.Repo(REPO_PATH)

    repo.git.add(A=True)

    repo.index.commit("Updated resume")

    origin = repo.remote(name="origin")
    origin.push()

def move_file():
    list_of_files = glob.glob(str(BASE_PATH / "Downloads" / "*.pdf"))
    latest_file = max(list_of_files, key=os.path.getctime)

    source_path = latest_file

    os.replace(source_path, DESTINATION_PATH)

    time.sleep(2)

def main():
    try:
        page.get(LOGIN_URL)

        if "project" in page.url:
            find_resume()
        else:
            log_in()
            find_resume()

        move_file()
        commit_file()
    except Exception as e:
        print(f"Automation failed: {e}")
    finally:
        page.quit()


if __name__ == "__main__":
    main()
