<div align="center">

<img src="Picture1.png" alt="SDC Logo" width="360">

<h1>🚀 SDC Fleet Management System</h1>

<h3>Professional Fleet, Fuel & Maintenance Management Module for ERPNext V15</h3>

<p>
  <img src="https://img.shields.io/badge/Version-1.0.0-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/ERPNext-V15-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Production-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Maintained-Yes-brightgreen?style=for-the-badge">
</p>

</div>


---
# SDC Fleet — Advanced Fleet Management App for ERPNext v15

## 🇬🇧 English Version

SDC Fleet is a complete fleet management application built for ERPNext v15, designed for companies that operate heavy equipment, machinery, and diesel-powered assets.

Features include fuel tracking, maintenance monitoring, daily operating hours analysis, automated alerts, and a professional Fleet Dashboard Pro.

---

## 🔥 Key Features

### ✔ Fueling Log
- Track diesel fueling events  
- Log fuel quantity, price, operator, and time  
- Current & previous hour meter readings  
- Auto-calculates daily operating hours  
- Auto-calculates fuel consumption rate  
- Current reading becomes previous reading next time (correct behavior)

### ✔ Maintenance Log
- Record maintenance operations  
- Track filters, spare parts, diesel, oil, water separator  
- Reset operating hours after maintenance  
- Attach invoices and technician reports  

### ✔ Maintenance Request
- Auto-generated at 300 operating hours  
- Alerts:
  - Maintenance Due  
  - Maintenance Coming Soon  
  - Within Safe Range  
- Ensures maintenance is completed before closing  

### ✔ Equipment Maintenance Settings
- Configure maintenance cycles  
- Define filter list  
- Enable/disable 300-hour automatic logic  

### ✔ Dashboard Pro
- Real-time KPIs  
- Fuel consumption graphs  
- Operating hours analytics  
- Maintenance alerts  
- Equipment performance overview  

### ✔ Additional DocTypes
- Maintenance Cycle Record  
- Driver Log  
- Fuel Approval Log  
- Equipment Spare Parts  
- Asset Daily Utilization  
- Fuel Consumption Analysis  
- Asset Movement Log  

---

# 🚀 Installation

```bash
bench get-app https://github.com/sdce026/sdc_fleet.git
bench --site YOUR_SITE install-app sdc_fleet
bench restart
```

---

# 📊 API Endpoints

### Fueling Log
```
/api/method/sdc_fleet.api.fueling.submit_fueling
```

### Dashboard Pro
```
/api/method/sdc_fleet.api.dashboard_pro.get_kpis
```

---

# 🇸🇦 النسخة العربية — SDC Fleet لإدارة أسطول المعدات

تطبيق SDC Fleet هو نظام متكامل لإدارة المعدات الثقيلة والمولدات.  
يشمل تسجيل الديزل، ساعات التشغيل، الصيانة الدورية 300 ساعة، قطع الغيار، وDashboard Pro.

---

## المميزات الرئيسية

### ✔ سجل تعبئة الوقود
- تسجيل عمليات التعبئة  
- إدخال قراءة العداد الحالية والسابقة  
- حساب ساعات التشغيل اليومية تلقائيًا  
- حساب معدل استهلاك الديزل  
- القراءة الحالية تصبح السابقة في المرة القادمة  

### ✔ سجل الصيانة
- تسجيل عمليات الصيانة  
- تغيير الفلاتر والزيوت  
- إعادة ضبط دورة 300 ساعة  

### ✔ طلبات الصيانة
- إنشاء طلب صيانة تلقائي عند الوصول لـ 300 ساعة  
- تنبيهات صيانة احترافية  
- لا يمكن إغلاق الطلب قبل اكتمال الصيانة  

### ✔ إعدادات الصيانة
- تحديد دورة الصيانة  
- تحديد قائمة الفلاتر  
- ربط قطع الغيار بالمخزن  

### ✔ Dashboard Pro
يشمل:
- حالة المعدات  
- استهلاك الديزل  
- ساعات التشغيل  
- تنبيهات الصيانة  
- رسوم بيانية + KPIs  

---

# 📥 التثبيت

```bash
bench get-app https://github.com/sdce026/sdc_fleet.git
bench --site erp.sdce.com.sa install-app sdc_fleet
```

---

# 📝 License
MIT License

---

# 👨‍💻 Developer  
Shehab  
GitHub: https://github.com/sdce026
