
# ربات تلگرام بیماری‌نامه 🩺

> **توسعه‌دهنده**: پوریا حسینی  
> **تلگرام**: [@isPoori](https://t.me/isPoori)  
> **کانال**: [@OmgaDeveloper](https://t.me/OmgaDeveloper)

این ربات به کاربران اجازه می‌دهد تا اطلاعات بیماری‌ها را جستجو کنند. مدیر ربات می‌تواند بیماری‌های جدیدی به دیتابیس اضافه کند و هر بیماری شامل توضیحات، علل و داروهای پیشنهادی است. کاربران می‌توانند با وارد کردن نام بیماری، اطلاعات مرتبط با آن را دریافت کنند.

## ویژگی‌ها
- **مدیریت بیماری‌ها**: مدیر می‌تواند بیماری جدید اضافه کرده و توضیحات، علل و داروهای پیشنهادی آن را وارد کند.
- **جستجوی بیماری**: کاربران می‌توانند با وارد کردن نام بیماری، اطلاعات آن را جستجو کنند.
- **دیتابیس محلی**: اطلاعات بیماری‌ها در قالب یک فایل JSON ذخیره می‌شود که در سرور ذخیره می‌گردد.

## پیش‌نیازها
1. **Python** 3.7+
2. **کتابخانه‌های مورد نیاز** (در بخش نصب آمده است)
3. **توکن ربات تلگرام** (که از طریق بات‌فادر تلگرام دریافت می‌شود)

## نصب و راه‌اندازی
برای راه‌اندازی ربات، مراحل زیر را طی کنید:

### 1. کلون کردن پروژه
```bash
git clone https://github.com/isPoori/health-info-bot.git
cd health-info-bot
```

### 2. نصب وابستگی‌ها
برای نصب وابستگی‌های Python، دستور زیر را اجرا کنید:

```bash
pip install python-telegram-bot
```

### 3. تنظیمات اولیه
توکن ربات و آی‌دی ادمین را به‌روزرسانی کنید:
- در فایل `main.py`، مقدار `TOKEN` را با توکن ربات و `ADMIN_ID` را با آی‌دی عددی ادمین جایگزین کنید.

### 4. اجرای ربات
پس از تنظیمات بالا، می‌توانید ربات را اجرا کنید:

```bash
python3 main.py
```

## فایل دیتابیس
اطلاعات بیماری‌ها در فایل `disease_db.json` ذخیره می‌شود. این فایل به‌صورت خودکار ساخته می‌شود و اطلاعات هر بیماری شامل موارد زیر است:
- **نام بیماری**: نام بیماری که به عنوان کلید استفاده می‌شود.
- **توضیحات**: توضیح مختصری از بیماری.
- **علل**: دلایل احتمالی بیماری.
- **داروهای پیشنهادی**: داروهای معمول که برای این بیماری توصیه شده‌اند.

## نحوه استفاده
### دستورات ربات
1. **شروع**:
    - کاربر می‌تواند با ارسال دستور `/start` با ربات ارتباط برقرار کند.
2. **دسترسی ادمین**:
    - تنها ادمین ربات می‌تواند با دستور `/admin` به بخش افزودن بیماری دسترسی پیدا کند.
3. **افزودن بیماری جدید**:
    - ادمین می‌تواند گزینه "اضافه کردن بیماری" را انتخاب کرده و اطلاعات بیماری را مرحله به مرحله وارد کند.

### مکالمه افزودن بیماری
- **مرحله 1**: ادمین ابتدا نام بیماری را وارد می‌کند.
- **مرحله 2**: سپس توضیحات بیماری را وارد می‌کند.
- **مرحله 3**: علت‌های بیماری را (با ویرگول جدا شده) وارد می‌کند.
- **مرحله 4**: داروهای پیشنهادی را (با ویرگول جدا شده) وارد می‌کند.
- پس از تکمیل مراحل، بیماری در دیتابیس ذخیره می‌شود.

### جستجوی بیماری
کاربران با وارد کردن نام بیماری، اطلاعات آن را دریافت خواهند کرد. اگر بیماری در دیتابیس نباشد، پیام "بیماری مورد نظر پیدا نشد" برای کاربر ارسال می‌شود.

## ساختار کد
- **توابع اصلی**:
    - `start`: پیام خوش‌آمدگویی به کاربر ارسال می‌کند.
    - `admin`: دسترسی ادمین را بررسی کرده و گزینه‌ها را نمایش می‌دهد.
    - `add_disease`: فرآیند افزودن بیماری جدید را مدیریت می‌کند.
    - `get_disease_info`: اطلاعات بیماری مورد نظر کاربر را جستجو و نمایش می‌دهد.
- **دیتابیس**:
    - از فایل `disease_db.json` برای ذخیره اطلاعات استفاده شده است.
    - دو تابع `load_disease_db` و `save_disease_db` برای مدیریت اطلاعات دیتابیس به کار می‌روند.

## مثال‌ها
### پیام خوش‌آمدگویی
```
/start
سلام! برای دریافت راهنمایی بیماری خود را ارسال کنید.
```

### افزودن بیماری (برای ادمین)
```
/admin
اضافه کردن بیماری -> لطفاً نام بیماری جدید را وارد کنید.
```

### جستجوی بیماری
```
کاربر: سرماخوردگی
ربات: بیماری: سرماخوردگی
       توضیحات: یک بیماری ویروسی متداول که ...
       علل: ویروس سرماخوردگی، تغییرات دما، ...
       داروهای پیشنهادی: آنتی‌هیستامین، استامینوفن، ...
```

## نکات امنیتی
- حتماً `ADMIN_ID` را به آی‌دی عددی ادمین واقعی ربات تغییر دهید.
- توکن ربات را در مکانی امن نگه دارید و آن را به اشتراک نگذارید.

## توسعه‌دهنده
- **پوریا حسینی**
- برای ارتباط مستقیم، به [تلگرام](https://t.me/isPoori) پیام دهید.

## مجوز
[MIT](LICENSE)
