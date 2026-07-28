```markdown
# 🧮 Ultimate Math Calculator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![SymPy](https://img.shields.io/badge/SymPy-1.12-orange)](https://www.sympy.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24-lightblue)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-MiladMA87-black?logo=github)](https://github.com/MiladMA87)

> **یک ماشین‌حساب جامع برای ریاضیات پیشرفته**  
> پشتیبانی از محاسبات عددی، سمبلیک، حل معادله، مشتق، انتگرال، حد، ماتریس، معادلات دیفرانسیل و رسم نمودار

---

## ✨ ویژگی‌های برجسته

| دسته‌بندی | قابلیت‌ها |
|-----------|-----------|
| 📊 **محاسبات عددی** | عملیات سریع با توابع مثلثاتی، لگاریتمی، نمایی |
| 🧮 **محاسبات سمبلیک** | کار با متغیرهای نمادین (`x`, `y`, `z`, `t`) |
| ✏️ **حل معادله** | حل معادلات خطی، درجه‌۲، غیرخطی (دقیق و عددی) |
| 📈 **مشتق و انتگرال** | مشتق مرتبه‌های مختلف، انتگرال معین و نامعین |
| 🔢 **حد و سری** | محاسبه حد در نقاط مختلف، سری تیلور |
| 🧩 **ساده‌سازی** | بسط، فاکتورگیری، ساده‌سازی عبارات |
| 📐 **ماتریس** | ایجاد ماتریس و حل دستگاه معادلات خطی |
| 📉 **رسم نمودار** | رسم نمودار توابع با کتابخانه Matplotlib |
| 💾 **ذخیره‌سازی** | ذخیره و بازیابی متغیرها از فایل |

---

## 📸 پیش‌نمایش

```bash
╔════════════════════════════════════════════════════════════╗
║              ULTIMATE MATH CALCULATOR                     ║
║              Created by: Milad Moradpour                 ║
╚════════════════════════════════════════════════════════════╝

Available Commands:
────────────────────────────────────────────────────────────
  calc <expression>    : Numeric calculation
  sym <expression>     : Symbolic calculation
  solve <expression>   : Solve equation
  diff <expression>    : Derivative
  int <expression>     : Indefinite integral
  defint <expr> a b    : Definite integral from a to b
  limit <expr> a       : Limit at point a
  expand <expression>  : Expand expression
  simplify <expr>      : Simplify expression
  factor <expression>  : Factor expression
  taylor <expr> n      : Taylor series order n
  plot <expression>    : Plot graph
  set <var> <value>    : Set variable
  vars                 : Show variables
  clear                : Clear variables
  history              : Show history
  save                 : Save variables
  load                 : Load variables
  help                 : This help
  exit                 : Exit
────────────────────────────────────────────────────────────

🔢 > calc sin(pi/2) + 3**2
📊 Result: 10.0

🔢 > diff x**3
📈 Derivative: 3*x**2

🔢 > int x**2
∫ Result: x**3/3 + C
```

---

## 🚀 نصب و راه‌اندازی

### پیش‌نیازها
- Python 3.8 یا بالاتر
- pip (مدیریت پکیج‌های Python)

### مراحل نصب

```bash
# ۱. کلون کردن مخزن
git clone https://github.com/MiladMA87/Math_Calculator.git

# ۲. ورود به دایرکتوری پروژه
cd Math_Calculator

# ۳. نصب وابستگی‌ها
pip install -r requirements.txt

# ۴. اجرای برنامه
python Math_Calculator.py
```

### وابستگی‌ها (requirements.txt)

```txt
sympy>=1.12
numpy>=1.24
matplotlib>=3.7
```

---

## 💻 نحوه استفاده

### ۱. اجرا به عنوان برنامه خط فرمان

```bash
python Math_Calculator.py
```

### ۲. استفاده به عنوان کتابخانه در کد خودتان

```python
from Math_Calculator import UltimateMathCalculator

calc = UltimateMathCalculator()

# محاسبه عددی
result = calc.numeric_calc('sin(pi/4) + sqrt(16)')
print(result)  # 4.707106781186547

# محاسبه سمبلیک
expr = calc.symbolic_calc('x**2 + 2*x + 1')
print(expr)  # x**2 + 2*x + 1

# حل معادله
solutions = calc.solve_equation('x**2 - 4')
print(solutions)  # [-2, 2]

# مشتق
derivative = calc.derivative('x**3', 'x', 2)
print(derivative)  # 6*x

# انتگرال معین
integral = calc.definite_integral('x**2', 'x', 0, 1)
print(integral)  # 0.3333333333333333

# حد
limit = calc.limit('sin(x)/x', 'x', 0)
print(limit)  # 1

# سری تیلور
taylor = calc.taylor_series('sin(x)', 'x', 0, 3)
print(taylor)  # x - x**3/6 + O(x**4)

# رسم نمودار
calc.plot_graph('x**2', -5, 5)
```

### ۳. مثال‌های عملی

```python
# حل دستگاه معادلات
A = [[2, 3], [4, 5]]
b = [8, 14]
solution = calc.solve_matrix(A, b)
print(solution)  # [1.0, 2.0]

# معادله دیفرانسیل
ode_solution = calc.solve_ode('f(x).diff(x) - f(x)', 'f(x)')
print(ode_solution)  # Eq(f(x), C1*exp(x))

