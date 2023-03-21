import tkinter

time = 10
running = False


def increment_timer(event):
    global running
    if not running:
        global time
        time += 30
        update_display()


def decrement_timer(event):
    global time
    global running
    if not running:
        if time > 30:
            time -= 30
            update_display()
        else:
            time = 0
            running = False
            time_display.config(bg='green')
            window.config(bg='green')
            update_display()


def update_display():
    global time
    if running:
        if time < 30:
            window.configure(bg="red")
            time_display.config(bg="red", fg="white")
        elif time < 60:
            window.configure(bg="yellow")
            time_display.config(bg="yellow", fg="black")
        else:
            window.configure(bg="green")
            time_display.config(bg="green", fg="white")
    else:
        time_display.config(text="Time is up.")
    minutes = int(time / 60)
    seconds = time % 60
    if seconds < 10:
        formatted_seconds = f"0{seconds}"
        seconds = formatted_seconds
    # if seconds == 0:
    #     seconds = "00"
    time_display.config(text=f"{minutes}:{seconds}")


def start_stop(event):
    global running
    if running:
        running = False
    else:
        running = True
        countdown()


def countdown():
    global time
    global running
    if time > 0 and running:
        update_display()
        time -= 1
        window.after(1000, countdown)
    elif time == 0:
        update_display()
        window.after(1000, update_display)
        running = False


def reset_timer(event):
    global running
    if not running:
        global time
        time = 0
        update_display()
        window.config(bg='green')
        time_display.config(bg='green')

# Need better way to hide window borders without also hiding taskbar icon
# def hide_border(event):
#     window.overrideredirect(1)
#
# def show_border(event):
#     window.overrideredirect(0)


window = tkinter.Tk()
window.config(padx=10, pady=10, bg='green')
window.title("Debate Timer")
# window.iconbitmap("stopwatch image.ico")

time_display = tkinter.Label(text="", font=("Arial", 100, 'normal'), fg='white', bg='green')
time_display.grid(column=0, row=0)
update_display()

window.bind('<Up>', increment_timer)
window.bind('<Down>', decrement_timer)
window.bind('<space>', start_stop)
window.bind('<r>', reset_timer)
# window.bind('<h>', hide_border)
# window.bind('<s>', show_border)

window.mainloop()
