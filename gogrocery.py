from tkinter import*
from string import ascii_uppercase
from tkinter import*
from tkinter.font import BOLD
#from tkinter.tix import IMAGETEXT
import random
root = Tk()
root.title("Grocery")
root.iconbitmap('C:/Users/evtam/OneDrive/Pictures/cart_icon.ico')
#root.maxsize()
root.geometry('600x500+700+400')
space = (f' '*43)

################################################# CREATE AND PUT ON SCREEN *** BUTTONS *** #################################################3
yourcart = Label(root, text=" your cart: ", borderwidth= 5, width=7, height = 1,font = ('Arial', 10),fg = 'black')#,fg="brown",bg="yellow",activebackground="#F3E5AB")
yourcart.grid(row=2, column=18)

quantLabel = Label(root, text=" quantity: ", borderwidth= 5, width=7, height = 1,font = ('Arial', 10), fg = 'black')#,fg="brown",bg="yellow",activebackground="#F3E5AB")
quantLabel.grid(row=2, column=13)


menuLabel = Label(root, text="   M E N U   ",borderwidth = 5, width=15,height = 1,font = ('Georgia', 13),fg="White",bg="Grey",activebackground="#F3E5AB")
menuLabel.grid(row=0, column=0)




#################################################### CREATE ALL LABELS ################################################################################ 
#******************* FRUIT SECTION
fruitsLabel = Label(root, text=" Fruits",borderwidth = 5, width=15,height = 1,font = ('Georgia', 13,), fg="#8B0000",bg="white",activebackground="#F3E5AB")
fruitsLabel.grid(row=2, column=0)

grapesLabel = Label(root, text="Grapes",borderwidth = 4, width=15,height = 1,font = ('Georgia', 13),fg="#FFFFFF",bg="#663046",activebackground="#F3E5AB")
grapesLabel.grid(row=3, column=0)

orangesLabel = Label(root, text="Oranges",borderwidth = 4, width=15,height = 1,font = ('Georgia', 13),fg="#FFFFFF",bg="#FBBF77",activebackground="#F3E5AB")
orangesLabel.grid(row=4, column=0)

applesLabel = Label(root, text="Apples",borderwidth = 4, width=15,height = 1,font = ('Georgia', 13),fg="#FFFFFF",bg="#8B0000",activebackground="#F3E5AB")
applesLabel.grid(row=5, column=0)

kiwisLabel = Label(root, text="Kiwis",borderwidth = 4, width=15,height = 1,font = ('Georgia', 13),fg="#FFFFFF",bg="#D2B48C",activebackground="#F3E5AB")
kiwisLabel.grid(row=6, column=0)

#**************** MEAT SECTION 
meatsLabel = Label(root, text=" Meats",borderwidth = 4, width=15,height = 1,font = ('Georgia', 13), fg="#483B2D",bg="white",activebackground="#F3E5AB")
meatsLabel.grid(row=7, column=0)

chickenLabel = Label(root, text="Chicken",borderwidth = 4, width=15,height = 1,font = ('Georgia', 13),fg="#FFFFFF",bg="brown",activebackground="#F3E5AB")
chickenLabel.grid(row=8, column=0)

beefLabel = Label(root, text="Beef",borderwidth = 4, width=15,height = 1,font = ('Georgia', 13),fg="#FFFFFF",bg="#483B2D",activebackground="#F3E5AB")
beefLabel.grid(row=9, column=0)

turkeyLabel = Label(root, text="Turkey",borderwidth = 4, width=15,height = 1,font = ('Georgia', 13),fg="#FFFFFF",bg="#988558",activebackground="#F3E5AB")
turkeyLabel.grid(row=10, column=0)

#************* VEGETABLE SECTION 
veggiesLabel = Label(root, text=" Vegetables",borderwidth = 4, width=15,height = 1,font = ('Georgia', 13), fg="#014421",bg="white",activebackground="#F3E5AB")
veggiesLabel.grid(row=11, column=0)

greenbeansLabel = Label(root, text="Green beans",borderwidth = 4, width=15,height = 1,font = ('Georgia', 13),fg="#FFFFFF",bg="green",activebackground="#F3E5AB")
greenbeansLabel.grid(row=12, column=0)

