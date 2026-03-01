import sqlite3

def init_database():
    conn = sqlite3.connect('ayurveda.db')
    cursor = conn.cursor()
    
    # Create dosha_data table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dosha_data (
            id INTEGER PRIMARY KEY,
            symptom TEXT NOT NULL,
            dosha TEXT NOT NULL
        )
    ''')
    
    # Create herb_interactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS herb_interactions (
            id INTEGER PRIMARY KEY,
            herb TEXT NOT NULL,
            medicine TEXT NOT NULL,
            risk TEXT NOT NULL
        )
    ''')
    
    # Create seasonal_rules table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS seasonal_rules (
            id INTEGER PRIMARY KEY,
            season TEXT NOT NULL,
            risk_dosha TEXT NOT NULL,
            advice TEXT NOT NULL
        )
    ''')
    
    # Create product_verification table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product_verification (
            id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            ayush_certified TEXT NOT NULL,
            batch_number TEXT NOT NULL
        )
    ''')
    
    # Insert sample data
    cursor.execute("INSERT INTO dosha_data (symptom, dosha) VALUES (?, ?)", ("Anxiety", "Vata"))
    cursor.execute("INSERT INTO herb_interactions (herb, medicine, risk) VALUES (?, ?, ?)", ("Turmeric", "Warfarin", "High"))
    cursor.execute("INSERT INTO seasonal_rules (season, risk_dosha, advice) VALUES (?, ?, ?)", ("Summer", "Pitta", "Avoid heat exposure"))
    cursor.execute("INSERT INTO product_verification (product_name, ayush_certified, batch_number) VALUES (?, ?, ?)", ("Ashwagandha", "Yes", "AB123"))
    
    conn.commit()
    conn.close()
    print("Database initialized!")

if __name__ == "__main__":
    init_database()