import requests
import os
from urllib.parse import urlparse

def main():
    print("🌍 Welcome to the Ubuntu Image Fetcher")
    print("✨ 'I am because we are' – Collecting shared beauty from the web ✨\n")
    
    # Ask the user for the image URL
    url = input("🔗 Please enter the image URL: ").strip()
    
    try:
        # Ensure Fetched_Images directory exists
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # Fetch image with requests
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Handle bad HTTP codes

        # Parse filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If filename is missing, create one
        if not filename:
            filename = "ubuntu_image.jpg"
        
        # Build file path
        filepath = os.path.join("Fetched_Images", filename)
        
        # Save in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        # Success messages
        print(f"✅ Success: {filename} fetched from the community")
        print(f"📂 Saved mindfully at: {filepath}")
        print("\n🤝 Connection made. Community enriched. - HexSentiel")
    
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e.response.status_code} - Respectfully handled.")
    except requests.exceptions.Timeout:
        print("⏳ Connection timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Connection issue: {e}")
    except Exception as e:
        print(f"🚨 Unexpected error: {e}")

if __name__ == "__main__":
    main()
