# אפליקציית מטופלים – מרינה (v1)
- `data/<id>.json` – קובץ לכל מטופל. אחרי עדכון: `python3 build.py` → `hospice.html` (עצמאי, נתונים מוטמעים). לא לפרסם ברשת.
- אסור: ת"ז, טלפון, כתובת, שמות מטפלים/בני משפחה (רק תפקיד).
## Schema
id, initials, sex, age (int|null), program, visit_frequency, doctor, caregiver (תפקיד), diagnoses[], risk_factors[], function, meds[], next_focus[] (דגשים לביקור הבא),
visits[] {date YYYY-MM-DD, time, source, summary, fields{שם שדה: ערך}} – בסדר כרונולוגי, חדש אחרון; stats{} (שמור למגמות: pain, saturation, BP...),
missing[], discrepancies[].
סוכן מטופל: מוסיף visit בסוף, מעדכן next_focus/meds, מריץ build.py.

- אופציונלי: referral (טקסט הפניה), meds_printout[] (רשימת תרופות מתדפיס כללית להשוואה; מוצגת עם אזהרה).
- visit_frequency_days (int): מחשב 'ביקור הבא עד' מהביקור האחרון.
