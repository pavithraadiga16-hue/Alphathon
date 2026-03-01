import sqlite3

# Connect to local database file
conn = sqlite3.connect("ayurveda.db")
cursor = conn.cursor()

# -----------------------------
# 1. DOSHA TABLE
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS dosha_conditions (
    dosha TEXT,
    symptom TEXT
)
""")

dosha_data = [
    ("Vata", "Dry skin"),
    ("Vata", "Anxiety"),
    ("Vata", "Constipation"),
    ("Vata", "Insomnia"),
    ("Pitta", "Acidity"),
    ("Pitta", "Skin rashes"),
    ("Pitta", "Anger"),
    ("Pitta", "Excess sweating"),
    ("Kapha", "Weight gain"),
    ("Kapha", "Lethargy"),
    ("Kapha", "Cold and cough"),
    ("Kapha", "Depression")
]

cursor.executemany("INSERT INTO dosha_conditions VALUES (?,?)", dosha_data)

# -----------------------------
# 2. SEASONAL RULES TABLE
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS seasonal_rules (
    season TEXT,
    risk_dosha TEXT,
    advice TEXT
)
""")

season_data = [
    ("Summer", "Pitta", "Avoid spicy food, drink coconut water"),
    ("Winter", "Vata", "Eat warm food, oil massage"),
    ("Spring", "Kapha", "Exercise daily, avoid dairy"),
    ("Monsoon", "Vata", "Eat light warm meals")
]

cursor.executemany("INSERT INTO seasonal_rules VALUES (?,?,?)", season_data)

# -----------------------------
# 3. HERB INTERACTIONS TABLE
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS herb_interactions (
    herb TEXT,
    medicine TEXT,
    risk TEXT
)
""")

herb_data = [
    ("Ashwagandha", "Antidepressants", "Excess sedation risk"),
    ("Turmeric", "Blood thinners", "Bleeding risk"),
    ("Ginseng", "BP medication", "Blood pressure fluctuation"),
    ("Triphala", "Diarrhea medicine", "Over-laxative effect")
]

cursor.executemany("INSERT INTO herb_interactions VALUES (?,?,?)", herb_data)

# -----------------------------
# 4. PRODUCT VERIFICATION TABLE
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS product_verification (
    product_name TEXT,
    ayush_certified TEXT,
    batch_number TEXT
)
""")

product_data = [
    ("Organic Ashwagandha Oil", "Yes", "BATCH101"),
    ("Pure Turmeric Powder", "Yes", "BATCH202"),
    ("Unknown Herbal Mix", "No", "NULL")
]

cursor.executemany("INSERT INTO product_verification VALUES (?,?,?)", product_data)

conn.commit()

print("🌿 Ayurvedic Local Database Created Successfully!")

conn.close()
