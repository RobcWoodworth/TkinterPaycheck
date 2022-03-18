# CS223 Paycheck Lab, Rob Woodworth 1/5/22

# we did a similar assignment in IS103 last quarter making a tip
# calculator in the IDLE, so I wanted to try making a GUI

# tkinter code from pg513, ttk labels from pg515, commands from pg517
# messagebox from pg525, f strings from page 45, rounding from pg265
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# make the window
root = tk.Tk()
root.title(" Robert's Paycheck Calculator")
frame = ttk.Frame(root, padding=(50, 50, 50, 50))
frame.pack(fill=tk.BOTH, expand=True)
ttk.Label(frame, text="Rob Woodworth CS223 Paycheck Lab\n\n").pack()

# input entry boxes
ttk.Label(frame, text="Enter your First name:").pack()
firstnameText = tk.StringVar()
ttk.Entry(frame, width=25, textvariable=firstnameText).pack()

ttk.Label(frame, text="\nEnter your Last name:").pack()
lastnameText = tk.StringVar()
ttk.Entry(frame, width=25, textvariable=lastnameText).pack()

ttk.Label(frame, text="\nEnter your hourly rate of pay:").pack()
wageText = tk.StringVar()
ttk.Entry(frame, width=25, textvariable=wageText).pack()

ttk.Label(frame, text="\nHow many hours worked this period:").pack()
hoursText = tk.StringVar()
ttk.Entry(frame, width=25, textvariable=hoursText).pack()

ttk.Label(frame, text="\n").pack()


# calculate paycheck on button press
def click_button1():
    first_name = firstnameText.get()
    last_name = lastnameText.get()
    your_wage = wageText.get()
    your_hours = hoursText.get()
    gross_income = round(float(your_hours) * float(your_wage), 2)
    fitw = round(float(gross_income) * 0.12, 2)
    medicare = round(float(gross_income) * 0.014, 2)
    oasdi = round(float(gross_income) * 0.06, 2)
    taxes = round(float(fitw) + float(medicare) + float(oasdi), 2)
    take_home = round(float(gross_income) - float(taxes), 2)

    # display paycheck in message box
    # I tried to use the :,.2f format from page 261, but for some reason using
    # it on the float functions causes the name function to break??
    messagebox.showinfo(f"{first_name}'s Paycheck",
                        f"""Name: .................. {last_name}, {first_name}
Hours worked: .... {your_hours}
Hourly rate: ......... ${your_wage}
Gross income: .....  ${gross_income}
\nFITW 12%: .......... ${fitw}
Medicare 1.4%: .. ${medicare}
OASDI 6%: .......... ${oasdi}
\nTotal taxes: ........ ${taxes}
After tax total: ... ${take_home}
\nTotal take home: .. ${take_home}
""")


# big button
ttk.Button(frame, text="Compute paycheck", command=click_button1, padding=(25, 25, 25, 25)).pack()

root.mainloop()
