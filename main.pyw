import requests
import re
from bs4 import BeautifulSoup
from pynotifier import Notification
# Only required if you want to extract the image -- disabled
# from PIL import Image

# If you want to use the icon image file and make the iamge a square -- disabled
# def make_square(im, min_size=256, fill_color=(0, 0, 0, 0)):
#     x, y = im.size
#     size = max(min_size, x, y)
#     new_im = Image.new('RGBA', (size, size), fill_color)
#     new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
#     return new_im

# The product page
#URL = 'https://www.babybunting.com.au/love-to-dream-swaddle-up-designer-lite-0-2-tog-celestial-nights-small.html'
URL = 'https://www.babybunting.com.au/peg-perego-siesta-follow-me-ice.html?fbclid=IwAR0W3M7mNd3ivatiEyrMQz4U5AUOqNURxpGQ6_NiBq3pRewrnd4CtSN5Qxo'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# Extract product name
productname = soup.find(itemprop='name').text.strip()
print(productname)

# Extract price
productpriceextract = soup.find(attrs={'itemprop': 'price'})
productprice = productpriceextract['content']
print(productprice)

# Extract image -- disabled
#productimageextract = soup.find(id='image-main')
#productimage = productimageextract['src']
#img = Image.open(requests.get(productimage, stream = True).raw)
#correctedimage = make_square(img)
#icon_sizes = [(255, 255)]
#correctedimage.save('image.ico', sizes=icon_sizes)
#print(productimage)

if float(productprice) < 479:
    Notification(
        title=productname,
        description=str('$'+productprice),
        # Not really useful with the size on ico image
        #icon_path='image.ico', # On Windows .ico is required, on Linux .png
        duration=60,                              # Duration in seconds
        urgency=Notification.URGENCY_CRITICAL
    ).send()
