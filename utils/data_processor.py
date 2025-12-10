import pandas as pd
import numpy as np

class DataProcessor:
    """Utility class for data processing operations"""
    
    @staticmethod
    def load_data(file, file_type='csv'):
        """Load data from file"""
        if file_type == 'csv':
            return pd.read_csv(file)
        elif file_type in ['xlsx', 'xls']:
            return pd.read_excel(file)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
    
    @staticmethod
    def handle_missing_values(df, method='drop'):
        """Handle missing values in dataframe"""
        if method == 'drop':
            return df.dropna()
        elif method == 'mean':
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
            return df
        elif method == 'median':
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
            return df
        elif method == 'mode':
            for col in df.columns:
                df[col].fillna(df[col].mode()[0], inplace=True)
            return df
        else:
            return df
    
    @staticmethod
    def remove_duplicates(df):
        """Remove duplicate rows"""
        return df.drop_duplicates()
    
    @staticmethod
    def filter_by_column(df, column, min_val=None, max_val=None):
        """Filter dataframe by column value range"""
        if min_val is not None and max_val is not None:
            return df[(df[column] >= min_val) & (df[column] <= max_val)]
        return df
    
    @staticmethod
    def get_data_info(df):
        """Get basic information about the dataframe"""
        return {
            'rows': len(df),
            'columns': len(df.columns),
            'missing_values': df.isnull().sum().sum(),
            'duplicates': df.duplicated().sum(),
            'numeric_columns': df.select_dtypes(include=[np.number]).columns.tolist(),
            'categorical_columns': df.select_dtypes(include=['object']).columns.tolist()
        }
