# 🚨 SecureCheck: Digital Police Check Post Registry  

<img width="1300" height="360" alt="image" src="https://github.com/user-attachments/assets/508b384a-3b33-405e-962d-a9bf61580dd9" />

SecureCheck is an advanced digital police check post registry system designed to modernize and secure check post operations through **real-time data analytics**, **centralized logging**, and **predictive insights**.  
It replaces inefficient manual systems with a robust **SQL-backed architecture** and a **Python-powered Streamlit dashboard**.  

---

## 📌 Overview  
Manual logging of vehicle checks often leads to inefficiencies and missed threats. **SecureCheck** addresses this by:  
- 📂 Providing a **centralized SQL database** for all police stop records.  
- 📊 Offering **real-time insights** through a Streamlit dashboard.  
- 🤖 Enabling **predictive analytics** for violations and outcomes.  
- 🕵️ Supporting **crime pattern analysis** for improved law enforcement coordination.  

---

## 🧾 Dataset  
**File:** `traffic_stops_with_vehicle_number.csv`  

**Columns include:**  
- stop_date, stop_time  
- country_name, driver_gender, driver_age_raw, driver_age, driver_race  
- violation_raw, violation, search_conducted, search_type  
- stop_outcome, is_arrested, stop_duration, drugs_related_stop  
- vehicle_number  

---

## 📁 Project Structure  

```
├── traffic_stops_with_vehicle_number.csv     # Dataset  
├── data_prep_and_sql_initial.ipynb           # Data cleaning & SQL DB setup  
├── app.py                                    # Streamlit app launcher  
├── home.py                                   # Home page with metrics & data preview  
├── fundamental_insights.py                   # Basic insights (tables + charts)  
├── profound_insights.py                      # Advanced analytics (tables + charts)  
├── add_log.py                                # Add new log + prediction logic  
├── db_utils.py                               # MySQL database connection handler  
```

---

## 🖥️ Streamlit Dashboard Pages  

### 🏠 Home  
- Project introduction and **dashboard metrics**:  
  - Total Police Stops  
  - Searches Conducted  
  - Arrests Made  
  - Tickets Issued  
- Live data preview  

### 💡 Fundamental Insights  
- Core statistics and visuals from SQL queries  
- Tables and visualizations (bar charts, line graphs, etc.)  

### 🧠 Profound Insights  
- Advanced analytics and **trend detection**  
- Crime pattern analysis with visual reports  

### 📝 Add New Police Log  
- Form to add a **new police stop entry**  
- Predicts:  
  - Violation Type  
  - Stop Outcome  
- Displays a summary of the new entry  

---

## ⚙️ Tech Stack  
- **Python** – Data processing & app backend  
- **MySQL** – Centralized database  
- **Pandas** – Data manipulation  
- **Plotly** – Data visualization  
- **Streamlit** – Interactive dashboard frontend  

---

## 🚀 Getting Started  

### 1. Clone the Repository  
```bash
git clone https://github.com/SamuIdhayanI/SecureCheck.git
cd SecureCheck
```

### 2. Set Up Environment  
```bash
pip install -r requirements.txt
```

### 3. Initialize Database  
Run the Jupyter notebook:  
- Clean the dataset  
- Create MySQL tables  
- Insert cleaned data  

```bash
jupyter notebook data_prep_and_sql_initial.ipynb
```

### 4. Launch the App  
```bash
streamlit run app.py
```
 

