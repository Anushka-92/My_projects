# 🎯 YouTube Close Project
## 🚀 Introduction
I was feeling a bit distracted 😵‍💫, so I channeled that energy into creating this fun project! 🎉<br>
The idea is simple: stop wasting time on YouTube and focus on what really matters 💪.<br>
Initially i wrote script just by using this logic of blocking domian name in (C:\Windows\System32\drivers\etc) host file , using python1.py [ file present above] where i have listed down different shortest approaches to sort out this issue.<br>
But the script nneeds to be run manually every time [ that is something which we definetly don't encourage ] So i came up with approach of exploring task scedular similar to concept of cron jobs in linux/unix based systems. <br>
This project is a small but meaningful step towards better productivity and time management. ⏳✨<br>
## ✨ Features<br>
🚫 Blocks Access to YouTube — Say goodbye to endless scrolling!<br>
🛠️ Automated Tasks — Helps you manage distractions seamlessly.<br>
📚 Learning by Doing — Explores Git, GitHub, and task scheduling.<br>
🛤️ Journey So Far.<br>
Here’s what we’ve done to bring this idea to life:<br>

1. Project Setup 🗂️<br>
Created a main folder called fun_project.<br>
Inside it, created a subfolder named scripts.<br>
Decided to manage the entire process from VS Code. ✍️<br>

2. Writing the Python Library 🐍<br>
Wrote a Python script to block YouTube by editing the system’s hosts file:<br>
Added an entry like this:
```bash
127.0.0.1 youtube.com
```
* This redirects YouTube requests to the local machine, effectively blocking the site.<br>
* Packaged the script into a reusable Python library.<br>
* Added proper error handling and configuration options for customization.<br>
* Tested the library to ensure it blocks and unblocks YouTube seamlessly. ✅<br>


3. Task Scheduling with Python 📆<br>
Integrated task scheduling into the library using the schedule module:<br>
Installed the library:<br>
```
pip install schedule
```
* Created a Python script to block and unblock YouTube at specific times:
```
import schedule
import time
from youtube_close import block_youtube, unblock_youtube

def block_task():
    block_youtube()
    print("YouTube is now blocked. 🚫")

def unblock_task():
    unblock_youtube()
    print("YouTube is now unblocked. ✅")

# Schedule the blocking and unblocking
schedule.every().day.at("09:00").do(block_task)  # Block at 9:00 AM
schedule.every().day.at("17:00").do(unblock_task)  # Unblock at 5:00 PM

while True:
    schedule.run_pending()
    time.sleep(1)
```
* Tested the scheduler to ensure tasks run at the correct times. 🕒

4. Version Control with Git 🐙<br>
Initialized the repository and tracked changes using Git:<br>
```
git init
git add .
git commit -m "Initial commit for YouTube blocking library"
```
Created a remote repository on GitHub and pushed the project:<br>
```
git remote add origin <repository-url>
git push -u origin main
```

5. Enhanced the README 📝<br>
Documented the process step-by-step to help others understand and replicate the solution. 🎨<br>

## 📜 Usage Instructions<br>
* Install the Library: (if published, otherwise link to your repository)<br>
* Set Up the Scheduler: Create a script using the example provided above to automate the blocking<br>


🌟 Thank You for Checking Out This Fun Productivity Project!
🎉 Let’s stay focused and try new things together. 🚀