carrotsLabel = Label(root, text="Carrots",borderwidth = 4, width=15,height = 1,font = ('Georgia', 13),fg="#FFFFFF",bg="#ED9121",activebackground="#F3E5AB")
carrotsLabel.grid(row=13, column=0)

potatoesLabel = Label(root, text="Potatoes",borderwidth = 4, width=15,height = 1,font = ('Georgia', 13),fg="#FFFFFF",bg="#996515",activebackground="#F3E5AB")
potatoesLabel.grid(row=14, column=0)

########################################################## PRICE LABEL FOR EACH ITEM ##################################################################################3
pricingLabel = Label(root, text="price: ",borderwidth = 7, width=15,height = 1,font = ('Arial', 9),fg="black",bg="white",activebackground="#F3E5AB")
pricingLabel.grid(row=2, column = 1)


grapespriceLabel =Label(root, text="($2.09/lbs)",borderwidth = 7, width=15,height = 1,font = ('Arial', 9),fg="black",bg="white",activebackground="#F3E5AB")
grapespriceLabel.grid(row=3, column = 1)

orangespriceLabel= Label(root, text="($1.45/lbs)",borderwidth = 7, width=15,height = 1,font = ('Arial', 9),fg="black",bg="white",activebackground="#F3E5AB")
orangespriceLabel.grid(row=4, column = 1)

applespriceLabel= Label(root, text="($1.32/lbs)",borderwidth = 7, width=15,height = 1,font = ('Arial', 9),fg="black",bg="white",activebackground="#F3E5AB")
applespriceLabel.grid(row=5, column = 1)

kiwispriceLabel= Label(root, text="($1.08/lbs)",borderwidth = 7, width=15,height = 1,font = ('Arial', 9),fg="black",bg="white",activebackground="#F3E5AB")
kiwispriceLabel.grid(row=6, column = 1)

chickenpriceLabel= Label(root, text="($3.67/lnb)",borderwidth = 7, width=15,height = 1,font = ('Arial', 9),fg="black",bg="white",activebackground="#F3E5AB")
chickenpriceLabel.grid(row=8, column = 1)

beefpriceLabel= Label(root, text="($5.85/lbs)",borderwidth = 7, width=15,height = 1,font = ('Arial', 9),fg="black",bg="white",activebackground="#F3E5AB")
beefpriceLabel.grid(row=9, column = 1)

turkeypriceLabel= Label(root, text="($4.75/lbs)",borderwidth = 7, width=15,height = 1,font = ('Arial', 9),fg="black",bg="white",activebackground="#F3E5AB")
turkeypriceLabel.grid(row=10, column = 1)

greenbeanspriceLabel= Label(root, text="($1.10/lbs)",borderwidth = 7, width=15,height = 1,font = ('Arial', 9),fg="black",bg="white",activebackground="#F3E5AB")
greenbeanspriceLabel.grid(row=12, column = 1)

carrotspriceLabel= Label(root, text="($1.06/lbs)",borderwidth = 7, width=15,height = 1,font = ('Arial', 9),fg="black",bg="white",activebackground="#F3E5AB")
carrotspriceLabel.grid(row=13, column = 1)

potatoespriceLabel= Label(root, text="($1.80/lbs)",borderwidth = 7, width=15,height = 1,font = ('Arial', 9),fg="black",bg="white",activebackground="#F3E5AB")
potatoespriceLabel.grid(row=14, column = 1)


####################################################### FRUITS SELECTION SECTION ##################################################################

# GRAPES QUANTITY SELECTION: 

def showgrapes():
    glabel.config( text = gclicked.get() )
  
# Dropdown menu options
options = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"
]
  
# datatype of menu text
gclicked = StringVar()
g = (gclicked.get())
# SET initial menu text TO "_"
gclicked.set( "_" )

# Create Dropdown menu
gdrop = OptionMenu( root , gclicked , *options)
gdrop.grid(row=3, column = 13)

# Create button, it will change label text
gquantity = Button( root , text = "add to cart", command = showgrapes ).grid(row=3, column = 16)

glabel = Label( root , text = "__", font = ('Arial', 9), borderwidth = 4, width=15,height = 1, bg = 'white')
glabel.grid(row = 3, column = 18)


#ORANGES QUANTITY SELECTION:
def showoranges():
    olabel.config( text = oclicked.get() )
  
