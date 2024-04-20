import tkinter


def main():
    screen = tkinter.Tk()
    screen.title('PY 6.1.3')
    text = tkinter.Label(screen, text="Whats my favourite Video?")
    text.pack()
    image = tkinter.PhotoImage(file="koral.gif")
    label = tkinter.Label(screen, image=image)
    button = tkinter.Button(screen, text="Favourite Video!", width=25, activebackground="Dark Gray", command=label.pack)
    button.pack()
    screen.mainloop()


if __name__ == '__main__':
    main()
