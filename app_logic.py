import sqlite3

def check_dosha(symptom):
    conn = sqlite3.connect("ayurveda.db")
    cursor = conn.cursor()

    cursor.execute("SELECT dosha FROM dosha_data WHERE symptom=?", (symptom,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return f"⚠ Imbalance detected in: {result[0]}"
    else:
        return "✅ No dosha imbalance found"


def check_herb_interaction(herb, medicine):
    conn = sqlite3.connect("ayurveda.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT risk FROM herb_interactions 
    WHERE herb=? AND medicine=?
    """, (herb, medicine))

    result = cursor.fetchone()
    conn.close()

    if result:
        return f"⚠ Risk Alert: {result[0]}"
    else:
        return "✅ No known interaction"


def check_season(season):
    conn = sqlite3.connect("ayurveda.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT risk_dosha, advice FROM seasonal_rules
    WHERE season=?
    """, (season,))

    result = cursor.fetchone()
    conn.close()

    if result:
        return f"⚠ {result[0]} may increase. Advice: {result[1]}"
    else:
        return "Season not found"


def verify_product(product):
    conn = sqlite3.connect("ayurveda.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT ayush_certified, batch_number 
    FROM product_verification
    WHERE product_name=?
    """, (product,))

    result = cursor.fetchone()
    conn.close()

    if result:
        if result[0] == "Yes":
            return "✅ Product is AYUSH Certified"
        else:
            return "⚠ Product not certified!"
    else:
        return "Product not found"
