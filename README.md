# Bank_FraudDetection_System
This project is a Fraud Detection Web Application built with Flask. It uses a pre-trained machine learning model (filename.pkl) to predict fraudulent transactions. The web interface allows users to input transaction data and get real-time predictions about whether a transaction is fraudulent or not.
----------------

# Fraud Detection Web Application | وب‌اپلیکیشن تشخیص تقلب

## English

### 📌 Project Overview
This project is a **Fraud Detection Web Application** built with Flask.  
It uses a pre-trained Machine Learning model (`filename.pkl`) to predict fraudulent transactions.  
The web interface allows users to input transaction data and get real-time predictions about whether a transaction is fraudulent or not.

### 🚀 Features
- Flask-based web application
- Machine Learning model integration (`.pkl` file)
- Simple and user-friendly web interface
- Real-time fraud prediction

### 📂 Project Structure
```
fraud/
│── app.py               # Main Flask application
│── filename.pkl         # Pre-trained ML model
│── j2.ipynb             # Jupyter Notebook for training and analysis
│── templates/
│   └── index.html       # Frontend HTML page
│── static/
│   └── style.css        # Styling for the web app
```

### ⚙️ Installation & Usage
1. Clone or download the project.  
2. Install required dependencies:
   ```bash
   pip install flask scikit-learn pandas numpy
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

### 📒 How it Works
1. User enters transaction details in the web interface.  
2. The data is passed to the ML model (`filename.pkl`).  
3. The model predicts if the transaction is **Fraudulent (1)** or **Legit (0)**.  
4. The result is displayed on the web page.

### 🛠 Technologies Used
- Python (Flask)
- Machine Learning (scikit-learn)
- HTML, CSS (Frontend)
- Jupyter Notebook (for training)

---

## فارسی

### 📌 معرفی پروژه
این پروژه یک **وب‌اپلیکیشن تشخیص تقلب** است که با استفاده از فریم‌ورک Flask پیاده‌سازی شده است.  
مدل یادگیری ماشین ذخیره‌شده (`filename.pkl`) برای پیش‌بینی تراکنش‌های تقلبی استفاده می‌شود.  
رابط کاربری وب به کاربران این امکان را می‌دهد که اطلاعات تراکنش را وارد کرده و پیش‌بینی بلادرنگ درباره تقلبی بودن یا نبودن تراکنش دریافت کنند.

### 🚀 ویژگی‌ها
- اپلیکیشن تحت وب با Flask  
- استفاده از مدل یادگیری ماشین از پیش آموزش‌دیده  
- رابط کاربری ساده و کاربرپسند  
- پیش‌بینی بلادرنگ تقلب  

### 📂 ساختار پروژه
```
fraud/
│── app.py               # برنامه اصلی Flask
│── filename.pkl         # مدل از پیش آموزش‌دیده
│── j2.ipynb             # نوت‌بوک برای آموزش و تحلیل داده
│── templates/
│   └── index.html       # صفحه وب اصلی
│── static/
│   └── style.css        # استایل برای رابط کاربری
```

### ⚙️ نصب و اجرا
1. پروژه را دانلود یا کلون کنید.  
2. کتابخانه‌های مورد نیاز را نصب کنید:
   ```bash
   pip install flask scikit-learn pandas numpy
   ```
3. برنامه Flask را اجرا کنید:
   ```bash
   python app.py
   ```
4. مرورگر را باز کنید و به آدرس زیر بروید:
   ```
   http://127.0.0.1:5000
   ```

### 📒 نحوه عملکرد
1. کاربر جزئیات تراکنش را در وب‌اپ وارد می‌کند.  
2. داده‌ها به مدل یادگیری ماشین (`filename.pkl`) ارسال می‌شود.  
3. مدل پیش‌بینی می‌کند که تراکنش **تقلبی (1)** یا **معتبر (0)** است.  
4. نتیجه روی صفحه وب نمایش داده می‌شود.  

### 🛠 تکنولوژی‌های استفاده‌شده
- Python (Flask)  
- یادگیری ماشین (scikit-learn)  
- HTML و CSS برای رابط کاربری  
- Jupyter Notebook برای آموزش و تحلیل  

---

✅ نویسنده: *سجاد علی بخشی*  
