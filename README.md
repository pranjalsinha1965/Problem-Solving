# Problem-Solving

# 📘 Exporting Your Django Database – A Developer's Guide

Whether you're backing up data, migrating servers, or just exploring options, exporting your database in Django is easier than you think.

---

## ✨ Why Export Your Django Database?

Here are a few common scenarios:

- **Backups** before major changes.
- **Migration** to another host or database (like SQLite → PostgreSQL).
- **Data Sharing** with teammates, analysts, or testers.
- **Testing** with real data.
- **Compliance** and recordkeeping.

---

## 🧠 Understand Your Database

Django supports:
- SQLite (default)
- PostgreSQL
- MySQL
- Oracle, and more

Each may require different tools—but most techniques work across the board.

---

## ✅ Method 1: Use Django’s `dumpdata` Command

### Full database export:

```bash
python manage.py dumpdata > db.json
```

### Specific app export:

```bash
python manage.py dumpdata myapp > myapp_data.json
```

### Single model export:

```bash
python manage.py dumpdata myapp.MyModel > model_data.json
```

#### Bonus: Reimporting with fixtures:

```bash
python manage.py loaddata db.json
```

---

## 🛠️ Method 2: Use Your Database’s Native Tools

### For SQLite:

```bash
cp db.sqlite3 db_backup.sqlite3
sqlite3 db.sqlite3 .dump > db_dump.sql
```

### For PostgreSQL:

```bash
pg_dump -U your_username your_database > backup.sql
```

---

## 📊 Method 3: Export to CSV (Excel / Google Sheets)

### Sample Model:

```python
# models.py
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
```

### CSV Export Script:

```python
# export_books.py
import csv
from myapp.models import Book

with open('books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Author'])

    for book in Book.objects.all():
        writer.writerow([book.title, book.author])
```

### Run via shell:

```bash
python manage.py shell < export_books.py
```

---

## 🧑‍💻 Method 4: Use Django Admin Actions

```python
# admin.py
import csv
from django.http import HttpResponse
from .models import Book

@admin.action(description='Export selected books to CSV')
def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=books.csv'
    writer = csv.writer(response)
    writer.writerow(['Title', 'Author'])

    for book in queryset:
        writer.writerow([book.title, book.author])

    return response

class BookAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

admin.site.register(Book, BookAdmin)
```

---

## 🙋‍♀️ FAQs

### Can I export in XML?

```bash
python manage.py dumpdata --format=xml > db.xml
```

### Best format for backups?

- **JSON**: Django-specific use (great for fixtures)
- **SQL**: Full backup, including schema

### Can I automate it?

Yes! Use cron jobs or scripts to schedule `dumpdata` + upload to cloud (e.g. AWS S3, Google Drive).

---

## 🔗 Further Reading

- [Django dumpdata docs](https://docs.djangoproject.com/en/stable/ref/django-admin/#dumpdata)
- [pg_dump – PostgreSQL tool](https://www.postgresql.org/docs/current/app-pgdump.html)
- [Backing up SQLite](https://sqlite.org/cli.html)
- [Django loaddata docs](https://docs.djangoproject.com/en/stable/ref/django-admin/#loaddata)

---

## ✅ Wrapping Up

You’ve now got multiple ways to handle Django database exports—from simple JSON fixtures to full SQL dumps or spreadsheet-ready CSVs.

Happy exporting 🚀

## Important questions frquently asked in interviews and all: (From Neetcode.io)
1. Contains Duplicate - Leetcode 217
2. TwoSum Leetcode 1
3. Valid Palindrome - Leetcode 125
4. Binary Search - Leetcode 704 
5. Subsets - Leetcode 78
6. Invert a Binary Tree - Leetcode 226 
7. Detect Squares - Letcode 2013
8. Linked List Cycle - Leetcode 141 
9. N-Queens - Leetcode 51 
10. House Robber - Leetcode 198
11. Meeting Rooms - Leetcode 252 
12. Max Area of Islands - Leetcode 695
13. Encode and Decode Strings - Leetcode 271 
14. Maximum Subarray = Leetcode - 53
15. Permutations - Leetcode 46
16. Single Number - Leetcode 136 
17. Longest Consecutive Sequence - Leetcode
18. Product of Array Except Self - Leetcode 238 
19. Climbing Stairs - Leetcode 70
20. Coin Change - Leetcode 322
21. Add Two Numbers - Leetcode 2
22. Kth Element any in a stream - Leetcode 
23. Validate Binary Search - Leetcode 98