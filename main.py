import os
import shutil

from banner import banner
from crawler import Crawler
from messages import full_success, primary, success, warning
from scanner import QRCodeScanner
from utils import is_valid

generic_count = 0
sensitive_count = 0

print(banner)
query_choice = False

while not query_choice:
    query = input("Expression to search? : ")
    if is_valid(query, "str"):
        primary(f"search query: {query}")
        query_choice = True
    else:
        warning("Wrong format for search, please try again")

start_year_choice = False
while not start_year_choice:
    start_year = input("Start year? : ")
    if is_valid(start_year, "int"):
        start_year_choice = True
    else:
        warning("Wrong start year format, please try again")

start_month_choice = False
while not start_month_choice:
    start_month = input("Start month? : ")
    if is_valid(start_month, "int"):
        start_month_choice = True
    else:
        warning("Wrong start month format, please try again")

start_day_choice = False
while not start_day_choice:
    start_day = input("Start day? : ")
    if is_valid(start_day, "int"):
        start_day_choice = True
    else:
        warning("Wrong start day format, please try again")

primary(f"start date {(start_year, start_month, start_day)}")

end_year_choice = False
while not end_year_choice:
    end_year = input("end year? : ")
    if is_valid(end_year, "int"):
        end_year_choice = True
    else:
        warning("Wrong end year format, please try again")

end_month_choice = False
while not end_month_choice:
    end_month = input("end month? : ")
    if is_valid(end_month, "int"):
        end_month_choice = True
    else:
        warning("Wrong end month format, please try again")

end_day_choice = False
while not end_day_choice:
    end_day = input("end day? : ")
    if is_valid(end_day, "int"):
        end_day_choice = True
    else:
        warning("Wrong end day format, please try again")

primary(f"end date {(end_year, end_month, end_day)}")

total_result = input("Total result wanted (1/100) - (default 50) ? :") or None

primary(f"total result expected {total_result}\n")

print("-" * 15)
print("Settings resume:")
success(f"Search: {query}")
success(f"Start date: {(start_year, start_month, start_day)}")
success(f"End date: {(end_year, end_month, end_day)}")
success(f"Total expected: {total_result}")
print("-" * 15)

warning("Start qrawler-decode ? Y/n\n")
choice = input("> ")

if choice.lower() == "n":
    primary("Exiting ..\n")
    exit(0)

print("\n*************\n")
full_success("Images collected")
primary("Starting scan....\n")

if choice.lower() == "y":
    primary("Starting collect...")
    crawler = Crawler(
        start=(int(start_year), int(start_month), int(start_day)),
        end=(int(end_year), int(end_month), int(end_day)),
        query=query,
        limit=int(total_result) or None,
    )
    crawler.get_images_google_images()
    # crawler.get_bing_images()

    primary("Collected done!")

    img = "./images"

    for files in os.scandir(img):
        if files.path.endswith("jpg"):
            scanner = QRCodeScanner(img=files.path)
            scanner.get_generic_qrcode_info()
            generic_count += 1
            try:
                if scanner.get_pass_info():
                    sensitive_count += 1

            except Exception as e:
                print(e)

    print("*" * 15)
    success("Operation done!")
    success(f"Total random data identified: {generic_count}")
    success(f"Sensitive data found: {sensitive_count}")
    full_success("Found datas are available in the /results directory.")

    clean = input("Remove images? Y/n ")
    if clean.lower() == "y":
        primary("Cleaning...")
        shutil.rmtree("./images")
        success("Clean done")
    else:
        primary("Exiting")
        exit(0)
