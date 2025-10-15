import requests
import json
from datetime import datetime

# === Cấu hình URL API (xoso.me) ===
API_URL = "https://api.xoso.me/app/kqxsmn"  # Miền Nam (mẫu)
API_URL_MT = "https://api.xoso.me/app/kqxsmt"  # Miền Trung
API_URL_MB = "https://api.xoso.me/app/kqxsmn?mien=mb"  # Miền Bắc

# === Lấy dữ liệu từ API ===
def get_data(url):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.json()
        else:
            return None
    except Exception as e:
        print("Lỗi khi lấy dữ liệu:", e)
        return None

# === Hàm chính ===
def main():
    today = datetime.now().strftime("%Y-%m-%d")

    data = {
        "XSMB": {"date": today, "result": "Không có dữ liệu"},
        "XSMT": {"date": today, "result": "Không có dữ liệu"},
        "XSMN": {"date": today, "result": "Không có dữ liệu"},
    }

    # Lấy từng miền
    mn = get_data(API_URL)
    mt = get_data(API_URL_MT)
    mb = get_data(API_URL_MB)

    if mn: data["XSMN"]["result"] = mn.get("data", "Không có")
    if mt: data["XSMT"]["result"] = mt.get("data", "Không có")
    if mb: data["XSMB"]["result"] = mb.get("data", "Không có")

    # Lưu file JSON
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("✅ Đã cập nhật dữ liệu:", today)

if __name__ == "__main__":
    main()
