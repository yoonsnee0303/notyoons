import schedule
import time
import subprocess



file_paths = [
    r"C:\Users\Data2\OneDrive\바탕 화면\네이버판매순\test.py", # 네이버판매순
    r"C:\Users\Data2\OneDrive\바탕 화면\0000\api_test_simple.py", # 고도몰
    r"C:\Users\Data2\OneDrive\바탕 화면\동서브랜드일일취합\test.py", # 동서브랜드
]

def run_script(file_path):
    process = subprocess.Popen(["python", file_path])
    process.communicate()  # Wait for the process to finish
    if process.returncode != 0:
        print(f"실행 실패: {file_path}")

def run_file1_and_file2():
    print('run_file1_and_file2')
    for file_path in file_paths[:len(file_paths)-1]:
        print(f'{file_path} ::: start')
        run_script(file_path)
    print('run_file1_and_file2 done done done')

def run_file3():
    print('run_file3')
    run_script(file_paths[len(file_paths)-1])
    print('run_file3 done')

# Schedule file1.py and file2.py to run every 24 hours at 8:00 AM
schedule.every().day.at("08:00").do(run_file1_and_file2)

# Schedule file3.py to run every hour
schedule.every().hour.do(run_file3)

# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)
