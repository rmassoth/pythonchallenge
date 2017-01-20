from PIL import Image

wire = Image.open("wire.png")
new_image = Image.new(mode=wire.mode, size=(100, 100))
wire_px = wire.load()
new_px = new_image.load()
i = 0
pixel_length = 100
currentx = 0
currenty = 0

while i < 10000:
    for x in range(currentx, currentx + pixel_length):
        new_px[x, currenty] = wire_px[i,0]
        i += 1
    currentx = x
    currenty += 1
    pixel_length -= 1

    for y in range(currenty, currenty + pixel_length):
        new_px[currentx, y] = wire_px[i,0]
        i += 1
    currenty = y
    currentx -= 1
    print(currentx, pixel_length)
    for x in range(currentx, currentx - pixel_length, -1):
        new_px[x, currenty] = wire_px[i,0]
        i += 1
    currentx = x
    currenty -= 1
    pixel_length -= 1
    
    for y in range(currenty, currenty - pixel_length, -1):
        new_px[currentx, y] = wire_px[i,0]
        i += 1
    currenty = y
    currentx +=1

new_image.show()