import requests
from PIL import Image
from io import BytesIO

def fetch_and_show_image(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/128.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img.show()  # Opens in default image viewer
            print("✅ Image fetched and displayed successfully.")
        else:
            print(f"❌ HTTP Error: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Request failed: {e}")

if __name__ == "__main__":
    url = input("🔗 Please enter the image URL: ").strip()
    fetch_and_show_image(url)
