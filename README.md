# Inventory Management System (Django)

A **role-based Inventory Management System** built using **Django** that helps manage products, suppliers, stock movements, and inventory history with proper authentication and authorization.

This project is designed to reflect **real-world business logic** and is fully **interview-ready**.

---

## 🚀 Features

### 🔐 Authentication & Authorization
- User login and logout
- Role-based access using **Admin** and **Staff** roles
- Backend-level permission protection (not just UI hiding)

### 📦 Inventory Management
- Add, update, view, and delete products (Admin only)
- Manage product categories and suppliers
- Search products by name

### 🔄 Stock Management
- Stock IN (increase quantity)
- Stock OUT (decrease quantity with validation)
- Prevents negative stock

### 🧾 Stock History (Audit Log)
- Tracks every stock IN and OUT
- Records:
  - Product
  - Change type (IN / OUT)
  - Quantity changed
  - Previous & new quantity
  - User who performed the action
  - Timestamp

### 👥 Role-Based Access
- **Admin**
  - Full access (CRUD operations)
- **Staff**
  - View products
  - Perform Stock IN / OUT
  - View stock history
  - Cannot add, edit, or delete products

### 🌐 REST API (Django REST Framework)
- `GET /api/products/`
- `POST /api/stock/in/`
- `POST /api/stock/out/`
- `GET /api/stock/history/`
- APIs secured with authentication

---

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **API**: Django REST Framework (DRF)
- **Database**: SQLite
- **Frontend**: HTML, Bootstrap
- **Authentication**: Django Auth
- **Version Control**: Git & GitHub

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/umamaheswararao04/inventory-management-system.git
cd inventory-management-system


---

## 📸 Screenshots

### Admin – Products Management
![Admin Products](https://github.com/user-attachments/assets/b97bb148-948f-446a-9943-e6d83297b81f)

### Admin – Edit Product
![Edit Product](https://github.com/user-attachments/assets/4a61ac93-9606-436c-a90f-18502d18efa6)

### Login Page
![Login](https://github.com/user-attachments/assets/c947680b-a437-40a7-8943-7f860aa25f97)

### Staff – Products View
![Staff Products](https://github.com/user-attachments/assets/f8c819d5-c6f3-4646-a3a9-5314e011518f)

### Stock History
![Stock History](https://github.com/user-attachments/assets/e3288cfa-ad94-4786-a6ef-50e23eb851b9)

### Stock In
![Stock In](https://github.com/user-attachments/assets/da773d04-2112-47c7-8d47-46bdba60621b)

### Stock Out
![Stock Out](https://github.com/user-attachments/assets/cf0d213-8045-4bbf-b3ae-75a528452c0c)







