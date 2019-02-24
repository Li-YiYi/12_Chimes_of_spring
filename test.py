# -*- coding:UTF-8 -*-
import time,random
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess
from gpiozero import Button

print ('程序开始')

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
b1 = Button(19)

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
#padding = -2
#top = padding
#bottom = height-padding
#x = 0
font16 = ImageFont.truetype('/root/oledt/ch.ttf',16)
font = ImageFont.truetype('/root/oledt/ch.ttf',14)
draw.text((48,0),"警告！",  font=font16, fill=255)
draw.text((0,17),"接入发动机控制系统",  font=font, fill=255)
disp.image(image)
disp.display()
time.sleep(1)
draw.rectangle((0,0,127,63), outline=0, fill=0) 
draw.rectangle((0,32,127,48), outline=255, fill=0) 
draw.rectangle((0,0,127,15), outline=255, fill=0)
draw.text((0,17),"正在加载春节十二响",  font=font, fill=255)
draw.text((1,1),"发动机控制系统",  font=font, fill=255)
draw.text((1,33),"0%",  font=font, fill=255)

disp.image(image)
disp.display()
for i in range(1,126):
    draw.rectangle((0,32,i,48), outline=255, fill=1)
    draw.text((1,33),str(int(i/1.28)+2)+'%',  font=font, fill=0)
    time.sleep(random.random()/30)
    disp.image(image)
    disp.display()
time.sleep(1)
draw.text((32,49),"激活Windows",  font=font, fill=255)
disp.image(image)
disp.display()
time.sleep(3)
draw.rectangle((32,49,127,63), outline=0, fill=0) 
disp.image(image)
disp.display()
b1.wait_for_release()
time.sleep(0.5)
b1.wait_for_press()
time.sleep(0.5)
draw.rectangle((0,32,127,48), outline=255, fill=1)
draw.text((1,33),str(100)+'%',  font=font, fill=0)
draw.rectangle((1,16,127,48), outline=0, fill=0) 
draw.text((0,16),"加载完成！",  font=font, fill=255)
disp.image(image)
disp.display()
draw.rectangle((0,32,127,48), outline=255, fill=1)
draw.text((1,33),'新年快乐！',  font=font, fill=0)
disp.image(image)
disp.display()
time.sleep(15)