# 🚨 SecureCheck: Digital Police Check Post Registry  

<img width="1300" height="360" alt="image" src="https://github.com/user-attachments/assets/508b384a-3b33-405e-962d-a9bf61580dd9" />


# 🔐 SecureCheck: Smart Digital Police Check Post System

**SecureCheck** is a next-gen solution for police check post management,
built to replace traditional manual logs with a **SQL-powered backend**
and an interactive **Streamlit dashboard**.\
It brings **efficiency, security, and intelligence** into everyday check
post operations.

------------------------------------------------------------------------

## 🌍 Why SecureCheck?

Conventional record-keeping at check posts is error-prone and slow.
SecureCheck modernizes this by:\
- 📑 Maintaining all stop records in a **centralized MySQL database**.\
- 📈 Delivering **real-time analytics** with dynamic dashboards.\
- 🔮 Using **predictive insights** for violations and arrest outcomes.\
- 🕵️‍♂️ Enabling **pattern recognition** for law enforcement strategies.

------------------------------------------------------------------------

## 📊 Dataset Information

**File used:** `traffic_stops_with_vehicle_number.csv`

**Important Columns:**\
- Date & Time → `stop_date`, `stop_time`\
- Demographics → `driver_gender`, `driver_age`, `driver_race`\
- Stop Details → `violation_raw`, `violation`, `search_conducted`,
`stop_outcome`\
- Law Actions → `is_arrested`, `stop_duration`, `drugs_related_stop`\
- Vehicle Tracking → `vehicle_number`

------------------------------------------------------------------------

## 📂 Repository Layout

    ├── traffic_stops_with_vehicle_number.csv     # Raw dataset  
    ├── Data_Cleaning_SQL.ipynb                   # Cleaning + DB setup  
    ├── app.py                                    # Streamlit entry point  
    ├── home.py                                   # Dashboard home + stats  
    ├── basic_insights.py                         # Basic analytics & charts  
    ├── complex_insights.py                      # Trend detection + reports  
    ├── add_log.py                                # New log form + ML prediction  
    ├── db_utils.py                               # Database connection helpers  

------------------------------------------------------------------------

## 🖼️ Dashboard Highlights

### 🏠 Home Page

-   Overview with **key metrics**: total stops, searches, arrests,
    tickets\
-   Quick preview of live SQL data

### 📊 Basic Insights

-   Straightforward analytics from SQL queries\
-   Visualizations: bar charts, line graphs, data tables

### 🔍 Complex Insights

-   Advanced reports with **crime trends & deep analysis**\
-   Rich graphical summaries

### 📝 Add Log

-   Form for entering a **new stop record**\
-   Auto-predicts violation type and stop outcome\
-   Displays a confirmation summary

------------------------------------------------------------------------

## 🛠️ Tools & Frameworks

-   **Python** → backend + analytics\
-   **MySQL** → data storage\
-   **Pandas** → preprocessing\
-   **Plotly** → interactive visuals\
-   **Streamlit** → dashboard frontend

------------------------------------------------------------------------


🚨 **SecureCheck: Smarter, Faster & Safer Policing**

