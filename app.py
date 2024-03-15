import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# Load Excel datasets
linkedin_df = pd.read_excel("youtube1.xlsx") 
instagram_df = pd.read_excel("INSTA1.xlsx")  
facebook_df = pd.read_excel("face book1.xlsx")  
twitter_df = pd.read_excel("twitter.xlsx") 

# Define function to plot data for LinkedIn reach
def plot_linkedin_data(df, car_model):
    filtered_data = df[df['Model Name'] == car_model]
    plt.figure(figsize=(10, 6))
    monthly_data = filtered_data.groupby('Month').agg({'Sales Count': 'sum'})
    st.bar_chart(monthly_data)
    plt.title(f'LinkedIn Reach Metrics for {car_model}')
    plt.xlabel('Month')
    plt.ylabel('Count')
    # Sales information
    st.subheader("Sales Information")
    st.write(filtered_data[['Month', 'Sales Count']])

# Define function to plot data for Instagram reach
def plot_instagram_data(df, car_model):
    filtered_data = df[df['Model Name'] == car_model]
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=filtered_data, x='Month', y='Likes', label='Likes', estimator='sum')
    sns.lineplot(data=filtered_data, x='Month', y='Comment', label='Comments', estimator='sum')
    sns.lineplot(data=filtered_data, x='Month', y='Share', label='Shares', estimator='sum')
    plt.title(f'Instagram Reach Metrics for {car_model}')
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.legend()

    # Sales information
    st.subheader("Sales Information")
    st.write(filtered_data[['Month', 'Likes', 'Comment', 'Share']])

# Define function to plot data for Facebook reach
def plot_facebook_data(df, car_model):
    filtered_data = df[df['Model Name'] == car_model]
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=filtered_data, x='Month', y='Likes', label='Likes', estimator='sum')
    sns.lineplot(data=filtered_data, x='Month', y='Comment', label='Comments', estimator='sum')
    sns.lineplot(data=filtered_data, x='Month', y='Share', label='Shares', estimator='sum')
    plt.title(f'Facebook Reach Metrics for {car_model}')
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.legend()

    # Sales information
    st.subheader("Sales Information")
    st.write(filtered_data[['Month', 'Likes', 'Comment', 'Share']])

# Define function to plot data for Twitter reach
def plot_twitter_data(df, car_model):
    filtered_data = df[df['Model Name'] == car_model]
    plt.figure(figsize=(10, 6))
    monthly_data = filtered_data.groupby('Month').agg({'Likes': 'sum', 'Comment': 'sum', 'Share': 'sum'})
    st.bar_chart(monthly_data)
    plt.title(f'Twitter Reach Metrics for {car_model}')
    plt.xlabel('Month')
    plt.ylabel('Count')

    # Sales information
    st.subheader("Sales Information")
    st.write(filtered_data[['Month', 'Likes', 'Comment', 'Share']])

def home():
    st.title("Welcome to the Marketing Campaign Tool")
    st.write("This tool provides insights into the performance of marketing campaigns across various social media platforms.")

    # Add an image
    image = Image.open("images\marketing.png")
    st.image(image, caption="Marketing Campaign", use_column_width=True)

    # Add a description
    st.markdown("""
    ### Features:
    - **LinkedIn Reach**: Analyze sales performance on LinkedIn.
    - **Instagram Reach**: Analyze sales performance on Instagram.
    - **Facebook Reach**: Analyze sales performance on Facebook.
    - **Twitter Reach**: Analyze sales performance on Twitter.
    """)

    # Add an explanation of marketing strategy
    st.markdown("""
     Marketing Strategy:
    Effective marketing strategies are crucial for the success of any business. This tool helps you analyze the performance of your marketing campaigns on various social media platforms. By understanding the reach and engagement metrics, you can refine your strategies to attract more customers and boost sales.

     Get Started:
    Click the button below to explore the different features of this tool!
    """)

    # Add a call-to-action button
    if st.button("Get Started"):
        st.sidebar.success("Choose an option from the sidebar to explore!")

# Define other functions...

def main():
    option = st.sidebar.selectbox(
        "Select an option",
        ("Home", "LinkedIn reach", "Instagram reach", "Facebook reach", "Twitter Reach")
    )

def option1():
    st.title("LinkedIn reach")
    car_model = st.sidebar.selectbox("Select car model", linkedin_df['Model Name'].unique())
    plot_linkedin_data(linkedin_df, car_model)

def option2():
    st.title("Instagram reach")
    car_model = st.sidebar.selectbox("Select car model", instagram_df['Model Name'].unique())
    plot_instagram_data(instagram_df, car_model)

def option3():
    st.title("Facebook reach")
    car_model = st.sidebar.selectbox("Select car model", facebook_df['Model Name'].unique())
    plot_facebook_data(facebook_df, car_model)

def option4():
    st.title("Twitter Reach")
    car_model = st.sidebar.selectbox("Select car model", twitter_df['Model Name'].unique())
    plot_twitter_data(twitter_df, car_model)

def main():
    option = st.sidebar.selectbox(
        "Select an option",
        ("Home", "LinkedIn reach", "Instagram reach", "Facebook reach", "Twitter Reach")
    )

    if option == "Home":
        home()
    elif option == "LinkedIn reach":
        option1()
    elif option == "Instagram reach":
        option2()
    elif option == "Facebook reach":
        option3()
    elif option == "Twitter Reach":
        option4()

# Apply Seaborn style
sns.set_style("whitegrid")

# Run the app
if __name__ == "__main__":
    main()
