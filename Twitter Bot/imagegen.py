import requests
import json
import textwrap
import config
def generate_image():
    category = 'success'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': config.X_Api_Key})
    if response.status_code == requests.codes.ok:
        data = response.json()
    else:
        print("Error:", response.status_code, response.text)
    quote = data[0]["quote"]
    author = data[0]["author"]
    from PIL import Image,ImageDraw,ImageFont,ImageFilter
    W, H = (1920,1080)
    img = Image.new(mode="RGB",size=(1920,1080),color=(0, 0, 24))
    img = Image.open("./template.png")
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("Utendo-Bold.ttf",size=62)
    message="\"" + quote + "\"" + " " + author
    wrapper = textwrap.TextWrapper(width=50) 
    word_list = wrapper.wrap(text=message) 
    caption_new = ''
    for ii in word_list[:-1]:
        caption_new = caption_new + ii + '\n'
    caption_new += word_list[-1]
    print(caption_new)

    w,h = fnt.getsize(message)
    x = (W-w)/2
    y = (H-h)/2
    if x < 0:
        x=60
    if y < 0:
        y=0
    print(x,y)
    draw.text(xy=(x,y),text=caption_new,size=92,font=fnt)
    img.save("test.png")
    return quote,author
