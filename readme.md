# SVG Turtle! 🐢
Turn your Turtle drawing to an SVG file. We will then turn the SVG into a sticker!  
Follow the directions in template.py. Read line 9, and start drawing on line 12!

### Turn the turtle drawing to an SVG
We will do this part together as a class. When you are completely done with your drawing:
1. At the top of the file, delete these lines:
```
import turtle
t = turtle.Turtle()
t.shape("turtle")
```
2. And uncomment these lines:
```
# from svg_turtle import SvgTurtle
# t = SvgTurtle(400, 400)
```
3. Make sure your first name has no spaces in it!
4. At the bottom of the file, delete this line:
```
t.screen.mainloop() # keep the turtle window open
```
5. And uncomment this line:
```
# t.save_as(first_name + ".svg")
```
6. Open a new terminal with <b>ctrl + shift + `</b>
7. Run the Python file in the terminal with this command:
```
python template.py
```
8. You should then see your svg file in the project folder!
9. Attach your svg file to Google Classroom.