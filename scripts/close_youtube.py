import os
import psutil
import time

def close_youtube_tabs():
    youtube_urls = ['youtube.com', 'www.youtube.com']
    browser_names = ['chrome', 'firefox', 'edge']  

    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
          
            if any(browser in process.info['name'].lower() for browser in browser_names):
              
                cmd = ' '.join(process.info.get('cmdline', []))
        
                if any(url in cmd for url in youtube_urls):
                    print(f"Found YouTube tab in {process.info['name']} (PID: {process.info['pid']}). Closing it.")
                    os.kill(process.info['pid'], 9) 
                    return 
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass

while True:
    close_youtube_tabs()
    time.sleep(3) 
