import board
import neopixel
pixels = neopixel.NeoPixel(board.D12, 16)

while True:
    pixels.fill((0,200,0))
    pixels.show()
