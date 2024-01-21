# WaterMarking App

The Watermarking App is a simple but effective tool for quick watermarking of photos without needing to have bulky or expensive photo editing software. Simply load a photo, write whatever name you'd like to watermark the photo with, and hit the "Mark It!" button. If happy with the photo, simply save it and you're done!

## Install Instructions

Clone this repo and run using `python main.py` to have the GUI to pop up.

## App Instructions

Just as simple as in the descriptition

1. Once the application is open, hit the "Load" button and select the image you want to mark.

2. The Image will be viewable in the window once opened, below it is a text box where you can type whatever you want to be watermarked onto the image.

3. Once satisfied with the text, hit the "Mark It!" button and the image should show the watermarkings in the window.

4. Click the "Save" button to save your image to a new file, and enjoy your photo!

## Project Writeup

Day 85 proved to be as time consuming as the previous projects. It's becoming apparent that I need to work on properly scoping and planning the applications that I write. There is no need for these programs to take 4 or 5 days when they're meant to be daily project, and I seem to get lost in the weeds several times over on different features. 

Perhaps the most time consuming was the math portion of this project. There are many ways to watermark a photo, and obviously the easiest way would be to put a single watermark in a consistent spot, however I wanted to try something a bit more common, not to mention useful, where the watermarking occurs in a reoccuring pattern around the image so that the parts around a watermark can't be used. 

One thing I was definitely proud of is after realizing text that goes off the image is completely disregarded, I discovered I could watermark a blank image larger than the photo to be marked, and then crop that larger blank image, which allowed partial watermarks to exist on the ends of the photo, creating a uniform pattern style.

I definitely reached a point where I felt I had to stop for time sake, but if I were to dedicate more time, I would definitely clean inputs better, so that a whole sentence couldn't be given as a watermark and look silly for example. I would fine tune my logic to specifically accomodate different sized photos so that the watermark was always clear, and lastly I would add a slider, or some other input method for the user to be able to change how closely clustered the watermarkings are.