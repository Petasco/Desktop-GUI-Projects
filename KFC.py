from tkinter import  *
import  tkinter as tk
from PIL import Image, ImageTk

petasco = Tk()
chicken = tk.StringVar
pizza = tk.StringVar
ice = tk.StringVar

petasco.title('KFC ONLINE FOOD ORDERING')
petasco.geometry('1300x700')
introlbl = Label(petasco, text='WELCOME TO PETASCO KFC', font=('algeria', 28, 'bold'),bg='blue', fg='gold', width=55 )
introlbl.place(x=15, y=1)

'''frame = Frame(petasco, highlightbackground='blue', highlightthickness=3, highlightcolor='red',height=10,width=50)
#frame.place(x=50, y=100)
frame.pack(pady=60, padx=250)
cusName = Label(frame, text='Customer Name:', font=('TIMES', 13, 'bold'))
cusName.pack(padx=10, pady=50)'''
# --------------------------------------------------- customer info label -----------------------------------------------------------
customerinfo_lbl = Label(petasco, text='================================= Customer Info =================================', font=('Arial', 15, 'bold'))
customerinfo_lbl.place(x=160, y=60)

customerlbl = Label(petasco, text='Customer Name:', font=('times', 13, 'bold'))
customerlbl.place(x=15, y=90)

customerName_var = StringVar()
customer_entry = Entry(petasco,textvariable=customerName_var,font=('times', 13, 'bold'), bd=2)
customer_entry.focus()
customer_entry.place(x=145, y=90)

customerPhone = Label(petasco, text='Phone No:', font=('times', 13, 'bold') )
customerPhone.place(x=350, y=90)
customerPhone_var = StringVar()
phone_entry = Entry(petasco,textvariable=customerPhone_var ,font=('times', 13, 'bold'), bd=2)
phone_entry.place(x=430, y=90)

billNo_lbl = Label(petasco, text='Bill No:', font=('Arial', 13, 'bold'))
billNo_lbl.place(x=630, y=90)
customerBill_var = IntVar()
bill_entry = Entry(petasco,textvariable=customerBill_var ,font=('times', 13, 'bold'), bd=2)
bill_entry.place(x=690, y=90)

customerAddress = Label(petasco, text='Customer Address: ', font=('Arial', 13, 'bold'))
customerAddress.place(x=890, y=90)
customerAddress_var = StringVar()
customerAddress_en = Entry(petasco,textvariable=customerAddress_var ,font=('times', 13, 'bold'), bd=2 )
customerAddress_en.place(x=1050, y=90)
# ----------------------------------------------Food  Menu ---------------------------------------------------------------------------
#menu_frame = LabelFrame(petasco,text='MENU', highlightbackground='blue',bg='gold',fg='white' , pady=10, padx=10)
#menu_frame.grid(row=50, column=15)

Fmenu_lbl = Label(petasco, text='============FOOD MENU============', font=('times', 14, 'bold'))
Fmenu_lbl.place(y=120, x=15)
# ------------------------------ Items label -------------------------------
items = Label(petasco, text='ITEM', font=('times', 13, 'bold'))
items.place(y=150, x=20)
# ====================================================================================
chicken_lbl = Label(petasco, text='Chicken', font=('times', 13, 'bold'))
chicken_lbl.place(x=20, y=180)


chicken_price = Label(text='$5', font=('times', 13, 'bold'))
chicken_price.place(y=180, x=180)

chickenVar = IntVar()
chicken_qty = Entry(petasco,textvariable=chickenVar, font=('times', 13, 'bold'), bd=2,width=7)
chicken_qty.place(y=180, x=300)
#chicken = int(chicken_qty.get())


#=========================================================================================

# ====================================================================================
#image = ImageTk.PhotoImage(Image.open(r'C:\Users\peter\OneDrive\Desktop\Bluetooth\piza.jpg'))
pizza_lbl = Label(petasco, text='Pizza', font=('times', 13, 'bold'))
pizza_lbl.place(x=20, y=220)
#pizza_lbl['compound'] = tk.RIGHT
#pizza_lbl['image'] = image

pizza_price = Label(text='$10', font=('times', 13, 'bold'))
pizza_price.place(y=220, x=180)

pizzaVar = IntVar()
pizza_qty = Entry(petasco,textvariable=pizzaVar,font=('times', 13, 'bold'), bd=2,width=7)
pizza_qty.place(y=220, x=300)


#=========================================================================================
friesvar = IntVar()
# ====================================================================================
fries_lbl = Label(petasco, text='Fries', font=('times', 13, 'bold'))
fries_lbl.place(x=20, y=260)

