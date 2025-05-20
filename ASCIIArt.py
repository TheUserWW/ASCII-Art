from PIL import Image

ASCII_CHARS = "@%#*+=-:. "
WIDTH = 100

def resize_image(image, new_width=WIDTH):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.5)
    return image.resize((new_width, new_height))

def convert_to_ascii_colored(image):
    image = resize_image(image)
    image = image.convert("RGB")
    pixels = list(image.getdata())

    scale = len(ASCII_CHARS)
    ascii_image = ""
    width = image.width

    for i in range(0, len(pixels), width):
        row = ""
        for j in range(width):
            r, g, b = pixels[i + j]
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            char = ASCII_CHARS[gray * (scale - 1) // 255]
            colored_char = f"\033[38;2;{r};{g};{b}m{char}\033[0m"
            row += colored_char
        ascii_image += row + "\n"
    return ascii_image

def convert_image_to_ascii(path):
    try:
        image = Image.open(path)
    except Exception as e:
        print("无法打开图片:", e)
        return
    ascii_img = convert_to_ascii_colored(image)
    print(ascii_img)

convert_image_to_ascii(r"C:\Users\wcx16\Desktop\Allen.png") #修改文件名或目录
