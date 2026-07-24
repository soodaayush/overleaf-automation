# Overleaf Automation

A Python script that keeps the resume on my personal website in sync with Overleaf. Instead of manually downloading a new PDF and committing it to my site repo every time I edit my resume, one command handles the whole pipeline: log in to Overleaf, download the compiled PDF, move it into place, and push the change to GitHub.

## How it works

1. Opens Overleaf in a Chromium browser via [DrissionPage](https://drissionpage.cn/), reusing the existing browser session where possible so login (and reCAPTCHA) can often be skipped entirely
2. Logs in with credentials from a `.env` file if no active session exists
3. Opens the resume project and clicks the PDF download button in the editor toolbar
4. Moves the freshly downloaded PDF from `~/Downloads` into the website repo at `public/assets/resume/resume.pdf`
5. Commits and pushes the change with GitPython

## Why DrissionPage

Overleaf's login flow sits behind reCAPTCHA, which is hostile to standard automation tools. DrissionPage drives a real Chromium instance rather than a webdriver, which produces a less detectable browser fingerprint and allows session reuse across runs, so the CAPTCHA rarely triggers at all.

## Setup

1. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root:

   ```
   EMAIL=your_overleaf_email
   PASSWORD=your_overleaf_password
   ```
5. Adjust the constants at the top of `main.py` for your own setup:
   - `REPO_PATH` - path to the local git repo the PDF should land in
   - `DESTINATION_PATH` - where the PDF lives inside that repo
   - `RESUME_LINK_TEXT` - the name of your resume project on the Overleaf dashboard

## Usage

```
python main.py
```

The script detects whether you're already logged in (by checking for a redirect to the project dashboard) and skips the login step if so.

## Requirements

- Python 3
- Chromium or Chrome installed locally
- Push access to the target git repo

## Notes

- Credentials never leave the `.env` file, which is gitignored
- The script grabs the most recently created PDF in `~/Downloads`, so avoid downloading other PDFs while it runs
