import os

captions_path = r'E:\Project\AI & ML\Python practice\Img Captioning\Flickr8k_text\Flickr8k.token.txt'

try:
    if not os.path.exists(captions_path):
        raise FileNotFoundError(f"File not found at: {captions_path}")
    with open(captions_path, 'r', encoding='utf-8') as f:
        captions = f.readlines()

    print("✅ Captions file loaded successfully.")
    print(f"Total captions: {len(captions)}\n")
    print("📄 First 5 captions:")
    for line in captions[:5]:
        print(line.strip())

except FileNotFoundError as e:
    print("❌ Error:", e)
    print("Please ensure the Flickr8k dataset is in 'E:\\Project\\AI & ML\\Python practice\\Img Captioning\\Flickr8k_text\\'")
    directory = os.path.dirname(captions_path)
    if os.path.exists(directory):
        print(f"Contents of {directory}:", os.listdir(directory))
    else:
        print(f"Directory does not exist: {directory}")
except Exception as e:
    print("❌ Error reading captions file:", e)
    