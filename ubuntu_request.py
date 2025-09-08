import requests
import os
from urllib.parse import urlparse
import hashlib

def generate_filename(url):
    """
    Extract the filename from URL or generate a unique one using hash
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename or '.' not in filename:  # if no proper filename or extension
        filename = f"image_{abs(hash(url))}.jpg"
    return filename

def save_image(url, directory="Fetched_Images"):
    """
    Download and save an image from a given URL to the specified directory
    """
    # Create directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    try:
        # Fetch the image with requests
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors

        # Generate or extract filename
        filename = generate_filename(url)
        filepath = os.path.join(directory, filename)

        # Prevent duplicates: check if file already exists
        if os.path.exists(filepath):
            print(f"⚠️ Image already exists: {filename}. Skipping download.")
            return

        # Save the image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("🌍 Connection strengthened. Community enriched.\n")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error while fetching {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Prompt user for multiple URLs separated by commas
    urls_input = input("Please enter image URLs (separate multiple URLs with commas): ")
    urls = [url.strip() for url in urls_input.split(',') if url.strip()]

    if not urls:
        print("No URLs provided. Exiting.")
        return

    for url in urls:
        save_image(url)

if __name__ == "__main__":
    main()
