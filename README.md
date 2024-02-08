# tiktok-like-experiment
CS315 project testing how likes affect a user's recommendation algorithm using Selenium.

By: Miles Mezaki, Sandy Liu, Sarah Goldman, Caroline Jung, Johanna Lee, Audrey Liang

##### The TikTok audit code is in the PageTiktok.py file in the page_objects folder. chrome_audit has not been updated.

git clone this repository on your device.

## how to run test:
1. open vscode
2. set python interpreter as venv (virtual environment, [directions to install](https://techinscribed.com/python-virtual-environment-in-vscode/) <br>
    a. open computer terminal and do the following, one line at a time  <br>
           pip install virtualenv  <br>
           virtualenv --version  <br>
           cd ~  <br>
           mkdir .virtualenvs  <br>
           cd .virtualenvs  <br>
           virtualenv venv  <br>
           source venv/bin/activate  <br>
    b. open vscode, go to view > command palette, type Python: Select Interpreter, click venv  <br>
    <img width="711" alt="Screenshot 2024-02-08 at 12 47 43 PM" src="https://github.com/mlsmzk/tiktok-like-experiment/assets/114271268/1c0da498-62be-4304-b7b7-1ccd92945f28">  <br>
    c. on vscode, go to terminal > New Terminal. You should see (venv) <img width="403" alt="Screenshot 2024-02-08 at 12 49 18 PM" src="https://github.com/mlsmzk/tiktok-like-experiment/assets/114271268/3f44556d-f415-4cf6-a711-a90d1a558618">  <br>
3. navigate to the tiktok-like-experiement folder on the vscode terminal (so where you cloned this repository into)
4. run: pip install -r requirements.txt to get all the packages
   a. if this doesn't work, move on to number 5.
5. run the python file PageTikTok.py by copying this to the terminal: python -m pytest . --html=report.html  <be>
    a. if this does not work ex) no module "module name", run: pip install "moudule name"
    b. repeat a until no more errors
    c. if you see the error "_main-py: error: unrecognized arguments: --html=report.html", run: "pip install pytest-html"
6. manually log in, ***remove two popups on bottom right after log in***  <br>
7. when "test passed" appears on the terminal, look inside folder and there should be a report.html with details  <br>




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
- csv header (completed)
- what information to store from html page 
    - currently saving batch, index, video, tags, author, number of likes, ***comments, saves, shares*** (2/8 new!)
    - might consider using pyktok later if need more specific information
