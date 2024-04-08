![header](https://capsule-render.vercel.app/api?type=slice&height=300&color=gradient&customColorList=0,2,2,5,4,6,8,10,12,14,16,20,30&text=Encryption%20Decryption%20of%20Image&fontSize=50&fontAlign=54&rotate=19&fontAlignY=45&textBg=false&animation=twinkling)
# Prodigy_CS_Task2
Encrypting and Decrypting an Image using `PIL library` by swapping **pixel values.**

### Libraries Used:
+ `PIL`
+ `Requests`
+ `IO`

## How to Use:
> Run using [Jupyter NoteBook](https://jupyter.org/) or any Python IDE.  

### `For V1.0`

+ **Enter Local Path of the Image File:**
> e.g C:\Users\[Username]\Downloads\[Image-Filename].[Extension]
+ **Format**
> C:\Users\Downloads\test.png

### `For V1.1`

+ **Enter URL of the Image File:**
> e.g Direct Link/URL
+ **Format**
> https://static.desygner.com/wp-content/uploads/sites/13/2022/05/04141642/Free-Stock-Photos-01.jpg 
+ OR 
> https://raw.githubusercontent.com/sadbattery/Prodigy_CS_Task2/67a27741c250ee40c9d7e4d6e3362b1b4980f83f/Sample%20Images/Free-Stock-Photos-01.jpg

## Installation:

#### ***PIL (Python Imaging Library) :***
> Pillow (Python Imaging Library): Pillow is used for image manipulation tasks like opening, saving, and modifying images.
```bash
pip install Pillow
```
#### ***Requests :***
> Requests library is used for making HTTP requests to download images from URLs. (It will be used in V1.1)
```bash
pip install requests
```
#### ***IO (Input/Output) :***
> This module provides facilities for working with various types of I/O (input/output) in Python.
---
> In the `V1.1` code, BytesIO from the io module is used to convert the response content from the requests library into a file-like object that PIL can work with.