# Dropdown menu options
options = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"
]
  
# datatype of menu text
oclicked = StringVar()
o = (oclicked.get())


# SET initial menu text TO "_"
oclicked.set( "_" )
  
# Create Dropdown menu
odrop = OptionMenu( root , oclicked , *options )
odrop.grid(row=4, column = 13)
  
# Create button, it will change label text
oquantity = Button( root , text = "add to cart", command = showoranges ).grid(row=4, column = 16)

olabel = Label( root , text = "__", font = ('Arial', 9),borderwidth = 4, width=15,height = 1,bg = 'white')
olabel.grid(row = 4, column = 18)

#NOTES ON FORMATTING, CREATING LABELS AND PUTTING THEM ON SCREEN **************
# Create Label
#label = Label( root , text = "__" ) 
#label.pack()
#*****************************************************


# APPLES QUANTITY SELECTION:
def showapples():
    alabel.config( text = aclicked.get() )
  
# Dropdown menu options
options = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"
]
  
# datatype of menu text
aclicked = StringVar()
a = (aclicked.get())

# SET inital menu text TO "_"
aclicked.set( "_" )
  
# Create Dropdown menu
adrop = OptionMenu( root , aclicked , *options )
adrop.grid(row=5, column = 13)
  
# Create button, it will change label text
aquantity = Button( root , text = "add to cart", command = showapples ).grid(row=5, column = 16)

alabel = Label( root , text = "__", font= ('Arial', 9),borderwidth = 4, width=15,height = 1,bg = 'white')
alabel.grid(row = 5, column = 18)


#KIWIS QUANTITY SELECTION:
def showkiwis():
    klabel.config( text = kclicked.get() )
  
# Dropdown menu options
options = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"
]
  
# datatype of menu text
kclicked = StringVar() 
k = (kclicked.get())

# SET initial menu text TO "_"
kclicked.set( "_" )
  
# Create Dropdown menu
kdrop = OptionMenu( root , kclicked , *options )
kdrop.grid(row=6, column = 13)
  
# Create button, it will change label text
kquantity = Button( root , text = "add to cart", command = showkiwis ).grid(row=6, column = 16)

klabel = Label( root , text = "__", font= ('Arial', 9),borderwidth = 4, width=15,height = 1,bg = 'white')
klabel.grid(row = 6, column = 18)

################################################## MEATS SECTION ################################################

#CHICKEN QUANTITY SELECTION:
def showchicken():
    chlabel.config( text = chclicked.get() )
  
# Dropdown menu options
options = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"
]
  
# datatype of menu text
chclicked = StringVar()
ch = (chclicked.get())
# SET initial menu text TO "_"
chclicked.set( "_" )
  
# Create Dropdown menu
chdrop = OptionMenu( root , chclicked , *options )
chdrop.grid(row=8, column = 13)
  
# Create button, it will change label text
chquantity = Button( root , text = "add to cart", command = showchicken ).grid(row=8, column = 16)

chlabel = Label( root , text = "__", font = ('Arial', 9),borderwidth = 4, width=15,height = 1,bg = 'white')
chlabel.grid(row = 8, column = 18)

#BEEF QUANTITY SELECTION:
def showbeef():
    blabel.config( text = bclicked.get() )
  
# Dropdown menu options
options = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"
]
  
# datatype of menu text
bclicked = StringVar()
b = (bclicked.get())
# SET initial menu text TO "_"
bclicked.set( "_" )
  
# Create Dropdown menu
bdrop = OptionMenu( root , bclicked , *options )
bdrop.grid(row=9, column = 13)
  
# Create button, it will change label text
bquantity = Button( root , text = "add to cart", command = showbeef ).grid(row=9, column = 16)

blabel = Label( root , text = "__", font = ('Arial', 9),borderwidth = 4, width=15,height = 1, bg = 'white')
blabel.grid(row = 9, column = 18)



#TURKEY QUANTITY SELECTION:
def showturkey():
    tlabel.config( text = tclicked.get() )
  
# Dropdown menu options
options = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"
]
  
# datatype of menu text
tclicked = StringVar()
t = (tclicked.get())
# initial menu text
tclicked.set( "_" )
  
# Create Dropdown menu
tdrop = OptionMenu( root , tclicked , *options )
tdrop.grid(row=10, column = 13)
  
