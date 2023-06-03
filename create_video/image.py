from PIL import Image, ImageDraw, ImageFont

def make_empty():
    img = Image.new('RGB', (100, 100), 'white')
    img.save('empty.png')
    return img

def make_images(img):
    font = ImageFont.load_default()
    for i in range(100):
        img = Image.open('empty.png')
        idraw = ImageDraw.Draw(img)
        idraw.text((i, 50), 'TEST', (0, 0, 0), font=font)
        img.save(f'images/image_{i}.png')

def main():
    img = make_empty()
    make_images(img)

if __name__ == '__main__':
    main()

