# tiktok-like-experiment
CS315 project testing how likes affect a user's recommendation algorithm using Selenium.

By: Miles Mezaki, Sandy Liu, Sarah Goldman, Caroline Jung, Johanna Lee, Audrey Liang


## how to run test:
1. open vscode
2. set python interpreter as venv (virtual environment, [directions to install](https://techinscribed.com/python-virtual-environment-in-vscode/)
3. vscode terminal: python -m pytest . --html=report.html
4. manually log in, remove two popups on bottom right after log in
5. when "test passed" appears on the terminal, look inside folder and there should be a report.html with details

Currently, the code successfully identifies posts with **predefined hashtags** (scenario 1), and scrolls to the next batch if it's done with the current batch. 

## Have to work on:
- ElementClickInterception for some posts that are supposed to be liked
- randomly like posts (scenario 2)
- like posts with specific creator/sound (scenario 3)
- what information to store from html page
