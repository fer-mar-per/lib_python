import subprocess           # required for redirecting stdout to GUI

try:
    import Tkinter as tk    # required for the GUI python 2
except:
    import tkinter as tk    # required for the GUI python 3


def redirect(module, method):
    '''Redirects stdout from the method or function in module as a string.'''
    proc = subprocess.Popen(["python", "-c",
        "import " + module + ";" + module + "." + method + "()"], stdout=subprocess.PIPE)
    out = proc.communicate()[0]
    return out.decode('unicode_escape')

def put_in_txt():
    '''Puts the redirected string in a text.'''
    txt.insert('1.0', redirect(module.get(), method.get()))


if __name__ == '__main__':

    root = tk.Tk()

    txt = tk.Text(root)
    module = tk.Entry(root)
    method = tk.Entry(root)
    btn = tk.Button(root, text="Redirect", command=put_in_txt)

    #layout
    txt.pack(fill='both', expand=True)
    module.pack(fill='both', expand=True, side='left')
    btn.pack(fill='both', expand=True, side='left')
    method.pack(fill='both', expand=True, side='left')

    root.mainloop()
