import os
from playwright.sync_api import sync_playwright
from playwright_recaptcha import recaptchav2
from dotenv import load_dotenv

load_dotenv()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.overleaf.com/login")

    print(f"Page Title: {page.title()}")

    page.locator("input#email").fill(os.getenv("EMAIL"))
    page.locator("input#password").fill(os.getenv("PASSWORD"))

    page.locator("button.btn").first.click()

    with recaptchav2.SyncSolver(page) as solver:
        token = solver.solve_recaptcha(wait=True)

        page.wait_for_load_state("networkidle")

    page.locator("text=UW Resume").click()
    page.wait_for_timeout(2000)

    context.close()
    browser.close()


