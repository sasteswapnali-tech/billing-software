from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time
import random


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        #VARIABLES
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()


        # Product Categories list
        self.Category = ["Select Option", "Groceries", "Electronics", "Clothing", "Home & Kitchen", "Beauty & Personal Care"]

        # SubCatGroceries
        self.SubCatGroceries = ["Rice & Grains", "Snacks", "Beverages", "Dairy Products"]

        self.RiceGrains = ["India Gate Basmati", "Daawat", "Fortune Sona Masoori"]
        self.price_IndiaGate = 1200
        self.price_Daawat = 1000
        self.price_Fortune = 950

        self.Snacks = ["Lays", "Kurkure", "Bingo"]
        self.price_Lays = 20
        self.price_Kurkure = 25
        self.price_Bingo = 30

        self.Beverages = ["Coca Cola", "Pepsi", "Frooti"]
        self.price_CocaCola = 40
        self.price_Pepsi = 35
        self.price_Frooti = 30

        self.Dairy = ["Amul Butter", "Mother Dairy Milk", "Britannia Cheese"]
        self.price_Amul = 60
        self.price_MotherDairy = 50
        self.price_Britannia = 70

        # SubCatElectronics
        self.SubCatElectronics = ["Smartphones", "Laptops", "Accessories", "Headphones"]

        self.Smartphones = ["iPhone 15", "Samsung S23", "OnePlus 12", "Redmi Note 13"]
        self.price_iPhone = 75000
        self.price_Samsung = 60000
        self.price_OnePlus = 55000
        self.price_Redmi = 18000

        self.Laptops = ["HP Pavilion", "Dell Inspiron", "Lenovo IdeaPad", "MacBook Air"]
        self.price_HP = 55000
        self.price_Dell = 60000
        self.price_Lenovo = 52000
        self.price_MacBook = 90000

        self.Accessories = ["Power Bank", "USB Cable", "Wireless Mouse"]
        self.price_PowerBank = 1200
        self.price_USBCable = 300
        self.price_Mouse = 800

        self.Headphones = ["Boat Rockerz 255", "JBL Tune 760NC", "Apple AirPods Pro"]
        self.price_BoatRockerz255 = 1499
        self.price_JBLTune760NC = 5999
        self.price_AppleAirPodsPro = 24900

        # SubCatClothing
        self.SubCatClothing = ["Men's Wear", "Women's Wear", "Footwear"]

        self.MensWear = ["Levis Jeans", "Mufti Shirt", "Spykar T-Shirt"]
        self.price_Levis = 2500
        self.price_Mufti = 1800
        self.price_Spykar = 1500

        self.WomensWear = ["Zara Dress", "H&M Top", "Only Skirt"]
        self.price_Zara = 3200
        self.price_HM = 2100
        self.price_Only = 1800

        self.Footwear = ["Nike Sneakers", "Adidas Running Shoes", "Bata Sandals"]
        self.price_Nike = 4500
        self.price_Adidas = 4000
        self.price_Bata = 1200


        # SubCatHomeKitchen
        self.SubCatHomeKitchen = ["Cookware", "Appliances", "Home Decor"]

        self.Cookware = ["Prestige Non-Stick Pan", "Hawkins Cooker", "Pigeon Kadhai"]
        self.price_Prestige = 1200
        self.price_Hawkins = 2500
        self.price_Pigeon = 1000

        self.Appliances = ["Philips Mixer", "LG Refrigerator", "Bosch Washing Machine"]
        self.price_Philips = 4800
        self.price_LG = 27000
        self.price_Bosch = 32000

        self.HomeDecor = ["Wall Clock", "Cushion Set", "Curtains"]
        self.price_Clock = 800
        self.price_Cushion = 600
        self.price_Curtains = 1500


        # SubCatBeauty
        self.SubCatBeauty = ["Skincare", "Haircare", "Perfumes", "Makeup"]

        self.Skincare = ["Nivea Cream", "Ponds Moisturizer", "Lotus Sunscreen"]
        self.price_Nivea = 180
        self.price_Ponds = 220
        self.price_Lotus = 350

        self.Haircare = ["Dove Shampoo", "Pantene Conditioner", "L’Oreal Hair Serum"]
        self.price_Dove = 250
        self.price_Pantene = 230
        self.price_LOreal = 400

        self.Perfumes = ["Fogg", "Engage", "Bella Vita"]
        self.price_Fogg = 300
        self.price_Engage = 280
        self.price_Bella = 450

        self.Makeup = ["Foundation", "Mascara", "Lipstick", "Concealer", "Blush", "Powder"]
        self.price_Foundation = 1300
        self.price_Mascara = 900
        self.price_Lipstick = 600
        self.price_Concealer = 600
        self.price_Blush = 700
        self.price_Powder = 799
        



        #IMAGE 1
        img = Image.open("images/b1.jpg")
        img = img.resize((550,130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_img = Label(self.root, image=self.photoimg)
        lbl_img.place(x=0, y=0, width=500, height=130)


        #IMAGE 2
        img1 = Image.open("images/girls.jpg")
        img1 = img1.resize((550,130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl_img1 = Label(self.root, image=self.photoimg1)
        lbl_img1.place(x=500, y=0, width=500, height=130)


        #IMAGE 3
        img2 = Image.open("images/girl1.jpg")
        img2 = img2.resize((550,130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_img2 = Label(self.root, image=self.photoimg2)
        lbl_img2.place(x=1000, y=0, width=500, height=130)


        lbl_title = Label(self.root, text="🧾 SuperMart Billing Software", font=("Segoe UI", 35, "bold"), bg="white", fg="red")
        lbl_title.place(x=0, y=130, width=1230, height=45)

        #CLOCK LABEL
        self.clock_lbl = Label(self.root, font=("times", 20), bg="white")
        self.clock_lbl.place(x=1230, y=130, width=300, height=45)

        self.update_clock()

        #MAIN FRAME
        Main_frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        Main_frame.place(x=0, y=175, width=1530, height=620)


        #CUSTOMER FRAME
        cust_Frame = LabelFrame(Main_frame, text="Custmore", font=("Segoe UI", 12, "bold"), bg="white", fg="red")
        cust_Frame.place(x=10, y=5, width=350, height=140)

        self.lbl_mob = Label(cust_Frame, text="Mobile No:", font=("Segoe UI", 12), bg="white")       
        self.lbl_mob.grid(row=0, column=0, sticky=W, padx=5, pady=2)      

        self.entry_mob = Entry(cust_Frame, textvariable=self.c_phone, font=("Segoe UI", 10), width=24)
        self.entry_mob.grid(row=0, column=1)

        self.lbl_CustName = Label(cust_Frame, text="Customer Name:", font=("Segoe UI", 12), bg="white", bd=4)       
        self.lbl_CustName.grid(row=1, column=0, sticky=W, padx=5, pady=2)      

        self.txtCustName = Entry(cust_Frame, textvariable=self.c_name, font=("Segoe UI", 10), width=24)
        self.txtCustName.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lblEmail = Label(cust_Frame, text="Email:", font=("Segoe UI", 12), bg="white", bd=4)       
        self.lblEmail.grid(row=2, column=0, sticky=W, padx=5, pady=2)      

        self.txtEmail = Entry(cust_Frame, textvariable=self.c_email,font=("Segoe UI", 10), width=24)
        self.txtEmail.grid(row=2, column=1, sticky=W, padx=5, pady=2)



        #PRODUCT FRAME
        prod_Frame = LabelFrame(Main_frame, text="Product", font=("Segoe UI", 12, "bold"), bg="white", fg="red")
        prod_Frame.place(x=366, y=5, width=720, height=140)


        #CATEGORY
        self.lblCategory = Label(prod_Frame, text="Select category:", font=("Segoe UI", 12), bg="white", bd=4)       
        self.lblCategory.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.combo_Category = ttk.Combobox(prod_Frame, value=self.Category, font=("Segoe UI", 12), width=24, state="readonly")
        self.combo_Category.current(0)
        self.combo_Category.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.combo_Category.bind("<<ComboboxSelected>>", self.Categories)

        #SUB CATEGORY
        self.lblSubCategory = Label(prod_Frame, text="Sub category:", font=("Segoe UI", 12), bg="white", bd=4)       
        self.lblSubCategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.combo_SubCategory = ttk.Combobox(prod_Frame, value=[""], font=("Segoe UI", 12), width=24, state="readonly")
        self.combo_SubCategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.combo_SubCategory.bind("<<ComboboxSelected>>", self.Product_add)

        #PRODUCT NAME
        self.lblproduct = Label(prod_Frame, text="Product Name:", font=("Segoe UI", 12), bg="white", bd=4)       
        self.lblproduct.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.combo_Product = ttk.Combobox(prod_Frame, textvariable=self.product,font=("Segoe UI", 12), width=24, state="readonly")
        self.combo_Product.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.combo_Product.bind("<<ComboboxSelected>>", self.price)

        #PRICE
        self.lblPrice = Label(prod_Frame, text="Price:", font=("Segoe UI", 12), bg="white", bd=4)       
        self.lblPrice.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.combo_Price = ttk.Combobox(prod_Frame, textvariable=self.prices, font=("Segoe UI", 12), width=24, state="readonly")
        self.combo_Price.grid(row=0, column=3, sticky=W, padx=5, pady=2)
        

        #QTY
        self.lblQty = Label(prod_Frame, text="Qty:", font=("Segoe UI", 12), bg="white", bd=4)       
        self.lblQty.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.combo_Qty = Entry(prod_Frame, textvariable=self.qty,font=("Segoe UI", 12), width=24)
        self.combo_Qty.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        #MIDDLE FRAME
        Middle_Frame = Frame(Main_frame, bd=10)
        Middle_Frame.place(x=10, y=150, width=1080, height=340)

        #IMAGE 1
        img_middle = Image.open("images/good.jpg")
        img_middle = img_middle.resize((490,340), Image.Resampling.LANCZOS)
        self.photoimg_middle = ImageTk.PhotoImage(img_middle)

        lbl_img_middle = Label(Middle_Frame, image=self.photoimg_middle)
        lbl_img_middle.place(x=0, y=0, width=500, height=340)


        #IMAGE 2
        img_middle1 = Image.open("images/mall.jpg")
        img_middle1 = img_middle1.resize((490,340), Image.Resampling.LANCZOS)
        self.photoimg_middle1 = ImageTk.PhotoImage(img_middle1)

        lbl_img_middle1 = Label(Middle_Frame, image=self.photoimg_middle1)
        lbl_img_middle1.place(x=490, y=0, width=500, height=340)


        #SEARCHING AREA
        Search_Frame = Frame(Main_frame, bd=2, bg="white")
        Search_Frame.place(x=1095, y=10, width=500, height=40)

        #SEARCH LABLE
        self.lblBill = Label(Search_Frame, text="Bill Number", font=("Segoe UI", 12, "bold"), bg="red", fg="white")       
        self.lblBill.grid(row=0, column=0, sticky=W, padx=1)

        self.Entry_Search = Entry(Search_Frame, textvariable=self.search_bill,font=("Segoe UI", 12, "bold"), width=24)
        self.Entry_Search.grid(row=0, column=1, sticky=W, padx=2)
        
        self.BtnSearch = Button(Search_Frame, text="Search", font=("Segoe UI", 10, "bold"), bg="red", fg="white", width=10, cursor="hand2")
        self.BtnSearch.grid(row=0, column=2)


        #RIGHT FRAME BILL AREA
        RightLabelFrame = LabelFrame(Main_frame, text="Bill Area", font=("Segoe UI", 12, "bold"), bg="white", fg="red")
        RightLabelFrame.place(x=1095, y=45, width=410, height=440)

        scroll_y = Scrollbar(RightLabelFrame, orient=VERTICAL)
        self.textarea = Text(RightLabelFrame, yscrollcommand=scroll_y.set, bg="white", fg="blue", font=("Segoe UI", 12, "bold"))
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)


        #BILL COUNTER
        bottom_Frame = LabelFrame(Main_frame, text="Bill Counter", font=("Segoe UI", 12, "bold"), bg="white", fg="red")
        bottom_Frame.place(x=0, y=485, width=1520, height=125)

        #SUB TOTAL
        self.lblSubTotal = Label(bottom_Frame, text="Sub Total", font=("Segoe UI", 12), bg="white", bd=4)       
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.SubTotal = Entry(bottom_Frame, textvariable=self.sub_total,font=("Segoe UI", 12), width=24)
        self.SubTotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        #TAX
        self.lblTax = Label(bottom_Frame, text="Tax", font=("Segoe UI", 12), bg="white", bd=4)       
        self.lblTax.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.Tax = Entry(bottom_Frame, textvariable=self.tax_input,font=("Segoe UI", 12), width=24)
        self.Tax.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        #AMOUNT
        self.lblAmountTotal = Label(bottom_Frame, text="Total", font=("Segoe UI", 12), bg="white", bd=4)       
        self.lblAmountTotal.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txtAmountTotal = Entry(bottom_Frame, textvariable=self.total,font=("Segoe UI", 12), width=24)
        self.txtAmountTotal.grid(row=2, column=1, sticky=W, padx=5, pady=2)


        #BUTTON FRAME
        Btn_Frame = Frame(bottom_Frame, bd=2, bg="white")
        Btn_Frame.place(x=350, y=0)

        self.BtnAddToCart = Button(Btn_Frame, height=2, text="Add To Cart", font=("Segoe UI", 10, "bold"), bg="orangered", fg="white", width=20, cursor="hand2")
        self.BtnAddToCart.grid(row=1, column=0)

        self.BtnGenrate = Button(Btn_Frame, height=2, text="Genrate Bill", font=("Segoe UI", 10, "bold"), bg="orangered", fg="white", width=20, cursor="hand2")
        self.BtnGenrate.grid(row=1, column=1)

        self.BtnSave = Button(Btn_Frame, height=2, text="Save Bill", font=("Segoe UI", 10, "bold"), bg="orangered", fg="white", width=20, cursor="hand2")
        self.BtnSave.grid(row=1, column=2)

        self.BtnPrint = Button(Btn_Frame, height=2, text="Print", font=("Segoe UI", 10, "bold"), bg="orangered", fg="white", width=20, cursor="hand2")
        self.BtnPrint.grid(row=1, column=3)

        self.BtnClear = Button(Btn_Frame, height=2, text="Clear", font=("Segoe UI", 10, "bold"), bg="orangered", fg="white", width=20, cursor="hand2")
        self.BtnClear.grid(row=1, column=4)

        self.BtnExit = Button(Btn_Frame, height=2, text="Exit", font=("Segoe UI", 10, "bold"), bg="orangered", fg="white", width=20, cursor="hand2")
        self.BtnExit.grid(row=1, column=5)


    def Categories(self, event=""):
        if self.combo_Category.get()=="Groceries":
            self.combo_SubCategory.config(value=self.SubCatGroceries)
            self.combo_SubCategory.current(0)

        if self.combo_Category.get()=="Electronics":
            self.combo_SubCategory.config(value=self.SubCatElectronics)
            self.combo_SubCategory.current(0)

        if self.combo_Category.get()=="Clothing":
            self.combo_SubCategory.config(value=self.SubCatClothing)
            self.combo_SubCategory.current(0)

        if self.combo_Category.get()=="Home & Kitchen":
            self.combo_SubCategory.config(value=self.SubCatHomeKitchen)
            self.combo_SubCategory.current(0)

        if self.combo_Category.get()=="Beauty & Personal Care":
            self.combo_SubCategory.config(value=self.SubCatBeauty)
            self.combo_SubCategory.current(0)


    def Product_add(self, event=""):
        #GROCERY LIST
        if self.combo_SubCategory.get()=="Rice & Grains":
            self.combo_Product.config(value=self.RiceGrains)
            self.combo_Product.current(0)

        if self.combo_SubCategory.get()=="Snacks":
            self.combo_Product.config(value=self.Snacks)
            self.combo_Product.current(0)

        if self.combo_SubCategory.get()=="Beverages":
            self.combo_Product.config(value=self.Beverages)
            self.combo_Product.current(0)

        if self.combo_SubCategory.get()=="Dairy Products":
            self.combo_Product.config(value=self.Dairy)
            self.combo_Product.current(0)

        #ELECTRONICS LIST
        if self.combo_SubCategory.get()=="Smartphones":
            self.combo_Product.config(value=self.Smartphones)
            self.combo_Product.current(0)

        if self.combo_SubCategory.get()=="Laptops":
            self.combo_Product.config(value=self.Laptops)
            self.combo_Product.current(0)

        if self.combo_SubCategory.get()=="Accessories":
            self.combo_Product.config(value=self.Accessories)
            self.combo_Product.current(0)

        if self.combo_SubCategory.get()=="Headphones":
            self.combo_Product.config(value=self.Headphones)
            self.combo_Product.current(0)

        #CLOTHING LIST
        if self.combo_SubCategory.get()=="Men's Wear":
            self.combo_Product.config(value=self.MensWear)
            self.combo_Product.current(0)

        if self.combo_SubCategory.get()=="Women's Wear":
            self.combo_Product.config(value=self.WomensWear)
            self.combo_Product.current(0)

        if self.combo_SubCategory.get()=="Footwear":
            self.combo_Product.config(value=self.Footwear)
            self.combo_Product.current(0)

        #HOME AND KITCHEN LIST
        if self.combo_SubCategory.get()=="Cookware":
            self.combo_Product.config(value=self.Cookware)
            self.combo_Product.current(0)

        if self.combo_SubCategory.get()=="Appliances":
            self.combo_Product.config(value=self.Appliances)
            self.combo_Product.current(0)

        if self.combo_SubCategory.get()=="Home Decor":
            self.combo_Product.config(value=self.HomeDecor)
            self.combo_Product.current(0)

        #BEAUTY AND PERSONAL CARE LIST
        if self.combo_SubCategory.get()=="Skincare":
            self.combo_Product.config(value=self.Skincare)
            self.combo_Product.current(0)

        if self.combo_SubCategory.get()=="Haircare":
            self.combo_Product.config(value=self.Haircare)
            self.combo_Product.current(0)

        if self.combo_SubCategory.get()=="Perfumes":
            self.combo_Product.config(value=self.Perfumes)
            self.combo_Product.current(0)

        if self.combo_SubCategory.get()=="Makeup":
            self.combo_Product.config(value=self.Makeup)
            self.combo_Product.current(0)


    def price(self,event=""):
        #GROCERY PRICE
        if self.combo_Product.get()=="India Gate Basmati":
            self.combo_Price.config(value=self.price_IndiaGate)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Daawat":
            self.combo_Price.config(value=self.price_Daawat)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Fortune Sona Masoori":
            self.combo_Price.config(value=self.price_Fortune)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Lays":
            self.combo_Price.config(value=self.price_Lays)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Kurkure":
            self.combo_Price.config(value=self.price_Kurkure)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Bingo":
            self.combo_Price.config(value=self.price_Bingo)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Coca Cola":
            self.combo_Price.config(value=self.price_CocaCola)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Pepsi":
            self.combo_Price.config(value=self.price_Pepsi)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Frooti":
            self.combo_Price.config(value=self.price_Frooti)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Amul Butter":
            self.combo_Price.config(value=self.price_Amul)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Mother Dairy Milk":
            self.combo_Price.config(value=self.price_MotherDairy)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Britannia Cheese":
            self.combo_Price.config(value=self.price_Britannia)
            self.combo_Price.current(0)
            self.qty.set(1)

        #ELECTRONICS PRICE
        if self.combo_Product.get()=="iPhone 15":
            self.combo_Price.config(value=self.price_iPhone)
            self.combo_Price.current(0)
            self.qty.set(1)
            
        if self.combo_Product.get()=="Samsung S23":
            self.combo_Price.config(value=self.price_Samsung)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="OnePlus 12":
            self.combo_Price.config(value=self.price_OnePlus)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Redmi Note 13":
            self.combo_Price.config(value=self.price_Redmi)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="HP Pavilion":
            self.combo_Price.config(value=self.price_HP)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Dell Inspiron":
            self.combo_Price.config(value=self.price_Dell)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Lenovo IdeaPad":
            self.combo_Price.config(value=self.price_Lenovo)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="MacBook Air":
            self.combo_Price.config(value=self.price_MacBook)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Power Bank":
            self.combo_Price.config(value=self.price_PowerBank)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="USB Cable":
            self.combo_Price.config(value=self.price_USBCable)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Wireless Mouse":
            self.combo_Price.config(value=self.price_Mouse)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Boat Rockerz 255":
            self.combo_Price.config(value=self.price_BoatRockerz255)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="JBL Tune 760NC":
            self.combo_Price.config(value=self.price_JBLTune760NC)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Apple AirPods Pro":
            self.combo_Price.config(value=self.price_AppleAirPodsPro)
            self.combo_Price.current(0)
            self.qty.set(1)

        #CLOTHING PRICE
        if self.combo_Product.get()=="Levis Jeans":
            self.combo_Price.config(value=self.price_Levis)
            self.combo_Price.current(0)
            self.qty.set(1)
            
        if self.combo_Product.get()=="Mufti Shirt":
            self.combo_Price.config(value=self.price_Mufti)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Spykar T-Shirt":
            self.combo_Price.config(value=self.price_Spykar)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Zara Dress":
            self.combo_Price.config(value=self.price_Zara)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="H&M Top":
            self.combo_Price.config(value=self.price_HM)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Only Skirt":
            self.combo_Price.config(value=self.price_Only)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Nike Sneakers":
            self.combo_Price.config(value=self.price_Nike)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Adidas Running Shoes":
            self.combo_Price.config(value=self.price_Adidas)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Bata Sandals":
            self.combo_Price.config(value=self.price_Bata)
            self.combo_Price.current(0)
            self.qty.set(1)

        #HOME AND KITCHEN PRICE
        if self.combo_Product.get()=="Prestige Non-Stick Pan":
            self.combo_Price.config(value=self.price_Prestige)
            self.combo_Price.current(0)
            self.qty.set(1)
            
        if self.combo_Product.get()=="Hawkins Cooker":
            self.combo_Price.config(value=self.price_Hawkins)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Pigeon Kadhai":
            self.combo_Price.config(value=self.price_Pigeon)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Philips Mixer":
            self.combo_Price.config(value=self.price_Philips)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="LG Refrigerator":
            self.combo_Price.config(value=self.price_LG)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Bosch Washing Machine":
            self.combo_Price.config(value=self.price_Bosch)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Wall Clock":
            self.combo_Price.config(value=self.price_Clock)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Cushion Set":
            self.combo_Price.config(value=self.price_Cushion)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Curtains":
            self.combo_Price.config(value=self.price_Curtains)
            self.combo_Price.current(0)
            self.qty.set(1)

        #BEAUTY AND CARE PRICE
        if self.combo_Product.get()=="Nivea Cream":
            self.combo_Price.config(value=self.price_Nivea)
            self.combo_Price.current(0)
            self.qty.set(1)
            
        if self.combo_Product.get()=="Ponds Moisturizer":
            self.combo_Price.config(value=self.price_Ponds)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Lotus Sunscreen":
            self.combo_Price.config(value=self.price_Lotus)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Dove Shampoo":
            self.combo_Price.config(value=self.price_Dove)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Pantene Conditioner":
            self.combo_Price.config(value=self.price_Pantene)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="L’Oreal Hair Serum":
            self.combo_Price.config(value=self.price_LOreal)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Fogg":
            self.combo_Price.config(value=self.price_Fogg)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Engage":
            self.combo_Price.config(value=self.price_Engage)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Bella Vita":
            self.combo_Price.config(value=self.price_Bella)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Foundation":
            self.combo_Price.config(value=self.price_Foundation)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Mascara":
            self.combo_Price.config(value=self.price_Mascara)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Lipstick":
            self.combo_Price.config(value=self.price_Lipstick)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Concealer":
            self.combo_Price.config(value=self.price_Concealer)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Blush":
            self.combo_Price.config(value=self.price_Blush)
            self.combo_Price.current(0)
            self.qty.set(1)

        if self.combo_Product.get()=="Powder":
            self.combo_Price.config(value=self.price_Powder)
            self.combo_Price.current(0)
            self.qty.set(1)


    #CLOCK FUNCTION
    def update_clock(self):
        current_time = time.strftime("%H:%M:%S %p")
        self.clock_lbl.config(text=current_time)
        self.root.after(1000, self.update_clock)


if __name__ == '__main__':
    root=Tk()
    obj = Bill_App(root)
    root.mainloop()
