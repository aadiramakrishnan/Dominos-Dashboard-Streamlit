import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load your data
@st.cache_data
def load_data():
    df = pd.read_csv("Dominos_Full_Example.csv")
    
    # Convert "Yes" and "No" to binary values
    binary_columns = ["Delivered On Time", "Predicted Delivered On Time"]
    for col in binary_columns:
        df[col] = df[col].map({"Yes": 1, "No": 0})
    
    return df

df = load_data()

# Title
st.title("Domino's Delivery Performance Dashboard")

# Sidebar for filters
st.sidebar.header("Filters")
test_phase = st.sidebar.multiselect("Select Test Phase", df["Test Phase"].unique())
store_location = st.sidebar.multiselect("Select Store Location", df["Store Location"].unique())
order_type = st.sidebar.multiselect("Select Order Type", df["Order Type"].unique())

# Apply filters
if test_phase:
    df = df[df["Test Phase"].isin(test_phase)]
if store_location:
    df = df[df["Store Location"].isin(store_location)]
if order_type:
    df = df[df["Order Type"].isin(order_type)]

# 1. On-Time Delivery Performance Comparison
st.header("On-Time Delivery Performance Comparison")

try:
    # Check if 'Test Phase' and 'Delivered On Time' columns exist
    if 'Test Phase' not in df.columns or 'Delivered On Time' not in df.columns:
        st.error("Required columns 'Test Phase' or 'Delivered On Time' are missing from the dataset.")
    else:
        # Perform the groupby operation
        grouped_data = df.groupby("Test Phase")["Delivered On Time"].mean().reset_index()
        
        # Create the bar chart
        fig_ontime = px.bar(grouped_data, x="Test Phase", y="Delivered On Time", 
                            title="On-Time Delivery Rate by Test Phase")
        st.plotly_chart(fig_ontime)

except Exception as e:
    st.error(f"An error occurred while creating the On-Time Delivery Performance chart: {str(e)}")
    st.write("DataFrame info:")
    st.write(df.info())
    st.write("First few rows of the DataFrame:")
    st.write(df.head())

# 2. Actual vs Predicted On-Time Delivery Comparison
st.header("Actual vs Predicted On-Time Delivery Comparison")
try:
    fig_comparison = go.Figure()
    for phase in df['Test Phase'].unique():
        df_phase = df[df['Test Phase'] == phase]
        fig_comparison.add_trace(go.Bar(x=['Actual', 'Predicted'], 
                                        y=[df_phase['Delivered On Time'].mean(), 
                                           df_phase['Predicted Delivered On Time'].mean()],
                                        name=phase))
    fig_comparison.update_layout(barmode='group', title='Actual vs Predicted On-Time Delivery Rate by Test Phase')
    st.plotly_chart(fig_comparison)
except Exception as e:
    st.error(f"An error occurred while creating the Actual vs Predicted comparison: {str(e)}")

# 3. Model Prediction Accuracy
st.header("Model Prediction Accuracy")
try:
    df['Correct_Prediction'] = df['Delivered On Time'] == df['Predicted Delivered On Time']
    fig_accuracy = px.bar(df.groupby("Test Phase")["Correct_Prediction"].mean().reset_index(), 
                          x="Test Phase", y="Correct_Prediction", 
                          title="Model Accuracy by Test Phase")
    st.plotly_chart(fig_accuracy)
except Exception as e:
    st.error(f"An error occurred while creating the Model Prediction Accuracy chart: {str(e)}")

# 4. On-Time Delivery Improvement
st.header("On-Time Delivery Improvement")
try:
    pre_test_rate = df[df["Test Phase"] == "Pre-Test"]["Delivered On Time"].mean()
    post_test_rate = df[df["Test Phase"] == "Post-Test"]["Delivered On Time"].mean()
    improvement = post_test_rate - pre_test_rate
    st.metric("On-Time Delivery Improvement", f"{improvement:.2%}")
except Exception as e:
    st.error(f"An error occurred while calculating On-Time Delivery Improvement: {str(e)}")

# 5. Correlation with Key Variables
st.header("Correlation with Key Variables")
try:
    corr_vars = ["Delivered On Time", "Predicted Delivered On Time", "Delivery Distance (miles)", "Order Size", "Total Dollars"]
    corr_matrix = df[corr_vars].corr()
    fig_corr = px.imshow(corr_matrix, text_auto=True, aspect="auto")
    st.plotly_chart(fig_corr)
except Exception as e:
    st.error(f"An error occurred while creating the Correlation Matrix: {str(e)}")

# 6. Impact of Key Variables on On-Time Delivery
st.header("Impact of Key Variables on On-Time Delivery")
key_vars = ["Delivery Distance (miles)", "Order Size", "Total Dollars"]
for var in key_vars:
    try:
        fig = px.scatter(df, x=var, y="Delivered On Time", 
                         color="Test Phase", trendline="ols", 
                         title=f"Impact of {var} on On-Time Delivery")
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"An error occurred while creating the Impact chart for {var}: {str(e)}")

# 7. Changes in Key Variables from Pre-Test to Post-Test
st.header("Changes in Key Variables from Pre-Test to Post-Test")
for var in key_vars:
    try:
        pre_mean = df[df["Test Phase"] == "Pre-Test"][var].mean()
        post_mean = df[df["Test Phase"] == "Post-Test"][var].mean()
        change = (post_mean - pre_mean) / pre_mean
        st.metric(f"Change in {var}", f"{change:.2%}")
    except Exception as e:
        st.error(f"An error occurred while calculating change for {var}: {str(e)}")

# 8. On-Time Performance by Store and Order Type
st.header("On-Time Performance by Store and Order Type")
try:
    fig_heatmap = px.density_heatmap(df, x="Order Type", y="Store Location", z="Delivered On Time", 
                                     histfunc="avg", title="On-Time Delivery Rate by Store and Order Type")
    st.plotly_chart(fig_heatmap)
except Exception as e:
    st.error(f"An error occurred while creating the On-Time Performance heatmap: {str(e)}")