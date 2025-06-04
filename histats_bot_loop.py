from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Daftar User-Agent realistis
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi Note 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1"
]

TARGET_URL = "https://c4up.me"  # Ganti dengan URL milikmu
TOTAL_VISITORS = 10             # Ganti sesuai jumlah yang diinginkan

def run_bot(visitor_id):
    user_agent = random.choice(user_agents)

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument(f"user-agent={user_agent}")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        print(f"[{visitor_id}] Membuka: {TARGET_URL} dengan UA: {user_agent}")
        driver.get(TARGET_URL)

        # Tunggu supaya Histats jalan dengan JS
        time.sleep(random.randint(6, 12))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.randint(2, 5))

        print(f"[{visitor_id}] ✓ Kunjungan selesai.\n")

    except Exception as e:
        print(f"[{visitor_id}] ✗ Error: {e}")

    finally:
        driver.quit()

for i in range(1, TOTAL_VISITORS + 1):
    run_bot(i)
    wait = random.randint(5, 15)
    print(f"Menunggu {wait} detik sebelum pengunjung berikutnya...\n")
    time.sleep(wait)
