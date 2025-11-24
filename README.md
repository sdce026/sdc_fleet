# SDC Fleet App
Arabic + English Fleet Management System
SDC Fleet Management System
Complete Fleet, Fueling & Maintenance Management Module for ERPNext

SDC Fleet هو نظام متكامل يُضيف قدرات احترافية لإدارة أسطول المعدات والمولدات داخل ERPNext v15+
مع تحليل فوري للوقود، والصيانة، وساعات التشغيل، وتتبّع المعدات…
كل ذلك من خلال واجهة بسيطة وسريعة ومرنة.

<div align="center">
🚜 إدارة أسطول – 🔧 صيانة – ⛽ وقود – 📊 تحليلات – 🛰 تتبع حركة — في نظام واحد
Screenshots
Dashboard	Fuel Analytics	Equipment Profile

	
	
</div>
📌 المميزات الرئيسية
1) إدارة الوقود Fueling Management

تسجيل عمليات التعبئة تلقائيًا

حساب الاستهلاك الفعلي (لتر/ساعة)

مقارنة بين الاستهلاك الطبيعي والفعلي

إشعارات عند وجود استهلاك غير طبيعي

Dashboard تحليلي كامل جاهز

2) الصيانة الذكية Smart Maintenance

إنشاء خطط صيانة Preventive و Corrective

حساب ساعات التشغيل منذ آخر صيانة

تنبيه تلقائي عند:

250 ساعة ✔

300 ساعة ✔

500 ساعة ✔

أو أي قيمة تُحددها من الإعدادات

سجل كامل لقطع الغيار المطلوبة

3) تتبع حركة المعدات Asset Movement

تتبع مواقع المعدات

حساب ساعات التشغيل اليومية

ربط الحركة بالتعبئة والصيانة

4) لوحة تحكم متقدمة – Fleet Dashboard PRO

✔ KPIs
✔ Fuel heat-map
✔ صيانة قريبة
✔ مؤشرات استهلاك غير طبيعي
✔ أكثر المعدات صرفًا للديزل
✔ أداء السائقين

🧩 الموديولات والـ Doctypes الموجودة في النظام
Fueling & Fuel Analytics
Doctype	وصف
Fueling Log	تسجيل كل عملية تعبئة
Fuel Consumption Analysis	تحليل الاستهلاك – تلقائي
Fuel Approval Log	نظام الموافقات للديزل
Maintenance
Doctype	وصف
Maintenance Request	طلب صيانة من المواقع
Maintenance Log	سجل الصيانة الكامل
Maintenance Cycle Record	تتبّع السايكل (250/300/500 ساعة)
Maintenance Required Item	قطع الغيار المطلوبة
Equipment
Doctype	وصف
Equipment Maintenance Settings	إعدادات الصيانة لكل معدّة
Equipment Spare Part	إدارة قطع الغيار
Driver Log	سجل السائقين
Asset Movement Log	حركة المعدات
Equipment Dashboard	Dashboard خاص بكل معدّة
⚙️ التركيب Installation
1️⃣ تحميل التطبيق من GitHub
cd ~/frappe-bench
bench get-app https://github.com/sdce026/sdc_fleet.git

2️⃣ تثبيت التطبيق على الموقع
bench --site yoursite.com install-app sdc_fleet
bench migrate

3️⃣ إعادة تشغيل الخدمات
sudo supervisorctl restart all
sudo systemctl restart nginx

🧱 هيكل المشروع Project Structure
sdc_fleet/
│
├── api/
│   ├── fueling.py
│   ├── maintenance.py
│   ├── dashboard.py
│   └── dashboard_pro.py
│
├── doctype/
│   ├── fueling_log/
│   ├── maintenance_log/
│   ├── maintenance_request/
│   ├── equipment_maintenance_settings/
│   ├── fuel_consumption_analysis/
│   └── ...
│
├── page/
│   └── fleet_dashboard_pro/
│
├── public/
│   └── images/screenshots/
│
├── hooks.py
├── setup.py
├── pyproject.toml
└── README.md

🔌 واجهة البرمجة API
مثال: حساب استهلاك الوقود
from sdc_fleet.api.fueling import calculate_consumption

result = calculate_consumption(asset_id="EXC-001", hours=5, liters=32)

مثال: إنشاء طلب صيانة
from sdc_fleet.api.maintenance import create_request

create_request(
    asset="GEN-450",
    issue="Oil pressure low",
    priority="High"
)

📊 لوحة التحكم Fleet Dashboard PRO

Fuel Analytics

Daily Utilization

Maintenance Cycle

Asset Cost

Driver Performance

Exception Alerts (red flags)

مصممة لتعمل بسرعة وبدون ضغط على السيرفر.

🛠 Roadmap (القادم)

🔄 Mobile app (Android)

🛰 GPS Integration

🧾 Advanced Fuel Billing

📶 IOT sensors support

🛑 Fuel Theft Detection

⛽ Smart Fuel Station module

🤝 المساهمة Contribution

نرحّب بأي مساهمات:

تطوير

تحسين API

Design

توثيق

© SDC – Shams Dubai Contracting

تم بناء النظام بالكامل خصيصًا لمؤسسة شمس دبي للمقاولات
لرفع كفاءة إدارة الأسطول وتقليل التكاليف التشغيلية بشكل احترافي.
