import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.data_processor import DataProcessor
from utils.chart_generator import ChartGenerator
from utils.statistics import StatisticsCalculator

# Page configuration
st.set_page_config(
    page_title="Data Visualization Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stButton>button {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📊 Interactive Data Visualization Dashboard")
st.markdown("Upload your data and create beautiful visualizations with statistical insights")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # File upload
    uploaded_file = st.file_uploader(
        "Upload your data file",
        type=['csv', 'xlsx', 'xls'],
        help="Supported formats: CSV, Excel"
    )
    
    if uploaded_file:
        st.success("✅ File uploaded successfully!")
        
        # Chart type selection
        st.subheader("📈 Chart Type")
        chart_type = st.selectbox(
            "Select visualization",
            ["Line Chart", "Bar Chart", "Pie Chart", "Scatter Plot", 
             "Histogram", "Heatmap", "Box Plot"]
        )
        
        # Color scheme
        st.subheader("🎨 Appearance")
        color_scheme = st.selectbox(
            "Color scheme",
            ["Plotly", "Viridis", "Cividis", "Blues", "Reds", "Greens"]
        )

# Main content
if uploaded_file is not None:
    # Load data
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        # Create tabs
        tab1, tab2, tab3, tab4 = st.tabs([
            "📊 Data Preview", 
            "📈 Visualizations", 
            "📉 Statistics", 
            "🔧 Data Processing"
        ])
        
        # Tab 1: Data Preview
        with tab1:
            st.subheader("Data Preview")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Rows", len(df))
            with col2:
                st.metric("Total Columns", len(df.columns))
            with col3:
                st.metric("Missing Values", df.isnull().sum().sum())
            with col4:
                st.metric("Duplicates", df.duplicated().sum())
            
            st.dataframe(df.head(100), use_container_width=True)
            
            # Download button
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                "📥 Download Data as CSV",
                csv,
                "filtered_data.csv",
                "text/csv",
                key='download-csv'
            )
        
        # Tab 2: Visualizations
        with tab2:
            st.subheader("Interactive Visualizations")
            
            # Column selection
            numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
            
            if chart_type == "Line Chart":
                col1, col2 = st.columns(2)
                with col1:
                    x_col = st.selectbox("X-axis", df.columns)
                with col2:
                    y_col = st.selectbox("Y-axis", numeric_cols)
                
                fig = px.line(df, x=x_col, y=y_col, 
                             title=f"{y_col} over {x_col}",
                             color_discrete_sequence=px.colors.qualitative.Set2)
                st.plotly_chart(fig, use_container_width=True)
            
            elif chart_type == "Bar Chart":
                col1, col2 = st.columns(2)
                with col1:
                    x_col = st.selectbox("X-axis", df.columns)
                with col2:
                    y_col = st.selectbox("Y-axis", numeric_cols)
                
                fig = px.bar(df, x=x_col, y=y_col,
                            title=f"{y_col} by {x_col}",
                            color_discrete_sequence=px.colors.qualitative.Pastel)
                st.plotly_chart(fig, use_container_width=True)
            
            elif chart_type == "Pie Chart":
                col1, col2 = st.columns(2)
                with col1:
                    names_col = st.selectbox("Categories", categorical_cols)
                with col2:
                    values_col = st.selectbox("Values", numeric_cols)
                
                fig = px.pie(df, names=names_col, values=values_col,
                            title=f"Distribution of {values_col}")
                st.plotly_chart(fig, use_container_width=True)
            
            elif chart_type == "Scatter Plot":
                col1, col2, col3 = st.columns(3)
                with col1:
                    x_col = st.selectbox("X-axis", numeric_cols)
                with col2:
                    y_col = st.selectbox("Y-axis", numeric_cols)
                with col3:
                    color_col = st.selectbox("Color by", [None] + categorical_cols)
                
                fig = px.scatter(df, x=x_col, y=y_col, color=color_col,
                               title=f"{y_col} vs {x_col}")
                st.plotly_chart(fig, use_container_width=True)
            
            elif chart_type == "Histogram":
                col = st.selectbox("Select column", numeric_cols)
                bins = st.slider("Number of bins", 10, 100, 30)
                
                fig = px.histogram(df, x=col, nbins=bins,
                                 title=f"Distribution of {col}")
                st.plotly_chart(fig, use_container_width=True)
            
            elif chart_type == "Heatmap":
                corr_matrix = df[numeric_cols].corr()
                fig = px.imshow(corr_matrix, 
                              text_auto=True,
                              title="Correlation Heatmap",
                              color_continuous_scale='RdBu_r')
                st.plotly_chart(fig, use_container_width=True)
            
            elif chart_type == "Box Plot":
                col1, col2 = st.columns(2)
                with col1:
                    y_col = st.selectbox("Y-axis", numeric_cols)
                with col2:
                    x_col = st.selectbox("Group by", [None] + categorical_cols)
                
                fig = px.box(df, x=x_col, y=y_col,
                           title=f"Box Plot of {y_col}")
                st.plotly_chart(fig, use_container_width=True)
        
        # Tab 3: Statistics
        with tab3:
            st.subheader("Statistical Analysis")
            
            # Descriptive statistics
            st.write("### Descriptive Statistics")
            st.dataframe(df.describe(), use_container_width=True)
            
            # Correlation matrix
            if len(numeric_cols) > 1:
                st.write("### Correlation Matrix")
                corr = df[numeric_cols].corr()
                st.dataframe(corr, use_container_width=True)
            
            # Missing values
            st.write("### Missing Values")
            missing = pd.DataFrame({
                'Column': df.columns,
                'Missing Count': df.isnull().sum(),
                'Percentage': (df.isnull().sum() / len(df) * 100).round(2)
            })
            st.dataframe(missing, use_container_width=True)
        
        # Tab 4: Data Processing
        with tab4:
            st.subheader("Data Processing Tools")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("### Handle Missing Values")
                if st.button("Drop Missing Values"):
                    df = df.dropna()
                    st.success("Missing values removed!")
                
                if st.button("Fill with Mean"):
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.success("Missing values filled with mean!")
            
            with col2:
                st.write("### Remove Duplicates")
                if st.button("Remove Duplicate Rows"):
                    df = df.drop_duplicates()
                    st.success("Duplicates removed!")
            
            st.write("### Filter Data")
            filter_col = st.selectbox("Select column to filter", df.columns)
            
            if df[filter_col].dtype in ['int64', 'float64']:
                min_val = float(df[filter_col].min())
                max_val = float(df[filter_col].max())
                filter_range = st.slider(
                    f"Select range for {filter_col}",
                    min_val, max_val, (min_val, max_val)
                )
                df = df[(df[filter_col] >= filter_range[0]) & 
                       (df[filter_col] <= filter_range[1])]
            
            st.dataframe(df.head(50), use_container_width=True)
    
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")

else:
    # Welcome screen
    st.info("👆 Upload a CSV or Excel file to get started!")
    
    st.markdown("""
    ### 🎯 Features
    - 📊 Multiple chart types (Line, Bar, Pie, Scatter, etc.)
    - 📈 Statistical analysis and insights
    - 🔧 Data cleaning and preprocessing
    - 📥 Export visualizations and data
    - 🎨 Customizable color schemes
    
    ### 📁 Supported File Formats
    - CSV (.csv)
    - Excel (.xlsx, .xls)
    
    ### 🚀 Quick Start
    1. Upload your data file
    2. Select visualization type
    3. Choose columns to visualize
    4. Explore statistics and insights
    """)