fries_price = Label(text='$1.5', font=('times', 13, 'bold'))
fries_price.place(y=260, x=180)

fries_qty = Entry(petasco, textvariable=friesvar, font=('times', 13, 'bold'), bd=2,width=7)
fries_qty.place(y=260, x=300)

#=========================================================================================

# ====================================================================================
ice_lbl = Label(petasco, text='Ice Cream', font=('times', 13, 'bold'))
ice_lbl.place(x=20, y=300)

ice_price = Label(text='$3', font=('times', 13, 'bold'))
ice_price.place(y=300, x=180)
icevar = IntVar()
ice_qty = Entry(petasco,textvariable=icevar ,font=('times', 13, 'bold'), bd=2,width=7)
ice_qty.place(y=300, x=300)

#ice_sum = 3 * int(ice_qty)
#=========================================================================================

# ====================================================================================
cheese_lbl = Label(petasco, text='Cheese', font=('times', 13, 'bold'))
cheese_lbl.place(x=20, y=340)

cheese_price = Label(text='$5', font=('times', 13, 'bold'))
cheese_price.place(y=340, x=180)
cheesevar = IntVar()
cheese_qty = Entry(petasco,textvariable=cheesevar, font=('times', 13, 'bold'), bd=2,width=7)
cheese_qty.place(y=340, x=300)

#cheese_sum = 5 * int(cheese_qty)
#=========================================================================================

# ====================================================================================
sand_lbl = Label(petasco, text='Sandwich', font=('times', 13, 'bold'))
sand_lbl.place(x=20, y=380)

sand_price = Label(text='$2.5', font=('times', 13, 'bold'))
sand_price.place(y=380, x=180)
sandvar = IntVar()
sand_qty = Entry(petasco,textvariable=sandvar, font=('times', 13, 'bold'), bd=2,width=7)
sand_qty.place(y=380, x=300)

#sand_sum = 2.5 * int(sand_qty)
#=========================================================================================

# ====================================================================================
fufu_lbl = Label(petasco, text='Fufu', font=('times', 13, 'bold'))
fufu_lbl.place(x=20, y=420)

fufu_price = Label(text='$1', font=('times', 13, 'bold'))
fufu_price.place(y=420, x=180)
futuvar = IntVar()
fufu_qty = Entry(petasco,textvariable=futuvar, font=('times', 13, 'bold'), bd=2,width=7)
fufu_qty.place(y=420, x=300)

#fufu_sum = 1 * int(fufu_qty)
#=========================================================================================



# ------------------------------ price label -------------------------------
price = Label(petasco, text='Price', font=('times', 13, 'bold'))
price.place(y=150, x=180)

# ------------------------------ qauntity label -------------------------------
qty = Label(petasco, text='Qauntity', font=('times', 13, 'bold'))
qty.place(y=150, x=300)


#---------------------------------- Drinks Menu -------------------------------------------
Fmenu_lbl = Label(petasco, text='============DRINKS MENU============', font=('times', 14, 'bold'))
Fmenu_lbl.place(y=120, x=450 )

# ------------------------------ Items label -------------------------------
items = Label(petasco, text='ITEM', font=('times', 13, 'bold'))
items.place(y=150, x=450)

# ------------------------------ price label -------------------------------
price = Label(petasco, text='Price', font=('times', 13, 'bold'))
price.place(y=150, x=620)

# ------------------------------ qauntity label -------------------------------
qty = Label(petasco, text='Qauntity', font=('times', 13, 'bold'))
qty.place(y=150, x=750)

# ====================================================================================
coke_lbl = Label(petasco, text='Coke', font=('times', 13, 'bold'))
coke_lbl.place(x=450, y=190)

coke_price = Label(text='Ghs 5', font=('times', 13, 'bold'))
coke_price.place(y=190, x=620)
cokevar = IntVar()
coke_qty = Entry(petasco, textvariable=cokevar,font=('times', 13, 'bold'), bd=2,width=7)
coke_qty.place(y=190, x=750)
coke = 5 * cokevar.get()
#=========================================================================================

# ========================================================================================
pepsi_lbl = Label(petasco, text='Pepsi', font=('times', 13, 'bold'))
pepsi_lbl.place(x=450, y=230)

pepsi_price = Label(text='Ghs 5', font=('times', 13, 'bold'))
pepsi_price.place(y=230, x=620)
pepsivar = IntVar()
pepsi_qty = Entry(petasco,textvariable=pepsivar, font=('times', 13, 'bold'), bd=2,width=7)
pepsi_qty.place(y=230, x=750)
pepsi = 5 * pepsivar.get()
#=========================================================================================

