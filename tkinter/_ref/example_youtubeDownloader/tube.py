from tkinter import Tk,Button,Label,StringVar,Entry
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from pytube import YouTube

root = Tk()
root.title('Youtube downloader')
root.configure(background="yellow")
root.minsize(width=420, height=100)
root.resizable(width=False, height=False)

def open_file():
    global directory
    directory = askdirectory()
    print(directory)



def download():
    if len(link.get()) == 0:
        messagebox.showerror("Link Empty", "Link can not be empty")
    else:
        YouTube(link.get()).streams.first().download(directory)
        messagebox.showinfo("Complete", "Video downloaded successfully")
        link_entry.delete(0, 'end')




link_lbl = Label(root, text="Enter link", font='Helvetica 15',bg="purple",fg="white")
link_lbl.grid(row=1, column=0)

link = StringVar()
link_entry = Entry(root, textvariable=link, width=50, borderwidth=4)
link_entry.grid(row=1, column=1)

select_dir = Button(root, text="Choose Directory", width=15, command=open_file,bg="blue",fg="white")
select_dir.grid(row=1, column=2)

download_btn = Button(root, text="Download", width=10, command=download,bg="green",fg="white")
download_btn.grid(row=2, column=1)

root.mainloop()
