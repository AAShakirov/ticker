import os, glob
from PIL import Image, ImageDraw, ImageFont
from video import make_video

def clear_folder():
    files = glob.glob('/home/arthur/Documents/code/it-solution/images')
    for file in files:
        os.remove(file)

def get_text():
    text = input()
    return text

def make_empty():
    img = Image.new('RGB', (100, 100), (147, 112, 219))
    img.save('empty.png')

def get_length_text(text):
    length_text = text.__len__() * 5
    return length_text

def make_images(text, length_text):
    font = ImageFont.load_default()
    length_text *= 2
    for i in range(100 + length_text):
        img = Image.open('empty.png')
        idraw = ImageDraw.Draw(img)
        idraw.text((i - length_text, 50), text, (0, 255, 255), font=font)
        img.save(f'images/image_{i}.png')

def delete_match_image(length_text):
    filenames = [int(path.split('_')[1].split('.')[0]) for path in 
                 os.listdir(r'/home/arthur/Documents/code/it-solution/images')]
    filenames.sort()
    images = {}
    image_empty = Image.open('images/image_0.png')
    for i in range(1, length_text):
        try:
            images[i] = Image.open(f'images/image_{filenames[i]}.png')
        except FileNotFoundError:
            continue
        if image_empty == images[i]:
            file = f'image_{(filenames[i])}.png'
            location = r'/home/arthur/Documents/code/it-solution/images'
            path = os.path.join(location, file)  
            os.remove(path)

def main():
    clear_folder()
    text = get_text()
    length_text = get_length_text(text)
    make_empty()
    make_images(text, length_text)
    delete_match_image(length_text)
    make_video()

if __name__ == '__main__':
    main()
