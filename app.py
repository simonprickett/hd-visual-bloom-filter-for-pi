import unicornhathd

unicornhathd.rotation(90)
unicornhathd.brightness(0.6)
u_width, u_height = unicornhathd.get_shape()

try:
    #for y in range(u_height):
    #    for x in range(u_width):
    #        unicornhathd.set_pixel(x, y, 255, 0, 0)

    unicornhathd.set_pixel(0, 0, 255, 0, 0)
    unicornhathd.set_pixel(15, 15, 0, 0, 255)
    unicornhathd.show()

    while True:
        continue

except KeyboardInterrupt:
    unicornhathd.off()
