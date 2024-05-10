from tkinter import *
from PIL import ImageTk,Image 
import os

# Set the title of the application, including a background picture
root = Tk()
root.title("Kevin's Ice Cream Ordering Portal")
home_image = ImageTk.PhotoImage(Image.open("ice_cream_background.png"))

selections = {"order_type": "", "style": "", "size": "", "toppings": []}

# Create the welcome label, and then prompting the user to place their order.
welcome = Label(root, text="Welcome to Kevin's Ice Cream Ordering Portal. \n Please take a moment and place your order!", font=5)
welcome.grid(row=1, columnspan=2)

# Insert a label asking the user if they will be dining in or taking out. Define buttons used to choose which of these options, or to cancel the order.
in_or_out = Label(root, text="Will you be Dining in or Taking out?", font=1)
in_or_out.grid(row=2, columnspan=2, pady=5)

in_order = Button(root, text="Dine-in", command=lambda: select_order_type("Dine-in"), height=5, width=10)
in_order.grid(row=3, column=0, pady=5)

out_order = Button(root, text="Carry out", command=lambda: select_order_type("Carry out"), height=5, width=10)
out_order.grid(row=3, column=1, pady=5)

exit_order = Button(root, text="Cancel", command=root.destroy)
exit_order.grid(row=4, columnspan=2, pady=5)

home_img = Label(root, image=home_image)
home_img.grid(row=0, columnspan=2)

# Define the order type.
def select_order_type(order_type):
    selections["order_type"] = order_type
    order_style()

# Define the options to choose cone or sundae, while also inserting buttons to move on to the next page.
def order_style():
    window = Toplevel()
    window.title("Kevin's Creamy Confections")

    choose_your_style = Label(window, text="Kevin's Ice Cream Ordering Portal. \n Choose either cone or sundae!", font=5)
    choose_your_style.grid(row=0, columnspan=2)

    cone = Button(window, text="Cone", command=lambda: select_style("Cone"), height=5, width=10)
    cone.grid(row=2, column=0, pady=5)

    sundae = Button(window, text="Sundae", command=lambda: select_style("Sundae"), height=5, width=10)
    sundae.grid(row=2, column=1, pady=5)

    return_screen = Button(window, text="Return to the previous screen", command=window.destroy)
    return_screen.grid(row=3, columnspan=2, pady=5)

    exit_order = Button(window, text="Cancel and close order", command=root.destroy)
    exit_order.grid(row=4, columnspan=2, pady=5)

    def select_style(style):
        selections["style"] = style
        order_size()

# Define order size, asking for one, two, or three scoops of ice cream. Inserting buttons to choose from the three options.
def order_size():
    window = Toplevel()
    window.title("Kevin's Ice Cream Ordering Portal")

    choose_your_size = Label(window, text="Kevin's Ice Cream Ordering Portal. \n Would you like one, two, or three scoops?", font=5)
    choose_your_size.grid(row=0, columnspan=3)

    scoop1 = Button(window, text="One Scoop", command=lambda: select_size("One Scoop"), height=5, width=10)
    scoop1.grid(row=2, column=0, pady=5)

    scoop2 = Button(window, text="Two Scoops", command=lambda: select_size("Two Scoops"), height=5, width=10)
    scoop2.grid(row=2, column=1, pady=5)

    scoop3 = Button(window, text="Three Scoops", command=lambda: select_size("Three Scoops"), height=5, width=10)
    scoop3.grid(row=2, column=2, pady=5)

    return_screen = Button(window, text="Go back to the previous screen", command=window.destroy)
    return_screen.grid(row=3, columnspan=3, pady=5)

    exit_order = Button(window, text="Cancel and close order", command=root.destroy)
    exit_order.grid(row=4, columnspan=3, pady=5)

    def select_size(size):
        selections["size"] = size
        order_toppings()

# Define the order toppings, giving the user the option to choose form a set number of toppings, or submitting without choosing a topping.
def order_toppings():
    window = Toplevel()
    window.title("Kevin's Ice Cream Ordering Portal")

    choose_your_toppings = Label(window, text="Kevin's Ice Cream Ordering Portal. \n What kind of toppings would you like?", font=5)
    choose_your_toppings.grid(row=0, columnspan=3)

    toppings = Listbox(window, selectmode="multiple")
    toppings.config(width=0,height=0)
    items = ["Nuts", "Chocolate", "Strawberry and pineapple syrup", "Whip cream", "Sprinkles", "Sugar cookies", "Bananas", "Cherry on top"]
    for item in items:
        toppings.insert(END, item)
    toppings.grid(row=1, columnspan=3)

# Insert the review order button, allowing users to review what they'd selected.
    review_order = Button(window, text="Review Order", command=lambda: [select_toppings(), order_review()])
    review_order.grid(row=2, columnspan=3, pady=5)

    return_screen = Button(window, text="Go back to previous screen", command=window.destroy)
    return_screen.grid(row=3, columnspan=3, pady=5)

    exit_order = Button(window, text="Cancel and close order", command=root.destroy)
    exit_order.grid(row=4, columnspan=3, pady=5)

    def select_toppings():
        selections["toppings"] = [items[i] for i in toppings.curselection()]


def order_review():
    window = Toplevel()
    window.title("Kevin's Ice Cream Ordering Portal")

    review = Label(window, text="Kevin's Ice Cream Ordering Portal. \n Review your order below, then submit and we'll start working on your order!", font=5)
    review.grid(row=0, columnspan=3)

    order_type_label = Label(window, text=f"Order Type: {selections['order_type']}")
    order_type_label.grid(row=1, columnspan=3)

    style_label = Label(window, text=f"Style: {selections['style']}")
    style_label.grid(row=2, columnspan=3)

    size_label = Label(window, text=f"Size: {selections['size']}")
    size_label.grid(row=3, columnspan=3)
# Initiate an if/else statement for the toppings, where if no toppings are selected then the following menu shows that no toppings were selected.
    if not selections["toppings"]:
        toppings_label = Label(window, text="Toppings: No toppings added")
        toppings_label.grid(row=4, columnspan=3)
    else:
        toppings_label = Label(window, text=f"Toppings: {', '.join(selections['toppings'])}")
        toppings_label.grid(row=4, columnspan=3)

    submit_order = Button(window, text="Submit Order", command=submit)
    submit_order.grid(row=5, columnspan=3, pady=5)

    return_screen = Button(window, text="Go back to the previous screen", command=window.destroy)
    return_screen.grid(row=6, columnspan=3, pady=5)

    exit_order = Button(window, text="Cancel and close order", command=root.destroy)
    exit_order.grid(row=7, columnspan=3, pady=5)

# Define the submit button, so that the order can be submitted and placed at the end of the application.
def submit():
    window = Toplevel()
    window.title("Kevin's Ice Cream Ordering Portal")

    review = Label(window, text="Kevin's Ice Cream Ordering Portal. \n Thank you for submitting your order, have a great day!", font=5)
    review.grid(row=1, columnspan=3)

    exit_order = Button(window, text="Close order", command=root.destroy)
    exit_order.grid(row=2, columnspan=3, pady=5)

    home_img = Label(window, image=home_image)
    home_img.grid(row=0, columnspan=3)



root.mainloop()
