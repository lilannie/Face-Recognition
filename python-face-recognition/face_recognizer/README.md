# ok, let's do this

first, you need to install opencv / python. I'm not sure what the windows equivalent to terminal is (I think windows 10 has a super-cmd that is similar? idk not sure) but I used terminal. I used [this rando tutorial](http://www.mobileway.net/2015/02/14/install-opencv-for-python-on-mac-os-x/). Installing everything is the real challenge, the code is actually pretty straightforward once all the gears spin. 

---

here's something important -> this code is set up to run specifically with the yalefaces folder. if you add your own folder of images to test you will need to change more than just 
```
path = './yalefaces'
```

the code relies heavily on images being named "subject[number].[emotion]", which kinda makes sense because there isn't a db backing this up. also I tried using a bunch of celebrities and it failed spectacularly. I'm pretty sure we need a bunch of photos of each person.

**as for the student img database**. kurt verified that we don't have real life sudo powers and ~~sadly~~ thankfully we can't get every student id and mug shot. he sent me a few leads on large public datasets, but the attached oneis the only one this code can run with.

with everything installed you just have to run the `face_recognizer.py` script. it should spazz and show a small window with faces/emotions like it's playing some terrifying old-school psychology film. wherever you ran the script from will print confidence levels for each unknown img, which at the time of writing this is images ending with `.happy`.

opencv is gross.