# Create button, it will change label text
tquantity = Button( root , text = "add to cart", command = showturkey ).grid(row=10, column = 16)

tlabel = Label( root , text = "__", font = ('Arial', 9),borderwidth = 4, width=15,height = 1, bg = 'white')
tlabel.grid(row = 10, column = 18)



############################################### VEGETABLES SECION ##########################################################################3

#GREEN BEANS QUANTITY SELECTION:
def showgreenbeans():
    gblabel.config( text = gbclicked.get() )
  
# Dropdown menu options
options = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"
]
  
# datatype of menu text
gbclicked = StringVar()
gb = (gbclicked.get())
# initial menu text
gbclicked.set( "_" )
  
# Create Dropdown menu
gbdrop = OptionMenu( root , gbclicked , *options )
gbdrop.grid(row=12, column = 13)
  
# Create button, it will change label text
gbquantity = Button( root , text = "add to cart", command = showgreenbeans ).grid(row=12, column = 16)

gblabel = Label( root , text = "__", font = ('Arial', 9),borderwidth = 4, width=15,height = 1, bg = 'white')
gblabel.grid(row = 12, column = 18)

#############################################
#CARROTS QUANTITY SELECTION:
def showcarrots():
    clabel.config( text = cclicked.get() )
  
# Dropdown menu options
options = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"
]
  
# datatype of menu text
cclicked = StringVar()
c = (cclicked.get())
# initial menu text
cclicked.set( "_" )
  
# Create Dropdown menu
cdrop = OptionMenu( root , cclicked , *options )
cdrop.grid(row=13, column = 13)
  
# Create button, it will change label text
cquantity = Button( root , text = "add to cart", command = showcarrots ).grid(row=13, column = 16)

clabel = Label( root , text = "__", font = ('Arial', 9),borderwidth = 4, width=15,height = 1, bg = 'white')
clabel.grid(row = 13, column = 18)

#POTATOES QUANTITY SELECTION:
def showpotatoes():
    plabel.config( text = (pclicked.get() ))
  
# Dropdown menu options
options = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"
]
# datatype of menu text
pclicked = StringVar()
p = (pclicked.get())

#p = int(pclicked)
# initial menu text
pclicked.set( "_" )
  
# Create Dropdown menu
pdrop = OptionMenu( root , pclicked , *options )
pdrop.grid(row=14, column = 13)
  
# Create button, it will change label text
pquantity = Button( root , text = "add to cart", command = showpotatoes ).grid(row=14, column = 16)

plabel = Label( root , text = "__", font = ('Arial', 9),borderwidth = 4, width=15,height = 1, bg = 'white')
plabel.grid(row = 14, column = 18)

#################################################### NUMBER TOTALLLLLL  ######################################################################


############################################################  NEW WINDOW  ########################################################################3

