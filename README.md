# Safty
> If you have any suggestion please contact me :smile:

Safty is really simple security app that can help you catch anyone that uses your computer/laptop without your knowledge.

Best way to use safty is to add it to startup programs. So everytime someone turn on computer/laptop a camera will take ona snap and save wherever you want.
> Pictures are named in format Year-Month-Day_Hour-Minute-Second.

**It's using openCV so before you use it you need to install openCV.**

```
install python-opencv bindings, numpy
```

or with pip

```
pip install opencv-python
```

# Setting up Safty
1) Create batch file that will have this:

```
python safty.py
```

2) Put that batch file and safty.py anywhere on your drive

3) Create shortcut of that batch file and place it in:
For Windows 10/8/7:
```
C:\Users\*YOUR_USERNAME*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

4) And that's it. Now everytime you turn your computer on camera will take one picture and save it (by default, but you can change it) in 'Pictures' folder in C:\User.

# Your changes
- If you have more then one camera and want any specific camera to take a snap you can change that on line 5. All your cameras has numbers (0 is for default one, then 1,2,3,...) so you have to check what camera you want.
```
cam = cv2.VideoCapture(*CAMERA_NUMBER*,cv2.CAP_DSHOW)
```

- Also if you want your picture to be saved somewhere else you can do that by changing line 10, where you can place any path you want.

# Releases
**1.0** Initial release
