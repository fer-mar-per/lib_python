try:
    from tkinter import *
except ImportError:
    from Tkinter import *
from PIL import Image, ImageSequence, ImageTk
import os


def decodeEscape(*args):
    u"""
    [PUBLIC FUNCTION]
    - It decodes the back slash "\" to the normal slash "/" of the input strings.
        The input strings need to be written as raw strings, using the prefix r"...".

    [ARGUMENTS]
    args:
        - You can directly set the target path(s) as string or list.
            For example: decodeEscape(r"C:\test\myScripts\RestartGUI.py").
    kwargs:
        - None

    [RETURNS]
    - <str/list>    The object(s) with its/their escape decoded.
    """
    if not args:
        raise ValueError("# {}: Please set at least one path.".format('fmpApps'))
    else:
        paths = []
        for arg in args:
            if isinstance(arg, str):
                paths = arg.replace(r"\\", "/").replace(r"\\", "/")
            elif isinstance(arg, (list, tuple)):
                for eachArg in arg:
                    paths.append(eachArg.replace(r"\\", "/").replace(r"\\", "/"))
            else:
                raise ValueError("# {} error: Specified path type is not valid. Please set a string or a list.".format(
                                                                                                        'fmpApps'))
        if paths:
            return paths
        else:
            return None


dir_path = os.path.dirname(os.path.realpath(__file__))
imgPath = '{}/LyUk8.gif'.format(dir_path)


class AnimatedGif(object):
    """ Animated GIF Image Container. """
    def __init__(self, image_file_path):
        # Read in all the frames of a multi-frame gif image.
        self._frames = []
        img = Image.open(image_file_path)
        for frame in ImageSequence.Iterator(img):
            photo = ImageTk.PhotoImage(frame)
            photo.delay = frame.info['duration'] * 10  # Add attribute.
            self._frames.append(photo)

    def __len__(self):
        return len(self._frames)

    def __getitem__(self, frame_num):
        return self._frames[frame_num]


def update_label_image(label, ani_img, frame_num):
    """ Change label image to given frame number of AnimatedGif. """
    global cancel_id
    frame = ani_img[frame_num]
    label.configure(image=frame)
    frame_num = (frame_num+1) % len(ani_img)  # Next frame number.
    cancel_id = root.after(frame.delay, update_label_image, label, ani_img, frame_num)

def enable_animation():
    """ Start animation of label image. """
    global cancel_id
    if cancel_id is None:  # Animation not started?
        cancel_id = root.after(ani_img[0].delay, update_label_image, animation, ani_img, 0)

def cancel_animation():
    """ Stop animation of label image. """
    global cancel_id
    if cancel_id is not None:  # Animation started?
        root.after_cancel(cancel_id)
        cancel_id = None


root = Tk()
root.title("Animation Demo")
root.geometry("250x125+100+100")
ani_img = AnimatedGif(imgPath)
cancel_id = None

animation = Label(image=ani_img[0])  # Display first frame initially.
animation.pack()
Button(root, text="start animation", command=enable_animation).pack()
Button(root, text="stop animation", command=cancel_animation).pack()
Button(root, text="exit", command=root.quit).pack()

root.mainloop()
