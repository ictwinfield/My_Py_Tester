from PIL import Image

def new_image(fn):
    old_im = Image.open(fn)
    old_size = old_im.size
    # new_size = (old_size[0] + 40, old_size[1] + 40)
    new_size = (400, 200)

    new_im = Image.new("RGB", new_size, '#ffffff')
    new_im.paste(old_im, (int((new_size[0]-old_size[0])/2), int((new_size[1]-old_size[1])/2)))

    new_im.save(fn)
