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

Goto List for starting coding: 

## ✨ 𝟏𝟓 𝐋𝐞𝐞𝐭𝐂𝐨𝐝𝐞 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 TO BE SOLVED REPEATEDLY ✨

I’ve solved 2500+ coding problems across different platforms.
But for PBC interviews, I focused on a small list that mattered most.
These 15 questions helped me quickly revise the important patterns and build real confidence.

### 🔍 𝐒𝐨𝐫𝐭𝐢𝐧𝐠 & 𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠
🔹 [Search in Rotated Sorted Array](https://lnkd.in/gt8nYfs4)
🔹 [Median of Two Sorted Arrays](https://lnkd.in/g7dV4DcJ)
### 🪟 𝐒𝐥𝐢𝐝𝐢𝐧𝐠 𝐖𝐢𝐧𝐝𝐨𝐰
 3. 🔹 [Minimum Window Substring](https://lnkd.in/gQa2S4W6)
 4. 🔹 [Longest Repeating Character Replacement](https://lnkd.in/gaEeGNJD)
### 📊 𝐏𝐫𝐞𝐟𝐢𝐱 𝐒𝐮𝐦
 5. 🔹 [Subarray Sum Equals K](https://lnkd.in/gKMvGjic)
 6. 🔹 [Range Sum Query - Immutable](https://lnkd.in/gyU-V6aB)
### 🧵 𝐓𝐫𝐢𝐞𝐬
 7. 🔹 [Implement Trie (Prefix Tree)](https://lnkd.in/gJWPgMxW)
 8. 🔹 [Word Search II](https://lnkd.in/g9gPWmze)
### 🧠 𝐃𝐲𝐧𝐚𝐦𝐢𝐜 𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐦𝐢𝐧𝐠
 9. 🔹 [Coin Change II](https://lnkd.in/gHh4VYdU)
 10. 🔹 [Word Break II](https://lnkd.in/gifJtP37)
 11. 🔹 [Longest Palindromic Substring](https://lnkd.in/g-R59vcE)
### 🔄 𝐁𝐚𝐜𝐤𝐭𝐫𝐚𝐜𝐤𝐢𝐧𝐠
 12. 🔹 [Subsets II](https://lnkd.in/g87BjD2z)
 13. 🔹 [Palindrome Partitioning](https://lnkd.in/gYru9v7P)
### 🌐 𝐆𝐫𝐚𝐩𝐡𝐬
 14. 🔹 [Course Schedule II](https://lnkd.in/gjv_ijdk)
 15. 🔹 [Word Ladder II](https://lnkd.in/gBTgDYjH)

 ## 🔝 𝐌𝐮𝐬𝐭-𝐃𝐨 𝐒𝐥𝐢𝐝𝐢𝐧𝐠 𝐖𝐢𝐧𝐝𝐨𝐰 𝐏𝐫𝐨𝐛𝐥𝐞𝐦𝐬 𝐟𝐨𝐫 𝐏𝐁𝐂 𝐈𝐧𝐭𝐞𝐫𝐯𝐢𝐞𝐰𝐬 🚪➡️

### 🟢🟢🟢🟢 𝐄𝐚𝐬𝐲 🟢🟢🟢🟢
 1. 💰 [𝐌𝐚𝐱𝐢𝐦𝐮𝐦 𝐀𝐯𝐞𝐫𝐚𝐠𝐞 𝐒𝐮𝐛𝐚𝐫𝐫𝐚𝐲 𝐈].(https://lnkd.in/gb92FXT7)
 2. 💰 [𝐌𝐚𝐱𝐢𝐦𝐮𝐦 𝐒𝐮𝐦 𝐒𝐮𝐛𝐚𝐫𝐫𝐚𝐲 𝐨𝐟 𝐒𝐢𝐳𝐞 𝐊.(https://lnkd.in/g_nJNtHJ)
 3. 💰 [𝐂𝐡𝐞𝐜𝐤 𝐈𝐟 𝐀𝐥𝐥 𝐂𝐡𝐚𝐫𝐚𝐜𝐭𝐞𝐫𝐬 𝐇𝐚𝐯𝐞 𝐄𝐪𝐮𝐚𝐥 𝐍𝐮𝐦𝐛𝐞𝐫 𝐨𝐟 𝐎𝐜𝐜𝐮𝐫𝐫𝐞𝐧𝐜𝐞𝐬].(https://lnkd.in/ghrU5UuJ)
4. 💰 [𝐍𝐮𝐦𝐛𝐞𝐫 𝐨𝐟 𝐒𝐮𝐛𝐬𝐭𝐫𝐢𝐧𝐠𝐬 𝐂𝐨𝐧𝐭𝐚𝐢𝐧𝐢𝐧𝐠 𝐀𝐥𝐥 𝐓𝐡𝐫𝐞𝐞 𝐂𝐡𝐚𝐫𝐚𝐜𝐭𝐞𝐫𝐬].(https://lnkd.in/gZd7s2mC)

### 🟡🟡🟡🟡 𝐌𝐞𝐝𝐢𝐮𝐦 🟡🟡🟡🟡
1. 💰 [𝐋𝐨𝐧𝐠𝐞𝐬𝐭 𝐒𝐮𝐛𝐬𝐭𝐫𝐢𝐧𝐠 𝐖𝐢𝐭𝐡𝐨𝐮𝐭 𝐑𝐞𝐩𝐞𝐚𝐭𝐢𝐧𝐠 𝐂𝐡𝐚𝐫𝐚𝐜𝐭𝐞𝐫𝐬].(https://lnkd.in/gty3gwAG)
2. 💰 [𝐌𝐢𝐧𝐢𝐦𝐮𝐦 𝐒𝐢𝐳𝐞 𝐒𝐮𝐛𝐚𝐫𝐫𝐚𝐲 𝐒𝐮𝐦].(https://lnkd.in/gdCgGpUV)
3. 💰 [𝐅𝐫𝐮𝐢𝐭𝐬 𝐢𝐧𝐭𝐨 𝐁𝐚𝐬𝐤𝐞𝐭𝐬].(https://lnkd.in/ge6NFV3Q)
4. 💰 [𝐏𝐞𝐫𝐦𝐮𝐭𝐚𝐭𝐢𝐨𝐧 𝐢𝐧 𝐒𝐭𝐫𝐢𝐧𝐠].(https://lnkd.in/gqGJwztv)
5. 💰 [𝐅𝐢𝐧𝐝 𝐀𝐥𝐥 𝐀𝐧𝐚𝐠𝐫𝐚𝐦𝐬 𝐢𝐧 𝐚 𝐒𝐭𝐫𝐢𝐧𝐠].(https://lnkd.in/gdhc4Pcb)
6. 💰 [𝐂𝐨𝐮𝐧𝐭 𝐍𝐮𝐦𝐛𝐞𝐫 𝐨𝐟 𝐍𝐢𝐜𝐞 𝐒𝐮𝐛𝐚𝐫𝐫𝐚𝐲𝐬].(https://lnkd.in/g2Kyz7tj)
7. 💰 [𝐒𝐮𝐛𝐚𝐫𝐫𝐚𝐲𝐬 𝐖𝐢𝐭𝐡 𝐊 𝐃𝐢𝐟𝐟𝐞𝐫𝐞𝐧𝐭 𝐈𝐧𝐭𝐞𝐠𝐞𝐫𝐬].(https://lnkd.in/gc88JhBz)

### 🔴🔴🔴🔴 𝐇𝐚𝐫𝐝 🔴🔴🔴🔴
1. 💰 [𝐒𝐥𝐢𝐝𝐢𝐧𝐠 𝐖𝐢𝐧𝐝𝐨𝐰 𝐌𝐚𝐱𝐢𝐦𝐮𝐦].(https://lnkd.in/gHv3i76F)
2. 💰 [𝐌𝐢𝐧𝐢𝐦𝐮𝐦 𝐖𝐢𝐧𝐝𝐨𝐰 𝐒𝐮𝐛𝐬𝐭𝐫𝐢𝐧𝐠].(https://lnkd.in/gQa2S4W6)
3. 💰 [𝐂𝐨𝐮𝐧𝐭 𝐨𝐟 𝐒𝐦𝐚𝐥𝐥𝐞𝐫 𝐍𝐮𝐦𝐛𝐞𝐫𝐬 𝐀𝐟𝐭𝐞𝐫 𝐒𝐞𝐥𝐟].(https://lnkd.in/ggdVayFY)
4. 💰 [𝐌𝐚𝐱𝐢𝐦𝐢𝐳𝐞 𝐒𝐜𝐨𝐫𝐞 𝐨𝐟 𝐚 𝐆𝐨𝐨𝐝 𝐒𝐮𝐛𝐚𝐫𝐫𝐚𝐲].(https://lnkd.in/gDwJ93WU)

## 𝗠𝗮𝘀𝘁𝗲𝗿𝗶𝗻𝗴 𝗕𝗶𝗻𝗮𝗿𝘆 𝗦𝗲𝗮𝗿𝗰𝗵 – 𝗙𝗿𝗼𝗺 𝗕𝗮𝘀𝗶𝗰 𝘁𝗼 𝗔𝗱𝘃𝗮𝗻𝗰𝗲𝗱

### 🔹 𝗦𝘁𝗲𝗽 𝟭: 𝗕𝗮𝘀𝗶𝗰𝘀 – 𝗨𝗻𝗱𝗲𝗿𝘀𝘁𝗮𝗻𝗱𝗶𝗻𝗴 𝘁𝗵𝗲 𝗖𝗼𝗿𝗲
Works only on monotonic conditions (sorted or yes/no search space).
Narrow the range until the answer is found.
Common pitfalls: overflow (mid = low + (high - low)/2), wrong boundaries, infinite loops.
Easy LeetCode Problems:
1️⃣ [Binary Search](https://lnkd.in/gS6HJ9sJ)
2️⃣ [First Bad Version](https://lnkd.in/gYv94xhN)
3️⃣ [Guess Number Higher or Lower](https://lnkd.in/gQxMFRuP)
4️⃣ [Search Insert Position](https://lnkd.in/ghTEhu68)
5️⃣ [Sqrt(x)](https://lnkd.in/grR6Qprg)

### 🔹 𝗦𝘁𝗲𝗽 𝟮: 𝗜𝗻𝘁𝗲𝗿𝗺𝗲𝗱𝗶𝗮𝘁𝗲 – 𝗕𝗶𝗻𝗮𝗿𝘆 𝗦𝗲𝗮𝗿𝗰𝗵 𝗩𝗮𝗿𝗶𝗮𝗻𝘁𝘀
Boundaries – find leftmost/rightmost element.
Rotated Arrays – binary search on two halves.
Peak Finding – search in non-standard monotonic structures.
Medium LeetCode Problems:
1️⃣ [Find First and Last Position](https://lnkd.in/g3NuHzvM)
2️⃣ [Search in Rotated Sorted Array](https://lnkd.in/gt8nYfs4)
3️⃣ [Find Peak Element](https://lnkd.in/gXvQvugc)
4️⃣ [Find Minimum in Rotated Sorted Array](https://lnkd.in/gTBiuc6x)
5️⃣ [Koko Eating Bananas](https://lnkd.in/gCsaZ3hp)

### 🔹 𝗦𝘁𝗲𝗽 𝟯: 𝗔𝗱𝘃𝗮𝗻𝗰𝗲𝗱 – 𝗕𝗶𝗻𝗮𝗿𝘆 𝗦𝗲𝗮𝗿𝗰𝗵 𝗼𝗻 𝗔𝗻𝘀𝘄𝗲𝗿𝘀
Here, you’re not finding an index, but the optimal answer in a numeric or conceptual range (min/max resources, distance, capacity).
Hard LeetCode Problems:
1️⃣ [Median of Two Sorted Arrays](https://lnkd.in/g7dV4DcJ)
2️⃣ [Split Array Largest Sum](https://lnkd.in/gxjnTK7m)
3️⃣ [Aggressive Cows (GFG/LC variant)](https://lnkd.in/gqGF9KmH)
4️⃣ [Capacity to Ship Packages](https://lnkd.in/gNcxa9nx)
5️⃣ [K-th Smallest Pair Distance](https://lnkd.in/g4yAeSq8)

## 𝗧𝗵𝗲 𝗨𝗹𝘁𝗶𝗺𝗮𝘁𝗲 𝗖𝗣 𝗦𝘁𝗮𝗿𝘁𝗲𝗿 𝗣𝗮𝗰𝗸 🚀 | 𝗧𝗼𝗽 𝗧𝗼𝗽𝗶𝗰𝘀 + 𝗖𝗼𝗱𝗲𝗳𝗼𝗿𝗰es

If you’re just getting into Competitive Programming, here’s a structured list of must-know topics with 5 beginner-friendly Codeforces problems (800–1200) for each.

### 🔹 𝗔𝗿𝗿𝗮𝘆𝘀 & 𝗣𝗿𝗲𝗳𝗶𝘅 𝗦𝘂𝗺𝘀
https://lnkd.in/gcrZzUfE
https://lnkd.in/gRytXvws
https://lnkd.in/gE3CvGu4
https://lnkd.in/gtNiPiGu
https://lnkd.in/gdMxBrtK

### 🔹 𝗦𝘁𝗿𝗶𝗻𝗴𝘀 & 𝗖𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿 𝗙𝗿𝗲𝗾𝘂𝗲𝗻𝗰𝗶𝗲𝘀
https://lnkd.in/g-ZG4bDC
https://lnkd.in/g-K_edc5
https://lnkd.in/gBHKD255
https://lnkd.in/g6u6gQiQ
https://lnkd.in/gQ7K5hey

### 🔹 𝗚𝗿𝗲𝗲𝗱𝘆 𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵
https://lnkd.in/g_fqqr7W
https://lnkd.in/gf-s9699
https://lnkd.in/gcn-VBwC
https://lnkd.in/g_knaiWr
https://lnkd.in/gA7kEQHj

### 🔹 𝗠𝗮𝘁𝗵 & 𝗡𝘂𝗺𝗯𝗲𝗿 𝗧𝗵𝗲𝗼𝗿𝘆 𝗕𝗮𝘀𝗶𝗰𝘀
https://lnkd.in/geruwQGB
https://lnkd.in/ga_MGran
https://lnkd.in/gNX8_FDZ
https://lnkd.in/gvWuMFHZ
https://lnkd.in/gzVVVXpk

### 🔹 𝗕𝗶𝗻𝗮𝗿𝘆 𝗦𝗲𝗮𝗿𝗰𝗵 / 𝗦𝗼𝗿𝘁𝗶𝗻𝗴 𝗔𝗽𝗽𝗹𝗶𝗰𝗮𝘁𝗶𝗼𝗻𝘀
https://lnkd.in/gsP4T2xT
https://lnkd.in/gZErP8rP
https://lnkd.in/gqWAgUQD
https://lnkd.in/gp7adNww
https://lnkd.in/g6b7EptT