def newwindow():
    newwindow = Tk()
    newwindow.geometry('600x500+700+400')
    
    newwindow.title("Shipping / Personal Information: ")
    Label(newwindow,
            text = "").place(relx=.5, rely=0)
    backbutton = Button(newwindow, text = " back ", font = ('Arial', 10), command = newwindow.destroy, width= 19, fg="#FFFFFF", bg="brown")
    backbutton.grid(row=0, column=0)
    ############################################# LABELS FOR THE ENTRY BOXES ##############################################################################################    
    first_name = Label(newwindow, text=" First Name: ", borderwidth= 10, width=10, height = 1,font = ('Georgia', 10),fg = 'black')#,fg="brown",bg="yellow",activebackground="#F3E5AB")
    first_name.grid(row=2, column=0)
    
    
    last_name = Label(newwindow, text=" Last name: ", borderwidth= 10, width=10, height = 1,font = ('Georgia', 10),fg = 'black') #,fg="brown",bg="yellow",activebackground="#F3E5AB")
    last_name.grid(row=3, column=0)
    
    email_address = Label(newwindow, text=" Email: ", borderwidth= 10, width=12, height = 1,font = ('Georgia', 10),fg = 'black')#,fg="brown","yellow",activebackground="#F3E5AB")
    email_address.grid(row=4, column=0)

    your_street_address = Label(newwindow, text=" Street Address:   ", borderwidth= 12, width=9, height = 1,font = ('Georgia', 10),fg = 'black')#,fg="brown",bg="yellow",activebackground="#F3E5AB")
    your_street_address.grid(row=5, column=0)

    your_city = Label(newwindow, text=" City: ", borderwidth= 10, width=12, height = 1,font = ('Georgia', 10),fg = 'black')#,fg="brown",bg="yellow",activebackground="#F3E5AB")
    your_city.grid(row=6, column=0)

    your_state = Label(newwindow, text=" State: ", borderwidth= 10, width=12, height = 1,font = ('Georgia', 10),fg = 'black')#,fg="brown",bg="yellow",activebackground="#F3E5AB")
    your_state.grid(row=7, column=0)

    your_zipcode = Label(newwindow, text=" ZIP: ", borderwidth= 10, width=12, height = 1,font = ('Georgia', 10),fg = 'black')#,fg="brown",bg="yellow",activebackground="#F3E5AB")
    your_zipcode.grid(row=8, column=0)

    your_phonenumber = Label(newwindow, text=" Phone number: ", borderwidth= 12, width=9, height = 1,font = ('Georgia', 10),fg = 'black')#,fg="brown",bg="yellow",activebackground="#F3E5AB")
    your_phonenumber.grid(row=9, column=0)

    personalinfo_label = Label(newwindow, text=" Personal Information: ", borderwidth= 12, width=18, height = 1,font = ('Georgia', 10),fg = 'black', bg="white")#,fg="brown",bg="yellow",activebackground="#F3E5AB")
    personalinfo_label.grid(row=1, column = 0)

############################################################ NEW WINDOW (2) ################################################################33
    def newwindow_two():
        newwindow_two = Tk()
        newwindow_two.geometry('600x500+700+400')
    
        newwindow_two.title("Shipping Information")
        Label(newwindow_two,
            text = "").place(relx=.5, rely=0)
               
        cancel_order_button = Button(newwindow_two, text = " back ", font = ('Arial', 10), command = newwindow_two.destroy, width= 19, fg="#FFFFFF", bg="brown")
        cancel_order_button.grid(row=0, column=1)
        
        shippinginfoLabel = Label(newwindow_two, text = 'Shipping/Contact Information', font = 'Georgia',bg = 'white', padx=15, pady=10)
        shippinginfoLabel.grid(row = 1, column= 3)
    # FULL NAME LABEL 
        lname = (enter_last_name.get())
        fname = (enter_first_name.get())
        fullname = (f'{fname} {lname}')
        firstnameLabel = Label(newwindow_two, text=fullname, font = ('Georgia', 14, 'underline'), padx=15, pady=10)
        firstnameLabel.grid(row = 2, column= 3)
    #contact information 

        email = (enter_email_address.get())
        phonenumber = (enter_phonenumber.get())
        emailinfo = (f'Email: {email}') 
        emailLabel = Label(newwindow_two, text = emailinfo, padx = 15, pady = 10)
        emailLabel.grid(row = 3, column = 3)

        phonenumberinfo = (f'Phone Number: {phonenumber}')
        phonenumberLabel = Label(newwindow_two, text= phonenumberinfo, padx=15, pady=10)
        phonenumberLabel.grid(row = 4, column = 3)

        #shipping incofmation
        streetaddress=(enter_street_address.get())
        streetaddressLabel = Label(newwindow_two, text = streetaddress, padx = 15, pady = 10)
        city = (enter_city.get())
        state = (enter_state.get()) 
        zipcode = (enter_zipcode.get())
        country = (enter_country.get())
        #zip - city, IN, State. 
        zipcitystatecountry = (f'Shipping Address: {zipcode} - {city}, {state} {country}')
        zipcitystatecountryLabel = Label(newwindow_two, text=zipcitystatecountry, padx = 15, pady= 10)
        zipcitystatecountryLabel.grid(row = 5, column = 3)

        




        def newwindow_three(): 
            newwindow_three = Tk()
            newwindow_three.geometry('500x500+700+400')
            newwindow_three.title("Shipping Information")
            ################### insert image in window three ###################
            
            #newwindow_three = Canvas(newwindow_three, width=569, height=303)
            #newwindow_three.pack()

            # in the file = ' ' <<< open file properties and copy the location (open file location)
            #image = PhotoImage(file = 'C:\\Users\\evtam\\OneDrive\\Desktop\\SDEV_FINAL_PROJ\\thank_you.PNG')
            #'C:\\GUI\\thank_you.PNG')

            #newwindow_three.create_image(0,0, anchor = NW, image = image)

            

            ######################################################################
            tyconfirmation = "  Thank you for your order"
            tyconfirmationLabel= Label(newwindow_three, text =tyconfirmation, font = ('Georgia',36), padx=15, pady=10)
            tyconfirmationLabel.place(relx = .3, rely =.3)
            
            #******************** CREATE ID NUMBER******************************
            IDnum = random.randint(1,99999990)
            IDlett = random.choice(seq=ascii_uppercase)
            yourID = "  Your ORDER NUMBER: "
            yourIDLabel = Label(newwindow_three, text = yourID, font=('Georgia', 35), fg="black", padx= 15,pady=10)
            yourIDLabel.place(relx = .31,rely=.4)
            #*******************************************************************

            customerID = f'{IDlett}{IDnum}'
            customerIDLabel = Label(newwindow_three, text = customerID, font=('Arial', 35, 'underline'), fg="black", padx= 15,pady=10)
            customerIDLabel.place(relx = .4, rely = .5)

            

            
        confirmbutton = Button(newwindow_two, text = "confirm your order", font = ('Arial', 10), command = newwindow_three, padx = 15, pady=10, width = 15, fg="#FFFFFF", bg="brown")
        confirmbutton.grid(row = 6, column = 3)


    
    continuebutton = Button(newwindow, text = "continue", font = ('Arial', 10), command = newwindow_two, width= 15, fg="#FFFFFF", bg="brown")
    continuebutton.grid(row=10, column=5)




