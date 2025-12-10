# 📊 Interactive Data Visualization Dashboard

A powerful Python-based data visualization dashboard for analyzing and visualizing data from CSV/Excel files with interactive charts, statistical analysis, and export capabilities.

## ✨ Features

- **File Upload** - Support for CSV, Excel (XLSX, XLS)
- **Multiple Chart Types** - Line, Bar, Pie, Scatter, Histogram, Heatmap
- **Statistical Analysis** - Mean, Median, Mode, Standard Deviation, Correlation
- **Data Filtering** - Filter by columns, date ranges, values
- **Interactive Charts** - Zoom, pan, hover tooltips
- **Export Reports** - PDF, PNG, HTML
- **Data Cleaning** - Handle missing values, duplicates
- **Real-time Updates** - Dynamic chart updates
- **Responsive Design** - Works on all screen sizes

## 🛠️ Tech Stack

- Python 3.10+
- Streamlit (Web Framework)
- Pandas (Data Manipulation)
- Plotly (Interactive Charts)
- Matplotlib & Seaborn (Static Charts)
- NumPy (Numerical Computing)
- SciPy (Statistical Analysis)

## 🚀 Installation

```bash
# Clone repository
git clone https://github.com/Keshavja29/data-visualization-dashboard.git
cd data-visualization-dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

Application runs on: `http://localhost:8501`

## 📊 Supported Chart Types

### 1. Line Chart
- Time series data
- Trend analysis
- Multiple lines comparison

### 2. Bar Chart
- Category comparison
- Horizontal/Vertical bars
- Grouped/Stacked bars

### 3. Pie Chart
- Percentage distribution
- Category breakdown
- Donut charts

### 4. Scatter Plot
- Correlation analysis
- Relationship between variables
- Bubble charts

### 5. Histogram
- Data distribution
- Frequency analysis
- Bin customization

### 6. Heatmap
- Correlation matrix
- Pattern detection
- Color-coded values

### 7. Box Plot
- Outlier detection
- Quartile analysis
- Distribution comparison

## 📈 Statistical Features

### Descriptive Statistics
- Count, Mean, Median, Mode
- Standard Deviation, Variance
- Min, Max, Range
- Quartiles (Q1, Q2, Q3)
- Skewness, Kurtosis

### Correlation Analysis
- Pearson correlation
- Spearman correlation
- Correlation matrix
- Heatmap visualization

### Data Quality
- Missing value detection
- Duplicate identification
- Data type analysis
- Outlier detection

## 🎯 Use Cases

### Business Analytics
- Sales trend analysis
- Revenue forecasting
- Customer segmentation
- Performance metrics

### Data Science
- Exploratory Data Analysis (EDA)
- Feature correlation
- Distribution analysis
- Hypothesis testing

### Academic Research
- Statistical analysis
- Data presentation
- Report generation
- Visualization for papers

## 📁 Sample Datasets Included

- Sales data (sales.csv)
- Customer data (customers.csv)
- Stock prices (stocks.csv)
- Weather data (weather.csv)

## 🔧 Features Breakdown

### Data Upload
```python
# Supported formats
- CSV (.csv)
- Excel (.xlsx, .xls)
- JSON (.json)
```

### Data Preprocessing
- Handle missing values (drop, fill, interpolate)
- Remove duplicates
- Data type conversion
- Column renaming
- Filter rows/columns

### Visualization Options
- Chart title customization
- Axis labels
- Color schemes
- Legend position
- Grid lines
- Annotations

### Export Options
- Download charts as PNG/PDF
- Export filtered data as CSV
- Generate HTML reports
- Save analysis results

## 🌐 Deployment

### Deploy on Streamlit Cloud

1. Push code to GitHub
2. Visit: https://streamlit.io/cloud
3. Connect GitHub repository
4. Deploy with one click

### Deploy on Heroku

```bash
# Create Procfile
echo "web: streamlit run app.py --server.port=$PORT" > Procfile

# Deploy
heroku create
git push heroku main
```

## 📸 Screenshots

[Add screenshots here]

## 🔮 Future Enhancements

- Machine Learning predictions
- Real-time data streaming
- Database connectivity (SQL, MongoDB)
- Advanced statistical tests
- Custom dashboard templates
- Collaborative features
- API integration
- Automated reporting

## 📚 Documentation

Detailed documentation available in `/docs` folder:
- User Guide
- API Reference
- Chart Examples
- Statistical Methods

## 📄 License

MIT License
