import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# streamlit app for Interest and amount of money :...
st.set_page_config(
    page_title="SMIC Bill Generator",
    page_icon="smart.jpg"
)
st.title("Interest 📈 and Amount of 💰 Money Analysis")
# adding header and colors to my name 
st.markdown(
    """
    <p1 style='text-align: center; color: #4CAF50;'>
        Created by Sahil Kasana    
    </p1>
    """,
    unsafe_allow_html=True)
# adding description
st.markdown("""
 welcome to the Interest and Amount of Money Analysis app!
            """)


# adding advertisement
st.write("Our associate patner for this app ")
col1, col2 = st.columns(2)
col1.image("mpl_img.png", width=250, caption="https://mpl2025.streamlit.app/")
col2.image("library_banner.jpg", width = 300 , caption="Shree Dev narayan library, Kotputli")

st.warning("This app is based on monthly compound interest calculation ")
def interest_calculator(principle,rate,time):
    # here pricile is get updated every month
    for i in range(time):
        total_interest = 0  
        interest = (principle * rate * 1)/100
        principle += interest
        total_interest += interest 

    total_amount = principle  
    return total_amount


# input data in form submit button
st.subheader("Input Data")
principle = st.number_input("Enter the principle amount:", min_value=0.0, value=10000.0, step=100.0)
rate = st.number_input("Enter the interest rate (%):", min_value=0.0, value=2.0, step=0.1)
time_years =st.slider("Select the time (years):", min_value=0, max_value=30, value=1, step=1)
time_monnths = st.slider("Enter the time (months):", min_value=0,max_value=11, value=0, step=1)
time = time_years * 12 + time_monnths

if st.button("Calculate Interest"):
    total_amount = interest_calculator(principle, rate, time)
    st.success(f"Total amount after {time_years} years and {time_monnths} months is: ₹{total_amount:,.2f}")
    st.success(f"Total interest earned is: ₹{total_amount - principle:,.2f}")


st.subheader("Use our smart bill generator to generate bill 🧾 ")


# adding page logo 
st.image("smart.jpg", width=300)
st.subheader("Generate bill")

st.write("Please fill in the details below to generate a bill 🧾:")

L_name = st.text_input("Enter 👨‍💼 Lenders Name")
B_name = st.text_input("Enter 👨‍💼 Borrowers Name")
G_date = st.date_input("Enter Date 📅 when money given to borrower")
total_amount = round(interest_calculator(principle, rate, time), 2)

bill_date = pd.to_datetime("today").date()
df = ({
        "Lender Name": [L_name],
        "Bill Date": [bill_date],
        "Borrower Name": [B_name],
        "Date of loan": [G_date],
        "Principle Amount": [principle],
        "Interest Rate (%)": [rate],
        "Time (Years and months)": [f"{time_years} years and {time_monnths} months"],
        "Total Interest Earned": [round((total_amount - principle),2)],
        "Total Amount": [total_amount]
    })

# adding label to df
df = pd.DataFrame(df)
# adding label to df



if st.button("Generate Bill"):
    st.dataframe(df.T)
    st.success("Bill generated successfully!")

# Adding a sidebar with developer information
st.sidebar.title("Meet the Developer")
col1, col2 = st.sidebar.columns(2)
col1.image("sahil.jpg", width=100, caption="Er. Sahil Kasana")
col2.image("smart.jpg", width=100, caption="Smart Bill Generator")


st.sidebar.write("scan QR code to connect with me")
st.sidebar.image("linkedin_qr.png", caption="scan me",width=200)

st.sidebar.write("Contact Information:")
st.sidebar.write("Devnarayan Library, Kotputli :  Manoj Gurjar  8740880179")
st.sidebar.write("LinkedIn: [Sahil Kasana](https://www.linkedin.com/in/sahil-kasana6055/)")
st.sidebar.write("Email:sagurjar027@gmail.com")




# 
st.subheader("Click below for detailed analysis of interest and amount of money 💰📈")
st.write("Visualize the interest and total amount over time with detailed analysis with the help of graphs and charts.")



if st.button("Show detailed analysis"):
    # Generate data for analysis
    months = np.arange(1, time + 1)
    amounts = [interest_calculator(principle, rate, m) for m in months]
    interest = [amounts[i] - principle for i in range(len(amounts))]
    # Create a DataFrame for plotting
    df = pd.DataFrame({
        'Month': months,
        'Interst': interest,
        'Total Amount': amounts
    })
    st.dataframe(df)

    # Plotting the data
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='Month', y='Total Amount', marker='o')
    plt.title('Total Amount Over Time')
    plt.xlabel('Months')
    plt.ylabel('Total Amount (₹)')
    plt.grid(True)
    
    st.pyplot(plt)
    # Plotting interest earned and priciple using pie chart
    plt.figure(figsize=(8, 6))
    plt.pie([df['Interst'].sum(), principle], labels=['Total Interest Earned', 'Principle Amount'], autopct='%1.1f%%', startangle=140)
    plt.title('Total Interest Earned vs Principle Amount')
    plt.legend(loc='upper right')
    plt.axis('equal')  
    st.pyplot(plt)

# note footer should be vivible in both light and dark mode
st.markdown("""
    <style>
        body {
            background-color: #F5F5F5;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)
# Add a footer and footer should be visible all the time
st.markdown(
    """



    <div style='background-color: #222222; color: #FFFFFF; padding: 15px; text-align: center;'>
        © 2025 Smart Bill Generator. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)

