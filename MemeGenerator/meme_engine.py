#  TODO: create image using Pillow, add text, and return a path
from PIL import Image, ImageDraw, ImageFont
import textwrap
import random 


class MemeEngine:
    """ This is meme generator class.

    args: output_dir  
    """

    def __init__(self, output_dir):
        self.output_dir = output_dir
  
    
    def make_meme(self, quote, author):
        img_name = random.randint(0,10)
        in_path='./output/cute.jpg'
        out_path=f'./static/images/test{img_name}.jpg'
        with Image.open(in_path) as img:  
  
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=45)
            #draw.text((100, 300), message, fill='black')

            (x, y) = (50, 50)
            color = 'rgb(0, 0, 0)' # black color
            
            # draw the message on the background
            lines = textwrap.wrap(f'{quote} -{author}', width=25)
            margin = offset = 40
            for line in lines:
                draw.text((margin, offset), line, font=font, fill=color)
                offset += font.getsize(line)[1]
            img = img.resize((200,200))
            img.save(out_path)
        out_path = f'{self.output_dir}/test{img_name}.jpg'
        return out_path
        