########################################### THE ENTRY BOXES : ##################################################################################################3
    
    enter_first_name=Entry(newwindow, width=15, font=('Arial',12),fg="black" ,bg="#D3D3D3", borderwidth=3)
    enter_first_name.grid(row = 2, column= 1)
    fname = (enter_first_name.get())
    enter_last_name=Entry(newwindow, width=15, font=('Arial',12),fg="black" ,bg="#D3D3D3", borderwidth=3)
    enter_last_name.grid(row = 3, column= 1)
    lname = (enter_last_name.get())
    enter_email_address=Entry(newwindow, width=15, font=('Arial',12),fg="black" ,bg="#D3D3D3", borderwidth=3)
    enter_email_address.grid(row = 4, column= 1)
    email = (enter_email_address.get())
    enter_street_address=Entry(newwindow, width=15, font=('Arial',12),fg="black" ,bg="#D3D3D3", borderwidth=3)
    enter_street_address.grid(row = 5, column= 1)
    streetaddress=(enter_street_address.get())
    enter_city=Entry(newwindow, width=15, font=('Arial',12),fg="black" ,bg="#D3D3D3", borderwidth=3)
    enter_city.grid(row = 6, column= 1)
    city = (enter_city.get())
    enter_state=Entry(newwindow, width=15, font=('Arial',12),fg="black" ,bg="#D3D3D3", borderwidth=3)
    enter_state.grid(row = 7, column= 1)
    state = (enter_state.get())
    enter_zipcode=Entry(newwindow, width=15, font=('Arial',12),fg="black" ,bg="#D3D3D3", borderwidth=3)
    enter_zipcode.grid(row = 8, column= 1)
    zipcode = (enter_zipcode.get())
    enter_phonenumber=Entry(newwindow, width=15, font=('Arial',12),fg="black" ,bg="#D3D3D3", borderwidth=3)
    enter_phonenumber.grid(row = 9, column= 1)    
    phonenumber = (enter_phonenumber.get())
    enter_country=Entry(newwindow, width=15, font=('Arial',12),fg="black" ,bg="#D3D3D3", borderwidth=3)
    enter_country.grid(row = 9, column= 1)    
    country = (enter_country.get())
#    enter_country=Entry(newwindow, width=10, font=('Georgia',10),fg="black" ,bg="#D3D3D3", borderwidth=3)
#    enter_country.grid(row = 7, column= 2)



shippingandpersonalinfobutton = Button(root, text= "continue to shipping info", width= 25, command = newwindow, fg="#FFFFFF", bg="brown")
shippingandpersonalinfobutton.grid(row=16, column=19)



root.mainloop()