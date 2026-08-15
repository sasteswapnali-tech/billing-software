# 🧾 SuperMart Billing Software

A desktop-based **Billing Software** developed using **Python and Tkinter**. The application provides a graphical interface for managing customer information, selecting products by category and subcategory, automatically displaying product prices, entering quantities, and preparing bills.

## 📌 Project Overview

**SuperMart Billing Software** is a Python GUI application designed to simulate a supermarket billing system.

The application allows users to:

* Enter customer details
* Select product categories
* Select product subcategories
* Select products
* Automatically display product prices
* Enter product quantity
* Generate a unique bill number
* View a billing area
* Display a real-time clock
* Work with multiple supermarket product categories

The project demonstrates the use of **Python Object-Oriented Programming, Tkinter GUI development, event handling, and image processing with Pillow**.

## ✨ Features

* 🧾 Customer information management
* 📱 Customer mobile number input
* 👤 Customer name input
* 📧 Customer email input
* 🔢 Automatic bill number generation
* 🛒 Multiple product categories
* 📦 Product subcategory selection
* 💰 Automatic product price selection
* 🔢 Quantity input
* 🕐 Real-time digital clock
* 🖥️ Desktop GUI interface
* 🖼️ Image-based user interface
* 📜 Billing area with scrollbar
* 🎨 User-friendly Tkinter interface

## 🛍️ Product Categories

The application currently contains the following categories:

### 1. Groceries

* Rice & Grains
* Snacks
* Beverages
* Dairy Products

### 2. Electronics

* Smartphones
* Laptops
* Accessories
* Headphones

### 3. Clothing

* Men's Wear
* Women's Wear
* Footwear

### 4. Home & Kitchen

* Cookware
* Appliances
* Home Decor

### 5. Beauty & Personal Care

* Skincare
* Haircare
* Perfumes
* Makeup

## 🛠️ Technologies Used

| Technology   | Purpose                          |
| ------------ | -------------------------------- |
| Python       | Core programming language        |
| Tkinter      | GUI development                  |
| ttk          | Styled GUI widgets               |
| Pillow (PIL) | Image loading and processing     |
| OOP          | Application structure            |
| Random       | Automatic bill number generation |
| Time         | Real-time clock                  |

## 📂 Project Structure

```text
supermart-billing-software/
│
├── images/
│   ├── b1.jpg
│   ├── girls.jpg
│   ├── girl1.jpg
│   ├── good.jpg
│   └── mall.jpg
│
├── billing_software.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Requirements

Before running the project, make sure you have:

* Python 3.x
* Pillow

Tkinter is generally included with the standard Python installation on Windows.

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/supermart-billing-software.git
```

### 2. Navigate to the project directory

```bash
cd supermart-billing-software
```

### 3. Install required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python billing_software.py
```

## 🖥️ How to Use

### Step 1: Enter Customer Details

Enter:

* Mobile Number
* Customer Name
* Email

### Step 2: Select Product Category

Choose a category such as:

```text
Groceries
Electronics
Clothing
Home & Kitchen
Beauty & Personal Care
```

### Step 3: Select Subcategory

After selecting a category, the corresponding subcategories are displayed automatically.

### Step 4: Select Product

Select the required product from the product dropdown.

### Step 5: View Price

The application automatically displays the price of the selected product.

### Step 6: Enter Quantity

Enter the required product quantity.

### Step 7: Prepare the Bill

The billing interface provides an area where billing information can be displayed and managed.

## 🧠 Concepts Demonstrated

This project demonstrates several important Python programming concepts:

* Object-Oriented Programming
* Classes and objects
* Tkinter GUI programming
* Event-driven programming
* Variables using `StringVar` and `IntVar`
* Combobox widgets
* Frames and LabelFrames
* Grid and Place geometry managers
* Image handling with Pillow
* Callback functions
* Dynamic dropdown values
* Random number generation
* Real-time GUI updates using `after()`

## 📸 Screenshots

Add screenshots of your application here after uploading them to GitHub.

Example:

```markdown
![SuperMart Billing Software](screenshots/home-screen.png)
```

You can create a `screenshots` folder and add your application screenshots there.

## 🔮 Future Improvements

The following features can be added in future versions:

* [ ] Add To Cart functionality
* [ ] Automatic subtotal calculation
* [ ] Tax/GST calculation
* [ ] Automatic total calculation
* [ ] Generate complete invoices
* [ ] Save bills to files
* [ ] Search previous bills
* [ ] Print bills
* [ ] Clear billing data
* [ ] Exit confirmation
* [ ] MySQL database integration
* [ ] Product inventory management
* [ ] Stock management
* [ ] User login system
* [ ] Sales history
* [ ] Customer database
* [ ] PDF invoice generation

## 🎯 Learning Purpose

This project was developed as a **Python desktop application project** to practice GUI development, Object-Oriented Programming, event handling, and dynamic user interfaces using Tkinter.

## 👨‍💻 Author

**Swapnali Saste**

MCA Student | Java Full Stack Developer | Software Development Enthusiast

---

⭐ If you find this project useful, consider giving the repository a star!
