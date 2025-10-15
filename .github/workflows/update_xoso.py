import requests
import json
from datetime import datetime

# === Cấu hình URL API (miễn phí từ xoso.me) ===
API_MN = "https://api.xoso.me/app/kqxsmn"   # Miền Nam
API_MT = "https://api.xoso.me/app/kqxsmt"   # Miền Trung
API_MB = "https://api.xoso.me/app/kqxsmn?mien=mb"  # Miền Bắc

def lay_ket_qua(url):
    """Hàm lấy dữ liệu JSON từ API."""
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.json()
        else:
            print("Lỗi mã trạng thái:", r.status_code)
    except Exception as e:
        print("Lỗi khi lấy dữ liệu:", e)
    return None

def main():
    today = datetime.now().strftime("%Y-%m-%d")

    data = {
        "ngay_cap_nhat": today,
        "XSMN": {"mien": "Miền Nam", "ket_qua": "Đang cập nhật..."},
        "XSMT": {"mien": "Miền Trung", "ket_qua": "Đang cập nhật..."},
        "XSMB": {"mien": "Miền Bắc", "ket_qua": "Đang cập nhật..."}
    }

    mn = lay_ket_qua(API_MN)
    mt = lay_ket_qua(API_MT)
    mb = lay_ket_qua(API_MB)

    if mn: data["XSMN"]["ket_qua"] = mn
    if mt: data["XSMT"]["ket_qua"] = mt
    if mb: data["XSMB"]["ket_qua"] = mb

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("✅ Đã cập nhật dữ liệu ngày:", today)

if __name__ == "__main__":
    main()
