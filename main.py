# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os.path
import turtle


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
'import PIL'

import random
from PIL import Image
from PIL import ImageChops
import tkinter as tk
from tkinter import filedialog
import os
from PIL import ImageDraw,ImageFont
img1_path='D:\毕设\patterns/1 miao/Abundance.png'
img2_path='D:\毕设\patterns/1 miao/Auspicious.png'
img3_path='D:\毕设\patterns/1 miao/Bright.png'
img5_path='D:\毕设\patterns/1 miao/Auspicious.png'
img6_path='D:\毕设\patterns/1 miao/Auspicious.png'
img7_path='D:\毕设\patterns/1 miao/Flourish.png'
img8_path='D:\毕设\patterns/1 miao/Happiness and contentment.png'
img9_path='D:\毕设\patterns/1 miao/Harmonious.png'
img10_path='D:\毕设\patterns/1 miao/Healthy.png'
img11_path='D:\毕设\patterns/1 miao/Longevity.png'
img12_path='D:\毕设\patterns/1 miao/Lucky.png'
img13_path='D:\毕设\patterns/1 miao/Peaceful.png'
img14_path='D:\毕设\patterns/1 miao/Prosperity.png'
img15_path='D:\毕设\patterns/1 miao/Rich.png'
img16_path='D:\毕设\patterns/2 dai/Thriving.png'
img17_path='D:\毕设\patterns/2 dai/active.png'
img18_path='D:\毕设\patterns/2 dai/positive.png'
img19_path='D:\毕设\patterns/2 dai/flourishing.png'
img20_path='D:\毕设\patterns/2 dai/Vibrant.png'
img21_path='D:\毕设\patterns/2 dai/fortunate.png'
img22_path='D:\毕设\patterns/2 dai/good.png'
img23_path='D:\毕设\patterns/2 dai/tranquil.png'
img24_path='D:\毕设\patterns/2 dai/bold and geneous.png'
img25_path='D:\毕设\patterns/2 dai/adoring.png'
img26_path='D:\毕设\patterns/2 dai/ruyi.png'
img27_path='D:\毕设\patterns/2 dai/longevity.png'
img28_path='D:\毕设\patterns/2 dai/energetic.png'
img29_path='D:\毕设\patterns/2 dai/safe and rich.png'
img30_path='D:\毕设\patterns/2 dai/bright.png'
img31_path='D:\毕设\patterns/3 yi/smoothly.png'
img32_path='D:\毕设\patterns/3 yi/auspicious.png'
img33_path='D:\毕设\patterns/3 yi/courage and love.png'
img34_path='D:\毕设\patterns/3 yi/love nature.png'
img35_path='D:\毕设\patterns/3 yi/nature conservation.png'
img36_path='D:\毕设\patterns/3 yi/peaceful.png'
img37_path='D:\毕设\patterns/3 yi/persevnt.png'
img38_path='D:\毕设\patterns/3 yi/secure.png'
img39_path='D:\毕设\patterns/3 yi/status.png'
img40_path='D:\毕设\patterns/3 yi/wealthy.png'
img41_path='D:\毕设\patterns/3 yi/ancestral protection.png'
img42_path='D:\毕设\patterns/3 yi/fine.png'
img43_path='D:\毕设\patterns/3 yi/safe.png'
img44_path='D:\毕设\patterns/3 yi/pretty.png'
img45_path='D:\毕设\patterns/3 yi/beautiful.png'
image_folder1=[img1_path,img2_path]
image_floder2=[img31_path,img32_path,img33_path,img34_path,img35_path,img36_path,img37_path,img38_path,img39_path,img40_path,img41_path,img42_path,img43_path,img44_path,img45_path]
image_floder3=[img16_path,img17_path,img18_path,img19_path,img20_path,img21_path,img22_path,img23_path,img24_path,img25_path,img26_path,img27_path,img28_path,img29_path,img30_path]
image1_path=random.choice(image_folder1)
name1=os.path.basename(image1_path)
new_name1=os.path.splitext(name1)[0]
image1=Image.open(image1_path)
image2_path=random.choice(image_floder2)
name2=os.path.basename(image2_path)
new_name2=os.path.splitext(name2)[0]
image2=Image.open(image2_path)
image3_path=random.choice(image_floder3)
name3=os.path.basename(image3_path)
new_name3=os.path.splitext(name3)[0]
image3=Image.open(image3_path)
canvas = Image.new('RGB',(2362,2600),(0,0,0))
image33=image3.resize((1600,1600))
image22=image2.resize((805,805))
canvas.paste(image1,(0,0),)
canvas.paste(image33,(385,385))
canvas.paste(image22,(785,785))
draw=ImageDraw.Draw(canvas)
image_names=[new_name1,new_name2,new_name3]
template='This pattern hopes you have a {},{} and {} life !'
filled_text=template.format(image_names[0],image_names[1],image_names[2])
font=ImageFont.load_default(size=60)
draw.text((50,2500),filled_text,(255,255,255),font)
canvas.show()