# ========================================================================================
cola_lbl = Label(petasco, text='Coka Cola', font=('times', 13, 'bold'))
cola_lbl.place(x=450, y=270)

cola_price = Label(text='Ghs 5', font=('times', 13, 'bold'))
cola_price.place(y=270, x=620)
colavar = IntVar()
cola_qty = Entry(petasco,textvariable=colavar, font=('times', 13, 'bold'), bd=2,width=7)
cola_qty.place(y=270, x=750)
cola = 5 * colavar.get()
#=========================================================================================

# ========================================================================================
dew_lbl = Label(petasco, text='Dew', font=('times', 13, 'bold'))
dew_lbl.place(x=450, y=300)

dew_price = Label(text='Ghs 5', font=('times', 13, 'bold'))
dew_price.place(y=300, x=620)
dewvar = IntVar()
dew_qty = Entry(petasco,textvariable=dewvar, font=('times', 13, 'bold'), bd=2,width=7)
dew_qty.place(y=300, x=750)
dew = 5 * dewvar.get()
#=========================================================================================

# =================================== payment ============================================

payment = Entry(petasco, font=('times', 15, 'bold'), bd=2,width=36, bg='blue')
payment.place(x= 450, y=570, height=6)

payment_lbl = Label(petasco, text='Make Payment', font=('times', 15, 'bold'))
payment_lbl.place(x=565,y=580)
paymentMethod = Label(petasco, text='Mobile Money\n Name:  DIYOUH PETER  No: 0547736844', font=('times', 13, 'bold'), fg='blue')
paymentMethod.place(x=460, y=620)

# ======================================== Drinks Total ===================================

def drinkmenu():
    global drinkTotal
    drinkTotal = ((cokevar.get() * 5) + (pepsivar.get()*5) + (colavar.get()*5) + (dewvar.get()*5)) / 10
    drklbl.config(text='Total $ ' + str(drinkTotal))

drinktotal = Button(petasco, text='Total',command=drinkmenu, font=('times', 15, 'bold'), bd=5, width=7)
drinktotal.place(x=480, y=350)

drklbl = Label(petasco,font=('times', 15, 'bold') )
drklbl.place(x=650, y=370)
drinkmenu()

#---------------------------------- Invoice  -------------------------------------------
Fmenu_lbl = Label(petasco, text='============INVOICE============', font=('times', 14, 'bold'))
Fmenu_lbl.place(y=120, x=890 )

invoice_entry = Entry(petasco,font=('times', 13, 'bold'), bd=2,width=40 )
invoice_entry.place(y=150, x=890, height=470)

print_btn = Button(petasco, text='Print',font=('times', 15, 'bold'), bd=5, width=7)
print_btn.place(x=920, y=628)

save_btn = Button(petasco, text='Save',font=('times', 15, 'bold'), bd=5, width=7)
save_btn.place(x=1100, y=628)




# --------------------------------------------------- Total Button ----------------------------------------
def Total():
    global total
    total = (chickenVar.get() * 5) + (pizzaVar.get() * 10) + (friesvar.get()*1.5) + (icevar.get()*3) + (cheesevar.get()*5) + (sandvar.get()*2.5) + (futuvar.get()*1)
    totaloutput.config(text='Total $' + str(total))
    return total



btn = Button(petasco, text='Total',command=Total, font=('times', 15, 'bold'), bd=5, width=10)
btn.place(x=50, y=480)

totaloutput = Label(petasco, font=('times', 15, 'bold') )
totaloutput.place(x= 230, y=490)
Total()


def gross():
    grossTotal = int(total) + int(drinkTotal)
    grosslbl.config(text='$ ' + str(grossTotal))


grossbtn = Button(petasco, text='Gross Total',command=gross, font=('times', 15, 'bold'), bd=5, width=10)
grossbtn.place(x=50, y=580)

grosslbl = Label(petasco, font=('times', 15, 'bold'))
grosslbl.place(x=230, y=580)
gross()

# ================================================ Invoice Print Out =========================================================
'''def recipt():
    invoice_entry.get(customerName_var)
    name = customerlbl.config('CUSTOMER NAME: '+ str(customerName_var.get()))
    phone = customerPhone.config('PHONE: ' + str(customerPhone_var.get()))
    bill = bill_entry.config('Bill No: ' + str(customerBill_var.get()))'''


confirmQ = Label(petasco, text='Made Payment?', font=('Arial',12, 'bold'), fg='red')
confirmQ.place(x=495, y=665)
confirmbtn = Button(petasco,text='Confirm', font=('times', 15, 'bold'), bd=5, width=7, bg='red')
confirmbtn.place(x=640, y=665, height=35)


petasco.resizable(False, False)
petasco.mainloop()