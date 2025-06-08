# 💸 Personal Finance Tracker

A Django-based web application to manage your income, expenses, and account information with category filtering, charts visualization, and export features. The application includes user registration, login, and personalized dashboards.

---

## 📚 Features

✅ User Authentication  
✅ Dashboard Summary (Income, Expenses, Balance)  
✅ Add, Edit, Delete Transactions  
✅ Category Filtering  
✅ Export Transactions as CSV  
✅ Category-wise Charts (Income & Expense) using Chart.js  
✅ Manage Accounts & Cards  


---

## 🖼️ Screenshots

> _(Add your own screenshots here)_

- Dashboard with summary cards
- Filter by category
- Pie charts for income and expenses
- Manage accounts and cards
- Login/Register page

---

## 🛠️ Built With

- **Backend:** Django 4.x
- **Frontend:** HTML, Bootstrap 5, JavaScript
- **Database:** SQLite (default for development)
- **Charts:** Chart.js
- **Authentication:** Django’s built-in user model

---

## 🏗️ Project Structure

finance_tracker/
├── core/
│ ├── templates/
│ │ ├── base.html
│ │ ├── home.html
│ │ ├── income.html
│ │ ├── expenses.html
│ │ ├── charts.html
│ │ ├── accounts.html
│ │ ├── login.html
│ │ ├── register.html
│ │ ├── edit_transaction.html
│ │ └── confirm_delete.html
│ ├── forms.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── admin.py
├── finance_tracker/
│ ├── settings.py
│ └── urls.py
├── db.sqlite3
├── manage.py
└── requirements.txt


🗂️ App Functionality

🏠 Home Dashboard
Shows summary cards (Income, Expense, Balance)
Add transaction (modal)
Filter by category
Export data to CSV
View recent transactions
💸 Income / 🧾 Expense Pages
Show respective filtered transactions

📊 Charts
Two pie charts using Chart.js:
Income by category
Expense by category

🏦 Accounts & Cards
Display linked accounts/cards

👤 Login & Register
User sign-up and login using Django’s authentication
Auth-protected pages


Thank you
