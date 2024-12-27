From:
https://stackoverflow.com/questions/28531415/tkinter-animation-will-not-work


----------------------------------------------------------------------
Here's an alternative version of my previous answer. Although also based on the universal Tk 
widget after() method, it uses the PIL (or the pillow fork of it) module to read the gif image file. 
With PIL it's not only easy to extract each frame from the file, but also to get the delay (or "duration") between 
frames of the animation directly from the gif file — which eliminates guessing what it should be for different files.
----------------------------------------------------------------------