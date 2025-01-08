import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Amazing Dashboard",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
    }
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("✨ Navigation")
page = st.sidebar.selectbox(
    "Choose a page",
    ["Dashboard", "Data Analysis", "Interactive Demo"]
)

# Main content
st.title("✨ Amazing Streamlit App")
st.markdown("---")

if page == "Dashboard":
    # Create three columns
    col1, col2, col3 = st.columns(3)
    
    # Metrics
    with col1:
        st.metric(
            label="Revenue",
            value="$12,345",
            delta="$1,234"
        )
    with col2:
        st.metric(
            label="Users",
            value="1,234",
            delta="123"
        )
    with col3:
        st.metric(
            label="Conversion",
            value="12.3%",
            delta="1.2%"
        )
    
    # Generate sample data
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    data = pd.DataFrame({
        'Date': dates,
        'Value': np.random.normal(100, 15, len(dates)),
        'Category': np.random.choice(['A', 'B', 'C'], len(dates))
    })
    
    # Interactive chart
    st.subheader("📈 Interactive Chart")
    chart_type = st.selectbox(
        "Select chart type",
        ["Line", "Bar", "Area"]
    )
    
    if chart_type == "Line":
        fig = px.line(data, x='Date', y='Value', color='Category')
    elif chart_type == "Bar":
        fig = px.bar(data, x='Date', y='Value', color='Category')
    else:
        fig = px.area(data, x='Date', y='Value', color='Category')
    
    fig.update_layout(
        template="plotly_white",
        height=500,
    )
    st.plotly_chart(fig, use_container_width=True)

elif page == "Data Analysis":
    st.subheader("📊 Data Analysis")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Data Preview")
        st.dataframe(df.head())
        
        st.write("### Data Statistics")
        st.write(df.describe())
        
        # Column selection for visualization
        if len(df.columns) > 1:
            x_col = st.selectbox("Select X axis", df.columns)
            y_col = st.selectbox("Select Y axis", df.columns)
            
            fig = px.scatter(df, x=x_col, y=y_col)
            st.plotly_chart(fig, use_container_width=True)

elif page == "Interactive Demo":
    st.subheader("🎮 Interactive Demo")
    
    # Input widgets
    name = st.text_input("What's your name?")
    color = st.color_picker("Pick your favorite color")
    number = st.slider("Pick a number", 0, 100)
    
    # Button with custom styling
    if st.button("Generate"):
        if name:
            st.balloons()
            st.markdown(f"""
                ### Hello, {name}! 
                Your favorite color is {color} and you picked the number {number}.
                
                Here's a custom visualization just for you:
            """)
            
            # Generate custom visualization
            fig = px.scatter(
                np.random.randn(number, 2),
                color_discrete_sequence=[color]
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Please enter your name first!")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        Made with ❤️ using Streamlit
        <br>
        Current time: {}
    </div>
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    unsafe_allow_html=True
)