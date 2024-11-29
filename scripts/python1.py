###Initially i was trying to make changes inside host file soo
sites_to_block = ["www.youtube.com"]
hosts_path = r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
def block():

    #if datetime.now() < end_time:

    #print("block sites")

    with open(hosts_path , 'r') as hostsfile:

        hosts_content = hostsfile.read()
        for site in sites_to_block:
            if site not in hosts_content:
                hostsfile.write(redirect + " " + site + "\n")

if __name__ == "__main__":
    block()

##### Using different python libraries to create warning box and kill the process
import os 
os.popen('tasklist').readlines()
import os
os.system('taskkill /im youtube.com')
import ctypes
ctypes.windll.user32.MessageBoxW(0, 'Get back to work!', 'Alert!', 0)

####using kill 9 for ending process to terminate process .
def close_youtube():
    browser_names = ['chrome','edge']  # Add your browser's executable name
    youtube_urls = ['youtube.com', 'www.youtube.com']
    
    for process in psutil.process_iter(['pid', 'name']):
        if any(browser in process.info['name'].lower() for browser in browser_names):
            try:
                # Get command-line arguments (process.cmdline() may require admin permissions)
                cmd = ' '.join(process.cmdline())
                if any(url in cmd for url in youtube_urls):
                    os.kill(process.info['pid'], 9)  # Forcefully terminate the browser process
                    print(f"{process.info['name']} (YouTube tab) has been closed.")
                    return
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                pass
    print("No YouTube tab found.")

while True:         # Run continuously
    close_youtube()
    time.sleep(5)  # Check every 5 seconds




