import pandas as pd
import numpy as np
from scipy import stats

class StatisticsCalculator:
    """Utility class for statistical calculations"""
    
    @staticmethod
    def descriptive_stats(df, column):
        """Calculate descriptive statistics for a column"""
        return {
            'count': df[column].count(),
            'mean': df[column].mean(),
            'median': df[column].median(),
            'mode': df[column].mode()[0] if len(df[column].mode()) > 0 else None,
            'std': df[column].std(),
            'var': df[column].var(),
            'min': df[column].min(),
            'max': df[column].max(),
            'range': df[column].max() - df[column].min(),
            'q1': df[column].quantile(0.25),
            'q2': df[column].quantile(0.50),
            'q3': df[column].quantile(0.75),
            'iqr': df[column].quantile(0.75) - df[column].quantile(0.25),
            'skewness': df[column].skew(),
            'kurtosis': df[column].kurtosis()
        }
    
    @staticmethod
    def correlation_matrix(df):
        """Calculate correlation matrix for numeric columns"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        return df[numeric_cols].corr()
    
    @staticmethod
    def detect_outliers(df, column, method='iqr'):
        """Detect outliers in a column"""
        if method == 'iqr':
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
            return outliers
        elif method == 'zscore':
            z_scores = np.abs(stats.zscore(df[column].dropna()))
            outliers = df[z_scores > 3]
            return outliers
        else:
            return pd.DataFrame()
    
    @staticmethod
    def missing_value_analysis(df):
        """Analyze missing values in dataframe"""
        missing_data = pd.DataFrame({
            'Column': df.columns,
            'Missing_Count': df.isnull().sum(),
            'Percentage': (df.isnull().sum() / len(df) * 100).round(2)
        })
        return missing_data[missing_data['Missing_Count'] > 0].sort_values(
            'Missing_Count', ascending=False
        )
