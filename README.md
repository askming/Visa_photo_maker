# Visa photo maker
A simple python program to prepare visa photo tile.

## Introduction
- The program defines an object of class `visa_photo()` has features of width and height (in inches)
- `dim()` method prints the dimension of the object
- `print_photo(img, filename, dip, actual_w, actual_h)` method prints the imported `img` to the `visa_photo` object as a photo tile and save it with user given `filename` and `dpi` value; `actual_w` and `actual_h` are the physical (printed) width and height (in inches) of a single photo in the photo tile. For example, US visa photo has the dimension 2 X 2.
- Dependent modules: `Image`, `matplotlib`.

## Example:

```python
>>> import image_process
# initial an empty object with dimension 6 by 4
>>> visa_photo = visa_photo(6, 4)
# read the photo need to be printed
>>> img = Image.open('IMG_1135.JPG')
# print the photo on the canvas with 500 dpi
>>> visa_photo.print_photo(img, 'usvisaphoto.JPG', 500, 2, 2)
```
- Original photo

    <img src="./photo/IMG_1135.JPG" width="350">

- Photo tile (US visa standard) made from the program
    <img src="./photo/usvisaphoto.JPG" width="500">

