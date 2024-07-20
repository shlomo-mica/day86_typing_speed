import tkinter as tk

counter = []
story = "A selfish princess meets a frog,after dropping a golden ball into a well under a linden tree. The frog " \
        "offers to retrieve the ball in exchange for her friendship.\n\n\n\n\n\n "

# " She agrees but goes back on her word after getting her "
# "ball back and runs back to her castle. The next day, "
# "she is eating with her father the king when the frog knocks "
# "on the door and requests to be let in. The king tells his daughter"
# " that she must keep her promise and she reluctantly obeys. "
# "The frog sits next to her and eats from her plate,"
# " then desires to sleep in the princesss bed."
# " She is disgusted at the idea of sleeping with the frog,"
# " but her father angrily chastises her for loathing someone"
# " who helped her in a time of'"
c = 0
b = 60

def key_press_detect(event):  # When any key is pressed
    global c
    c += 1
    chars_typing_numbers.config(text=event.char)
    chars_typing_numbers.config(text=c)
    print(c)  # Update the text on Label
    for widget in root.winfo_children():  # Collect all classes of the widgets
        if isinstance(widget, tk.Button):  # If it belongs to button class
            if widget['text'] == event.char or widget['text'].lower() == event.char:
                widget['relief'] = 'sunken'  # Update relief option to pressed
                widget.invoke()


def key_handler(event):
    print("Pressed key:", event.char, counter.append(event.char), "Keysym:", event.keysym, "Keycode:", event.keycode)
    print(len(counter))


def stop():
    root.quit()
    return "stop action"


def new_timer():
    root.after(5000, stop)


def start():
    # timer_digit2.config(text=7)
    root.after(60000, stop)


def count_down_start():
    countdown(60)


def countdown(count):
    # change text in label
    timer_digit2['text'] = count

    if count > 0:
        global job
        # call countdown again after 1000ms (1s)
        job = root.after(1000, countdown, count - 1)
    else:
        timer_digit2['text'] = 'stop'


root = tk.Tk()
root.geometry('1200x600')
root.config(bg='pink')

canvas2 = tk.Canvas(root, bg='red')
canvas2.create_text(82, 35, text=" timer on line", width=112, font=('Arial', 18))
canvas2.create_line(33, 175, 400, 15, width=5)
canvas2.grid(column=12, row=24)

text_area = tk.Text(root, width=45, font=('Arial', 18), height=15, highlightbackground='#40E0D0', bg='#40E0D0',
                    fg="blue")
text_area.insert('1.0', story)
text_area.insert(2.0, '-------------------------------------------------------------------------')
text_area.grid(column=0, row=0)
# anchor: Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"]




timer_digit2 = tk.Label(root, text=b, width=2, bg="pink", font=('Arial', 35), fg='green')
timer_digit2.grid(column=1, row=0)

start_button = tk.Button(text='Start typing', font=('Arial', 25), command=count_down_start, width=15)
start_button.grid(column=2, row=0)

chars_typing_numbers = tk.Label(root, text="#", width=2, bg="pink", font=('Arial', 35), fg='green')
chars_typing_numbers.grid(row=0, column=3)
root.bind('<Key>', key_press_detect)

root.mainloop()
