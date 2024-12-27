From:
https://stackoverflow.com/questions/28531415/tkinter-animation-will-not-work


----------------------------------------------------------------------
You can use the universal Tk widget after() method to schedule a function to run after a specified delay given in milliseconds. 
This only happens once, so typically the function itself also calls after() to perpetuate the process.

In the code below a custom AnimatedGif container class is defined which loads and holds all the frames of animated 
sequence separately in a list which allows quick (random) access to them using [] indexing syntax. It reads individual 
frames from the file using the -index indexvalue image format suboption mentioned on 
the photo Tk manual page (https://www.tcl.tk/man/tcl8.6/TkCmd/photo.html#M49).

You should be able use the same technique to animate multiple images or those that are attached to other kinds of widgets, such as Button and Canvas instances.
----------------------------------------------------------------------