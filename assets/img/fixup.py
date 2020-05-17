from simpleimage import SimpleImage

BORDER_RED = 0
BORDER_GREEN = 51
BORDER_BlUE = 98

def main():
    # image = SimpleImage('images/simba-sq.jpg')
    # image = SimpleImage('../../PersonalProjects/LarynQi.github.io/assets/img/about/eecs.jpg')
    # image = SimpleImage('about/eecs.jpg')
    # image = SimpleImage('about/SEngineering.png')
    # image = SimpleImage('about/vr.png')
    # bordered_img = add_border(image, 20)
    # bordered_img.show()
    ### OG
    # bordered_img.show()

    ### EECS
    # shifted_img = shift(bordered_img, 5)
    # shifted_img.show()

    ### Stanford Engineering
    # trimmed_img = trim_crop_image(image, 15)
    # trimmed_img.show()
    ### VR

    ### CSM
    # image = SimpleImage('about/csm.png')
    # trimmed_img = trim_crop_image(image, 15)
    # trimmed_img.show()
    # add_border(image, 20)
    # filled_image = fill(image, 0)
    # filled_image.show()

    ###me 
    # image = SimpleImage('laryn.jpg')
    # trimmed_img = crop_vert(image, 100)
    # cropped_img = trim_crop_image(trimmed_img, 75)
    # cropped_img.show()

    ### cs61a
    image = SimpleImage('about/cs61a4.jpg')
    image.show()
    trimmed_img = crop_horiz(image, 20)
    trimmed_img.show()
    # bordered_img = add_border(image, 30)
    # bordered_img.show()
    # recolored_img = recolor(bordered_img, 255)
    # recolored_img.show()
    


def add_border(original_img, border_size):
    """
    This function returns a new SimpleImage which is the same as
    original image except with a black border added around it. The
    border should be border_size many pixels thick.

    Inputs:
        - original_img: The original image to process
        - border_size: The thickness of the border to add around the image

    Returns:
        A new SimpleImage with the border added around original image
    """
    # TODO: your code here
    new_width = original_img.width + (2 * border_size)
    new_height = original_img.height + (2 * border_size)
    result_image = SimpleImage.blank(new_width, new_height)

    for x in range(new_width):
        for y in range(new_height):
            if is_border(x, y, border_size, result_image):
                
                pixel = result_image.get_pixel(x, y)
                pixel.red = 0
                pixel.green = 0
                pixel.blue = 0
                # pixel.red = BORDER_RED
                # pixel.green = BORDER_GREEN
                # pixel.blue = BORDER_BlUE
                # pixel.red = 255
                # pixel.green = 255
                # pixel.blue = 255
            else:
                orig_x = x - border_size
                orig_y = y - border_size
                orig_pixel = original_img.get_pixel(orig_x, orig_y)
                # if (orig_pixel.green < 255):
                #     print(orig_pixel.red, orig_pixel.green, orig_pixel.blue)
                # if orig_x == 5 and orig_y == 2:
                #     print(orig_pixel.red, orig_pixel.green, orig_pixel.blue)
                result_image.set_pixel(x, y, orig_pixel)

    return result_image

def is_border(x, y, border_size, img):

    if x < border_size:
        return True
    if y < border_size:
        return True
    if x >= img.width - border_size:
        return True
    if y >= img.height - border_size:
        return True
    return False

def shift(img, pixels):
    result_image = SimpleImage.blank(img.width, img.height)
    for x in range(result_image.width):
        for y in range(result_image.height):
            orig_pixel = img.get_pixel(x, y)
            res_pixel = result_image.get_pixel(x, (y + pixels) % img.height)
            res_pixel.red = orig_pixel.red
            res_pixel.green = orig_pixel.green
            res_pixel.blue = orig_pixel.blue
    return result_image


def trim_crop_image(original_img, trim_size):
    """
    This function returns a new SimpleImage which is a trimmed and
    cropped version of the original image by shaving trim_size pixels
    from each side (top, left, bottom, right) of the image. You may
    assume trim_size is less than half the width of the image.

    Inputs:
        - original_img: The original image to process
        - trim_size: The number of pixels to shave from each side
                   of the original image

    Returns:
        A new SimpleImage with trim_size pixels shaved off each
        side of the original image
    """
    # TODO: your code here
    new_width = original_img.width - (2 * trim_size)
    new_height = original_img.height - (2 * trim_size)
    result_image = SimpleImage.blank(new_width, new_height)

    for x in range(new_width):
        for y in range(new_height):
            old_x = x + trim_size
            old_y = y + trim_size
            old_pixel = original_img.get_pixel(old_x, old_y)
            result_image.set_pixel(x, y, old_pixel)

    return result_image

def crop_vert(img, trim_size):
    new_height = img.height - (2 * trim_size)
    result = SimpleImage.blank(img.width, new_height)

    for x in range(img.width):
        for y in range(new_height):
            old_y = y + trim_size
            old_pixel = img.get_pixel(x, old_y)
            result.set_pixel(x, y, old_pixel)
    
    return result

def crop_horiz(img, trim_size):
    new_width = img.width - (2 * trim_size)
    result = SimpleImage.blank(new_width, img.height)

    for x in range(new_width):
        for y in range(img.height):
            old_x = x + trim_size
            old_pixel = img.get_pixel(old_x, y)
            result.set_pixel(x, y, old_pixel)
    
    return result

def recolor(img, color):
    result = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            old_pixel = img.get_pixel(x, y)
            if old_pixel.red == 0 and old_pixel.green == 0 and old_pixel.blue == 0:
                new_pixel = result.get_pixel(x, y)
                new_pixel.red = color;
                new_pixel.green = color;
                new_pixel.blue = color;
            else:
                new_pixel.red = old_pixel.red
                new_pixel.green = old_pixel.green
                new_pixel.blue = old_pixel.blue
            # print(old_pixel.red, old_pixel.green, old_pixel.blue)

    return result
if __name__ == '__main__':
    main()