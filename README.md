# SDC Fleet App
Arabic + English Fleet Management System
# 🚚 SDC Fleet – Smart Diesel & Maintenance Management for ERPNext  
**Premium Fleet Management Module for ERPNext v15 — by SDCE**

SDC Fleet هو تطبيق احترافي متكامل لإدارة المعدات والمولدات والديزل داخل ERPNext،  
يدعم مراقبة استهلاك الوقود، ساعات التشغيل، الصيانة الدورية 300 ساعة، المخزون، التنبيهات،  
وداشبورد احترافي (Dashboard Pro) يوفر رؤية كاملة لحالة الأسطول.

---

## 🚀 Features  
### ✔ إدارة الوقود Fueling Log  
- تسجيل تعبئة الديزل  
- احتساب ساعات التشغيل يوميًا  
- احتساب معدل الاستهلاك (لتر/ساعة)  
- تحديث عداد الساعات (Previous → Current)  
- دعم السائق / الأوبريتور  
- رسوم النقل

---

### ✔ الصيانة الدورية 300 ساعة  
- إنشاء Maintenance Request تلقائيًا  
- احتساب الساعات منذ آخر صيانة  
- قائمة قطع الغيار المطلوبة  
- إشعار عند تجاوز 250 / 300 ساعة  
- بدء دورة جديدة بعد الصيانة (Reset Logic)

---

### ✔ Dashboard Pro  
- KPI Cards  
- Fuel Analytics  
- Hour Meter Analytics  
- Maintenance Status  
- Alerts  
- Asset Profiling  

---

### ✔ تقارير احترافية  
- تحليل استهلاك الوقود  
- مراجعة دورات الصيانة  
- تحليل تشغيل المعدات  
- حركة الأصول (Asset Movement)  
- أداء السائقين Driver Log  

---

# 📦 Installation

### 1️⃣ Install from GitHub  
```
bench get-app sdc_fleet https://github.com/sdce026/sdc_fleet.git
bench --site yoursite install-app sdc_fleet
```

### 2️⃣ Required  
- ERPNext v15  
- Frappe Framework v15  

---

# 📁 Included DocTypes  
- Fueling Log  
- Maintenance Log  
- Maintenance Request  
- Maintenance Cycle Record  
- Equipment Maintenance Settings  
- Equipment Spare Part  
- Fuel Consumption Analysis  
- Driver Log  
- Asset Movement Log  
- Asset Daily Utilization  
- Dashboard Pro (Page)

---

# 🖼 Screenshots

### **Dashboard Pro**
![Dashboard Pro](assets/screenshots/dashboard_pro.png)

### **Fueling Log**
![Fueling Log](assets/screenshots/fueling_log.png)

### **Maintenance Request (300h Cycle)**
![Maintenance Request](assets/screenshots/maintenance_request.png)

### **Equipment Profile**
![Equipment Profile](assets/screenshots/equipment_profile.png)

### **Fleet KPIs**
![Fleet KPIs](assets/screenshots/fleet_kpis.png)

### **Fuel Analytics Dashboard**
![Fuel Analytics](assets/screenshots/fuel_analytics.png)

### **Maintenance Cycle Timeline**
![Maintenance Cycle Timeline](assets/screenshots/maintenance_cycle.png)

---

# 🛠 Automation & Logic

### 🔧 Fueling Log  
- Updates previous_hour → current_hour automatically  
- Computes hours_run = current - previous  
- Triggers alerts on abnormal usage  
- Sends data to Dashboard Pro

### 🔧 Maintenance Engine  
- Tracks last maintenance reading  
- Computes hours_since_last  
- Creates automatic Maintenance Request @ 300h  
- Resets cycle upon completion  

### 🔧 Dashboard Pro Integration  
- Real-time KPIs  
- Fuel trend analysis  
- Automatic equipment ranking  
- Smart alerts

---

# 📚 Documentation  
Full documentation is available in the GitHub **Wiki**:  
👉 https://github.com/sdce026/sdc_fleet/wiki

---

# 🧩 GitHub Marketplace Metadata  
- Name: **SDC Fleet Manager**  
- Category: ERPNext Modules  
- Status: Production Ready  
- License: MIT  
- Author: **SDCE Engineering**  

---

# 🏷 Badges

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![ERPNext](https://img.shields.io/badge/ERPNext-v15-blue)
![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Docs](https://img.shields.io/badge/docs-Wiki-blue)

---

# 📞 Support & Contact  
For custom development or support:  
📧 **contact@sdc-engineering.com**  
💼 SDCE — Smart Digital Construction Engineering

---

# 📝 License  
MIT License — Free for commercial and personal use.
