import glob
from PIL import Image
pasta = r'C:\Users\hansc\Downloads\pics'
pictures = glob.glob(f'{pasta}\\*.png')
print(pictures)
[Image.open(pic).convert('L').save(pic[:-3] + 'jpg') for pic in pictures]
