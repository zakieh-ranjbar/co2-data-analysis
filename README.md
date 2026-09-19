# تحلیل و بررسی داده‌های انتشار CO₂

این پروژه با هدف تحلیل، پردازش و بصری‌سازی داده‌های مربوط به انتشار دی‌اکسید کربن (CO₂) با استفاده از زبان برنامه‌نویسی Python توسعه داده شده است.

در این پروژه، داده‌های مربوط به انتشار CO₂ با استفاده از کتابخانه‌های رایج تحلیل داده پردازش شده و اطلاعات به‌دست‌آمده در قالب آمار توصیفی و نمودارهای قابل فهم ارائه می‌شوند.

## Technologies

- Python
- Pandas برای خواندن و تحلیل داده‌ها
- Matplotlib برای رسم نمودارها
- Pytest برای تست کد
- Jupyter Notebook برای نگهداری نسخهٔ اولیهٔ تحلیل

## Project Structure

```text
co2-data-analysis/
├── data/
│   └── co2.csv                 # دیتاست خام
├── notebooks/
│   └── co2_original.ipynb      # نوت‌بوک اولیه
├── outputs/                    # گزارش‌ها و نمودارهای تولیدشده
├── src/
│   ├── analysis.py             # تحلیل و محاسبهٔ آمار
│   └── visualize.py            # ساخت نمودارها
├── tests/
│   └── test_analysis.py        # تست‌های پروژه
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## داده‌ها

داده‌های خام این پروژه در فایل `data/co2.csv` قرار گرفته‌اند. این فایل چهار ستون اصلی دارد:

| نام ستون | توضیح |
|---|---|
| `engine` | حجم موتور |
| `cylandr` | تعداد سیلندر |
| `fuelcomb` | مصرف ترکیبی سوخت |
| `out1` | خروجی CO2 در دیتاست |

## یافته‌های پایه

- مجموع ۵۰۰ مقدار اول `out1`: **۱۳۴٬۰۱۳**
- میانگین `out1`: **۲۶۸٫۰۲۶**
- کمینه: **۱۱۰**
- بیشینه: **۴۸۸**
- انحراف معیار: **۶۷٫۱۰۰**

## نصب و اجرا

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements-dev.txt
```

ساخت گزارش عددی و نمودارها:

```bash
python -m src.analysis
python -m src.visualize
```

اجرای تست‌ها:

```bash
pytest
```

## نوت‌بوک

نسخهٔ اولیهٔ تحلیل در فایل `notebooks/co2_original.ipynb` قرار دارد. نسخهٔ ساختاریافته و قابل‌تکرار کد در پوشهٔ `src/` ارائه شده است.

## خروجی‌ها

- `outputs/summary.json`: آمار، مقادیر گمشده و همبستگی‌ها
- `outputs/co2_distribution.png`: توزیع خروجی CO2
- `outputs/features_vs_co2.png`: رابطهٔ ویژگی‌ها با خروجی CO2
- `outputs/correlation_heatmap.png`: ماتریس همبستگی

## مجوز

MIT