# بسط و فاکتورگیری
expanded = calc.expand('(x+1)**3')
print(expanded)  # x**3 + 3*x**2 + 3*x + 1

factored = calc.factor('x**2 - 4')
print(factored)  # (x - 2)*(x + 2)
```

---

## 📁 ساختار پروژه

```
Math_Calculator/
├── Math_Calculator.py     # فایل اصلی برنامه
├── LICENSE                # مجوز پروژه
└── README.md              # مستندات پروژه
```

---

## 🛠️ دستورات کامل محیط تعاملی

| دستور | توضیح | مثال |
|-------|-------|------|
| `calc <expr>` | محاسبه عددی عبارت | `calc sin(pi/2) + 3**2` |
| `sym <expr>` | محاسبه سمبلیک عبارت | `sym x**2 + 2*x` |
| `solve <expr>` | حل معادله | `solve x**2 - 4` |
| `diff <expr>` | محاسبه مشتق | `diff x**3` |
| `int <expr>` | انتگرال نامعین | `int x**2` |
| `defint <expr> a b` | انتگرال معین از a تا b | `defint x**2 0 1` |
| `limit <expr> a` | حد در نقطه a | `limit sin(x)/x 0` |
| `expand <expr>` | بسط عبارت | `expand (x+1)**2` |
| `simplify <expr>` | ساده‌سازی عبارت | `simplify x**2+2*x+1` |
| `factor <expr>` | فاکتورگیری | `factor x**2-4` |
| `taylor <expr> n` | سری تیلور مرتبه n | `taylor sin(x) 5` |
| `plot <expr>` | رسم نمودار | `plot x**2` |
| `set <var> <value>` | تعریف متغیر عددی | `set a 5` |
| `vars` | نمایش متغیرهای تعریف شده | `vars` |
| `clear` | پاک کردن متغیرها | `clear` |
| `history` | نمایش تاریخچه محاسبات | `history` |
| `save` | ذخیره متغیرها در فایل | `save` |
| `load` | بارگذاری متغیرها از فایل | `load` |
| `help` | نمایش راهنما | `help` |
| `exit` | خروج از برنامه | `exit` |

---

## 🧪 اجرای تست‌ها

برای تست عملکرد ماشین‌حساب:

```python
# تست سریع
calc = UltimateMathCalculator()

# تست محاسبات عددی
assert calc.numeric_calc('2 + 2') == 4
assert calc.numeric_calc('sin(pi/2)') == 1.0

# تست مشتق
assert calc.derivative('x**2') == 2*calc.x

# تست حل معادله
assert set(calc.solve_equation('x**2 - 4')) == {-2, 2}

print("✅ همه تست‌ها با موفقیت گذرانده شدند!")
```

---

## 🤝 مشارکت در توسعه

خوشحال می‌شیم که شما هم در بهبود این پروژه مشارکت کنید! مراحل زیر را دنبال کنید:

1. **فورک** (Fork) کردن مخزن
2. ایجاد **برنچ جدید** برای تغییرات:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **کامیت** (Commit) تغییرات:
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **پوش** (Push) به برنچ:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. باز کردن یک **Pull Request**

### قوانین مشارکت
- کد را با استانداردهای **PEP 8** هماهنگ کنید
- برای تغییرات بزرگ، ابتدا یک **Issue** باز کنید
- حتماً برای قابلیت‌های جدید، **تست** بنویسید
- مستندات را به‌روز کنید

---

## 📄 مجوز

این پروژه تحت مجوز **MIT** منتشر شده است - برای جزئیات بیشتر فایل [LICENSE](LICENSE) را ببینید.

```
MIT License

Copyright (c) 2026 Milad Moradpour

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
...
```

---

## 📞 ارتباط با توسعه‌دهنده

- **نام:** میلاد مرادپور (Milad Moradpour)
- **گیت‌هاب:** [@MiladMA87](https://github.com/MiladMA87)
- **ایمیل:** [miladmoradpor.j@gmail.com](mailto:miladmoradpor.j@gmail.com)
- **آدرس مخزن:** [https://github.com/MiladMA87/Math_Calculator](https://github.com/MiladMA87/Math_Calculator)

---

## 🙏 قدردانی

- کتابخانه‌ی **[SymPy](https://www.sympy.org/)** برای محاسبات سمبلیک قدرتمند
- کتابخانه‌ی **[NumPy](https://numpy.org/)** برای محاسبات عددی
- کتابخانه‌ی **[Matplotlib](https://matplotlib.org/)** برای رسم نمودار
- الهام‌گیری از پروژه‌های متن‌باز ریاضی

---

## ⭐ حمایت از پروژه

اگر این پروژه برای شما مفید بود:

- ⭐ به مخزن **Star** بدید
- 🔄 با دوستانتان به اشتراک بگذارید
- 🐛 باگ‌ها را در بخش [Issues](https://github.com/MiladMA87/Math_Calculator/issues) گزارش دهید
- 💡 ایده‌های خود را برای بهبود ارائه دهید


**ساخته شده با ❤️ توسط میلاد مرادپور**  
**آخرین بروزرسانی:** July 2026
```

---

## ✅ نکات نهایی

1. فایل رو با نام `README.md` ذخیره کنید
2. کنار فایل `Math_Calculator.py` قرارش بدید
3. فایل `requirements.txt` رو هم بسازید:
   ```txt
   sympy>=1.12
   numpy>=1.24
   matplotlib>=3.7
   ```