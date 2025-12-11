import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

class ChartGenerator:
    """Utility class for generating various chart types"""
    
    @staticmethod
    def create_line_chart(df, x_col, y_col, title="Line Chart"):
        """Create a line chart"""
        fig = px.line(df, x=x_col, y=y_col, title=title)
        fig.update_layout(
            xaxis_title=x_col,
            yaxis_title=y_col,
            hovermode='x unified'
        )
        return fig
    
    @staticmethod
    def create_bar_chart(df, x_col, y_col, title="Bar Chart"):
        """Create a bar chart"""
        fig = px.bar(df, x=x_col, y=y_col, title=title)
        fig.update_layout(
            xaxis_title=x_col,
            yaxis_title=y_col
        )
        return fig
    
    @staticmethod
    def create_pie_chart(df, names_col, values_col, title="Pie Chart"):
        """Create a pie chart"""
        fig = px.pie(df, names=names_col, values=values_col, title=title)
        return fig
    
    @staticmethod
    def create_scatter_plot(df, x_col, y_col, title="Scatter Plot"):
        """Create a scatter plot"""
        fig = px.scatter(df, x=x_col, y=y_col, title=title)
        fig.update_layout(
            xaxis_title=x_col,
            yaxis_title=y_col
        )
        return fig
    
    @staticmethod
    def create_histogram(df, col, title="Histogram"):
        """Create a histogram"""
        fig = px.histogram(df, x=col, title=title)
        fig.update_layout(
            xaxis_title=col,
            yaxis_title="Frequency"
        )
        return fig
    
    @staticmethod
    def create_box_plot(df, col, title="Box Plot"):
        """Create a box plot"""
        fig = px.box(df, y=col, title=title)
        fig.update_layout(yaxis_title=col)
        return fig
    
    @staticmethod
    def create_heatmap(df, title="Correlation Heatmap"):
        """Create a correlation heatmap"""
        numeric_df = df.select_dtypes(include=['number'])
        corr_matrix = numeric_df.corr()
        
        fig = go.Figure(data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale='RdBu',
            zmid=0
        ))
        
        fig.update_layout(
            title=title,
            xaxis_title="Features",
            yaxis_title="Features"
        )
        return fig
    
    @staticmethod
    def create_area_chart(df, x_col, y_col, title="Area Chart"):
        """Create an area chart"""
        fig = px.area(df, x=x_col, y=y_col, title=title)
        fig.update_layout(
            xaxis_title=x_col,
            yaxis_title=y_col
        )
        return fig
