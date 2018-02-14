def hue_to_rgb(h):
    return hsb_to_rgb(h, 1.0, 1.0)


def hsb_to_rgb(h, s, b):
    if s == 0.0: return b, b, b
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = b * (1.0 - s)
    q = b * (1.0 - s * f)
    t = b * (1.0 - s * (1.0 - f))
    if i % 6 == 0: rgb = b, t, p
    if i == 1: rgb = q, b, p
    if i == 2: rgb = p, b, t
    if i == 3: rgb = p, q, b
    if i == 4: rgb = t, p, b
    if i == 5: rgb = b, p, q
    return [int(val * 255) for val in rgb]

#TODO switch to bytes which can be frozen e.g. red = b'\xFF\x00\x00'
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

yellow = (255, 255, 0)
purple = (255, 0, 255)
teal = (0, 255, 255)

orange = (255, 128, 0)
pink = (255, 64, 64)

white = (255, 255, 255)
black = (0, 0, 0)
