# tiktok-like-experiment
CS315 project testing how likes affect a user's recommendation algorithm using Selenium.

By: Miles Mezaki, Sandy Liu, Sarah Goldman, Caroline Jung, Johanna Lee, Audrey Liang

##### The TikTok audit code is in the PageTiktok.py file in the page_objects folder. chrome_audit has not been updated.

## how to run test:
1. open vscode
2. set python interpreter as venv (virtual environment, [directions to install](https://techinscribed.com/python-virtual-environment-in-vscode/)
3. run the python file PageTikTok.py
4. vscode terminal: python -m pytest . --html=report.html
5. manually log in, remove two popups on bottom right after log in
6. when "test passed" appears on the terminal, look inside folder and there should be a report.html with details

## things to notice:
1. You can commment/uncomment the output csv code two iterate_through functions.
2. If the requirements does not work, pip install packages mentioned in the import
3. pytest contains both tendency liking/random liking test codes
4. You will have to **manually input** your account. Afterwards you can hold on to it and wait until the page start moving. If the terminal shows that it is still running, do not touch your tiktok webpage until your pytest pass/fail(feel free to look at other stuff while waiting)
5. report.html has to be opened in the browser to see the cleaned version

Currently, the code successfully identifies posts with **predefined hashtags** (scenario 1), and scrolls to the next batch if it's done with the current batch. **random liking** has been working as well.


## Have to work on:
- ElementClickInterception for some posts that are supposed to be liked (fixed)
- randomly like posts (scenario 2)  (completed)
- like posts with specific creator/sound (scenario 3) (Miles)
- what information to store from html page 
    - currently saving batch, index, video, tags, author, likes
    - might consider using pyktok later if need more specific information
