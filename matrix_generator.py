from PIL import Image
import sys
from font_bitmap import character_bitmap


def rgb_int(r, g, b):
    return r + (2**8 * g) + (2**16 * b)

# a: 0 - 24
# b: 0 - 3

def set_slot(a, b, val, char, matrix):
    x = a * 8
    y = b * 5
    for horizontal in range(x, x+5):
        for vertical in range(y, y+8):
            print("Horizontal: {}".format(horizontal))
            print("vertical: {}".format(vertical))
            print("char: {}".format(char))
            matrix.putpixel((horizontal, vertical), val * character_bitmap[char][a][b])

def generate_matrix(argv):
    width = 128
    height = 32
    rows = 4

    display_string = "12: 05 mins & 29 mins\n28: 08 mins & 16 mins\n39: 32 mins & 64 mins".split('\n')
    display_string = "ABC\nABC\nABC".split('\n')

    display_matrix = Image.new("RGB", (width, height), color=0)
    for b, row in enumerate(display_string):
        for a, char in enumerate(row):
            set_slot(a, b, rgb_int(255, 127, 0), char, display_matrix)

    display_matrix.save("./LED_display_matrix.png")

if __name__ == "__main__":
    generate_matrix(sys.argv[1:])