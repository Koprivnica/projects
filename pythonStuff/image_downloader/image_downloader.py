import os
import requests

def get_extension(image_url: str) -> str or None:
    extensions: list[str] = [".png", ".jpeg", ".jpg", ".gif", ".svg"]
    for ext in extensions:
        if ext in image_url:
            return ext

def download_image(image_url: str, name: str, folder: str=None):
    if ext := get_extension(image_url):
        if folder:
            image_name: str = f"{folder}/{name}{ext}"
        else:
            image_name: str = f"{name}{ext}"
    else:
        raise Exception("Image extension could not be located...")
    
    if os.path.isfile(image_name):
        raise Exception("File name already exists...")
    
    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, "wb") as handler:
            handler.write(image_content)
            print(f"Downloaded: {image_name} successfully!")
    except Exception as e:
        print("Error: {e}")

if __name__ == "__main__":
    input_url: str = input("Enter a URL: ")
    input_name: str = input("What would you like to name the image? ")
    
    print("Downloading...")
    download_image(input_url, name=input_name, folder="images")