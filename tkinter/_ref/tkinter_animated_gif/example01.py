try:
    from tkinter import *
except ImportError:
    from Tkinter import *  # Python 2
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
imgPath = '{}/_ico/LyUk8.gif'.format(dir_path)


class AnimatedGif(object):
    """ Animated GIF Image Container. """
    def __init__(self, image_file_path):
        # Read in all the frames of a multi-frame gif image.
        self._frames = []

        frame_num = 0  # Number of next frame to read.
        while True:
            try:
                frame = PhotoImage(file=image_file_path,
                                   format="gif -index {}".format(frame_num))
            except TclError:
                break
            self._frames.append(frame)
            frame_num += 1

    def __len__(self):
        return len(self._frames)

    def __getitem__(self, frame_num):
        return self._frames[frame_num]


def update_label_image(label, ani_img, ms_delay, frame_num):
    global cancel_id
    label.configure(image=ani_img[frame_num])
    frame_num = (frame_num+1) % len(ani_img)
    cancel_id = root.after(
        ms_delay, update_label_image, label, ani_img, ms_delay, frame_num)

def enable_animation():
    global cancel_id
    if cancel_id is None:  # Animation not started?
        ms_delay = 1000 // len(ani_img)  # Show all frames in 1000 ms.
        cancel_id = root.after(
            ms_delay, update_label_image, animation, ani_img, ms_delay, 0)

def cancel_animation():
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
