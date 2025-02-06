# 🔐 File Encryption & Decryption Web App

This project is a **Flask-based web application** that allows users to **encrypt and decrypt files** securely. Users can upload a file, choose to encrypt or decrypt it, and the processed file is automatically downloaded to their system.

---

## 📌 Features

- **Upload a file** for encryption or decryption
- **Automatic encryption** using a secure key
- **Auto-download of processed files**
- **File size validation** (Max: 10MB)
- **Prevention of multiple submissions** to avoid redundant processing
- **Real-time UI feedback** during file processing

---

## 🚀 Installation Guide

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Amansaxena16/Encrypty.git
cd Encrypty
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run the Flask App**
```sh
python app.py
```

The application will start at **http://127.0.0.1:5000/**

---

## 🛠️ How It Works

1. **Upload a File** → Users select a file from their system.
2. **Choose an Operation** → Select either **Encrypt** or **Decrypt**.
3. **Process & Auto-Download** → The file is processed and automatically downloaded to the user's system.
4. **Memory Cleanup** → The temporary file is deleted after processing.

---

## 📂 Project Structure
```
/encryption-web-app
│── /static              # Contains CSS & JS files
│── /templates           # HTML templates for frontend
│── /uploads             # Temporarily stores uploaded files
│── app.py               # Main Flask application
│── encryption.py        # Encryption & Decryption logic
│── requirements.txt     # Required dependencies
│── README.md            # Project Documentation
```

---

## 📚 Libraries Used

- **Flask** → Web framework
- **Cryptography** → Secure encryption & decryption
- **OS** → File handling
- **Werkzeug** → Secure file uploads

Install them using:
```sh
pip install flask cryptography werkzeug
```

---

## 🔍 Possible Test Cases & Edge Cases

| Scenario | Expected Behavior |
|----------|------------------|
| Upload no file & submit | Show error message |
| Upload a file > 10MB | Reject the file & display the alert |
| Select encrypt but click multiple times | Prevent multiple submissions |
| Successfully process a file | Auto-download processed file |
| Reload the page after submission | Ensures fresh upload & UI reset |

---

## 💡 Future Enhancements

- ✅ **User Authentication** for secure access
- ✅ **AES Key Management** for better encryption handling
- ✅ **Progress Bar UI** for better user experience
- ✅ **Multi-file encryption support**

---

## 🤝 Contribution Guide

1. **Fork the repo** & create a new branch.
2. Make your changes & test them.
3. Submit a **Pull Request** with a detailed description.

---

## 📞 Support & Contact

For any queries or suggestions, feel free to reach out:
📧 Email: your-email@example.com  
🐦 Twitter: [@yourTwitterHandle](https://twitter.com/yourTwitterHandle)  

---

🔒 **"Secure your files, one click at a time!"**

