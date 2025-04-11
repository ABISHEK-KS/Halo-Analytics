import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import re
import numpy as np

# Configurations
st.set_page_config(page_title="ProdRec - Product Comparison Platform", page_icon="🛍️", layout="wide")

# Load and Apply External CSS (if exists)
def load_css():
    """Reads external CSS and applies it."""
    try:
        with open("externalcss.css", "r") as f:
            css = f.read()
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("CSS file 'externalcss.css' not found. Make sure it is in the correct directory.")

# Helper Functions
@st.cache_data
def load_data(file_path):
    """Load dataset from a local CSV file and return a copy to avoid mutation."""
    data = pd.read_csv(file_path)
    
    # Check if 'category' column exists
    if 'category' not in data.columns:
        raise ValueError("'category' column not found in the dataset.")
    
    # Parse categories
    data = parse_categories(data)
    
    return data

def parse_categories(data):
    """Parse categories with synonyms separated by '|'."""
    data['parsed_category'] = data['category'].apply(lambda x: x.split('|')[0] if isinstance(x, str) else 'Unknown')
    return data

def show_home():
    """Render the Home Page."""
    st.title("Welcome to **ProdRec**")
    st.subheader("Your Trusted Companion in Smarter Shopping Decisions")
    st.markdown("""At **ProdRec**, we simplify your shopping journey by helping you:
    - Discover products tailored to your needs and budget.
    - Compare features, prices, and ratings side-by-side.
    - Decide with confidence, backed by clear, transparent insights.

    Let’s make your shopping experience smarter, easier, and more rewarding.""")
    st.image(
        "https://via.placeholder.com/1200x500.png?text=Your+Product+Comparison+Starts+Here!",
        use_column_width=True,
        caption="Explore. Compare. Decide."
    )
    st.markdown("---")
    st.markdown("### Ready to explore?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Explore Products"):
            st.success("Switch to 'Compare Products' using the sidebar.")
    with col2:
        if st.button("Learn More"):
            st.info("ProdRec makes smarter shopping possible.")
    st.markdown("---")
    st.markdown("© 2024 ProdRec Inc. | Built with ❤️ using Streamlit")

import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

@st.cache_data
def load_data(file_path):
    """Load dataset from a local CSV file and return a copy to avoid mutation."""
    data = pd.read_csv(file_path)
    
    # Check if 'Category' column exists (case-sensitive check)
    if 'Category' not in data.columns:
        raise ValueError("'Category' column not found in the dataset.")
    
    # Parse categories (handle cases where data might have multiple categories or issues)
    data = parse_categories(data)
    
    # Clean other columns such as price, ratings
    data['discounted_price'] = pd.to_numeric(data['Price now'], errors='coerce')
    data['actual_price'] = pd.to_numeric(data['Earlier Price'], errors='coerce')
    data['rating'] = pd.to_numeric(data['Rating'], errors='coerce')
    data['rating_count'] = pd.to_numeric(data['Rating Count'], errors='coerce')

    return data

def parse_categories(data):
    """Parse categories with synonyms separated by '|'."""
    data['parsed_category'] = data['Category'].apply(lambda x: x.split('|')[0] if isinstance(x, str) else 'Unknown')
    return data



def show_home():
    """Render the Home Page."""
    st.title("Welcome to **ProdRec**")
    st.subheader("Your Trusted Companion in Smarter Shopping Decisions")
    st.markdown("""At **ProdRec**, we simplify your shopping journey by helping you:
    - Discover products tailored to your needs and budget.
    - Compare features, prices, and ratings side-by-side.
    - Decide with confidence, backed by clear, transparent insights.

    Let’s make your shopping experience smarter, easier, and more rewarding.""")
    st.image(
        "https://via.placeholder.com/1200x500.png?text=Your+Product+Comparison+Starts+Here!",
        use_column_width=True,
        caption="Explore. Compare. Decide."
    )
    st.markdown("---")
    st.markdown("### Ready to explore?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Explore Products"):
            st.success("Switch to 'Compare Products' using the sidebar.")
    with col2:
        if st.button("Learn More"):
            st.info("ProdRec makes smarter shopping possible.")
    st.markdown("---")
    st.markdown("© 2024 ProdRec Inc. | Built with ❤️ using Streamlit")

@st.cache_data
def load_data(file_path):
    """Load dataset from a local CSV file and return a copy to avoid mutation."""
    data = pd.read_csv(file_path)
    
    # Check if 'Category' column exists (case-sensitive check)
    if 'Category' not in data.columns:
        raise ValueError("'Category' column not found in the dataset.")
    
    # Parse categories (handle cases where data might have multiple categories or issues)
    data = parse_categories(data)
    
    # Clean other columns such as price, ratings
    data['discounted_price'] = pd.to_numeric(data['Price now'], errors='coerce')
    data['actual_price'] = pd.to_numeric(data['Earlier Price'], errors='coerce')
    data['rating'] = pd.to_numeric(data['Rating'], errors='coerce')
    data['rating_count'] = pd.to_numeric(data['Rating Count'], errors='coerce')

    return data

def parse_categories(data):
    """Parse categories if they contain multiple values separated by '|'. For now, we take the first category."""
    data['parsed_category'] = data['Category'].apply(lambda x: x.split('|')[0] if isinstance(x, str) else 'Unknown')
    return data

@st.cache_data
def load_data(file_path):
    """Load dataset from a local CSV file and return a copy to avoid mutation."""
    data = pd.read_csv(file_path)
    
    # Check if 'Category' column exists (case-sensitive check)
    if 'Category' not in data.columns:
        raise ValueError("'Category' column not found in the dataset.")
    
    # Parse categories (handle cases where data might have multiple categories or issues)
    data = parse_categories(data)
    
    # Clean other columns such as price, ratings
    data['discounted_price'] = pd.to_numeric(data['Price now'], errors='coerce')
    data['actual_price'] = pd.to_numeric(data['Earlier Price'], errors='coerce')
    data['rating'] = pd.to_numeric(data['Rating'], errors='coerce')
    data['rating_count'] = pd.to_numeric(data['Rating Count'], errors='coerce')

    return data

def parse_categories(data):
    """Parse categories if they contain multiple values separated by '|'. For now, we take the first category."""
    data['parsed_category'] = data['Category'].apply(lambda x: x.split('|')[0] if isinstance(x, str) else 'Unknown')
    return data

@st.cache_data
def load_data(file_path):
    """Load dataset from a local CSV file and return a copy to avoid mutation."""
    data = pd.read_csv(file_path)
    
    # Check if 'Category' column exists (case-sensitive check)
    if 'Category' not in data.columns:
        raise ValueError("'Category' column not found in the dataset.")
    
    # Parse categories (handle cases where data might have multiple categories or issues)
    data = parse_categories(data)
    
    # Clean other columns such as price, ratings
    data['discounted_price'] = pd.to_numeric(data['Price now'], errors='coerce')
    data['actual_price'] = pd.to_numeric(data['Earlier Price'], errors='coerce')
    data['rating'] = pd.to_numeric(data['Rating'], errors='coerce')
    data['rating_count'] = pd.to_numeric(data['Rating Count'], errors='coerce')

    return data

def parse_categories(data):
    """Parse categories if they contain multiple values separated by '|'. For now, we take the first category."""
    data['parsed_category'] = data['Category'].apply(lambda x: x.split('|')[0] if isinstance(x, str) else 'Unknown')
    return data






#<---------------MAIN-FEATURES----PROCEED/LOG MODIFICATIONS---->

def clean_price(price_str):
    """Function to clean non-numeric characters from price strings and handle empty values."""
    if not price_str or price_str == '' or pd.isna(price_str):
        return np.nan  # Return NaN for empty or invalid price strings
    
    # Ensure price_str is a string and remove non-numeric characters (except dot for decimal)
    cleaned_price = re.sub(r'[^\d.]', '', str(price_str))
    
    try:
        return float(cleaned_price)  # Attempt to convert cleaned price to float
    except ValueError:
        return np.nan  # Return NaN if conversion fails

# Function to load product data from the 'aadv' folder
def load_data_from_folder(folder_path="aadv"):
    """Loads the product data from the 'aadv' folder and returns a DataFrame."""
    all_data = []
    for file in os.listdir(folder_path):
        if file.endswith('.csv'):  # assuming the data files are CSVs
            file_path = os.path.join(folder_path, file)
            # Read each CSV file and append to the list
            try:
                data = pd.read_csv(file_path)
                data['category'] = file.replace('.csv', '')  # Add category column based on filename
                all_data.append(data)
            except Exception as e:
                st.warning(f"Error reading {file}: {e}")
    
    # Concatenate all CSV files into one DataFrame
    if all_data:
        full_data = pd.concat(all_data, ignore_index=True)
        return full_data
    else:
        st.warning("No valid CSV files found in the folder.")
        return pd.DataFrame()

# Function to display the comparison page
def clean_ratings(rating_str):
    """Function to clean non-numeric characters from ratings and handle empty values."""
    try:
        return float(rating_str) if pd.notna(rating_str) else np.nan
    except ValueError:
        return np.nan  # Return NaN for invalid ratings

# In the show_compare function, clean ratings
def show_compare():
    """Render the Product Comparison Page with Visualizations"""
    st.title("🔍 Product Comparison")
    st.markdown("Compare products based on **category**, **price**, **ratings**, and other features.")

    # Load dataset with caching from the 'aadv' folder
    folder_path = "aadv"  # Update this with the path of the 'aadv' folder where your CSV files are
    data = load_data_from_folder(folder_path)

    if data.empty:
        st.error("No product data available for comparison.")
        return

    # Clean the price columns by removing non-numeric characters
    data['discount_price'] = data['discount_price'].apply(lambda x: clean_price(str(x)))
    data['actual_price'] = data['actual_price'].apply(lambda x: clean_price(str(x)))

    # Clean the ratings column
    data['ratings'] = data['ratings'].apply(lambda x: clean_ratings(x))

    # Ensure that discount_price and actual_price columns are numeric
    data['discount_price'] = pd.to_numeric(data['discount_price'], errors='coerce')
    data['actual_price'] = pd.to_numeric(data['actual_price'], errors='coerce')

    # Reduce initial dataset size (Show only top categories and products)
    unique_categories = data['category'].dropna().unique()
    selected_category = st.selectbox("Select a Category", unique_categories[:10])  # Display first 10 categories

    # Filter data based on selected category
    filtered_data = data[data['category'] == selected_category]

    # Product selection
    st.subheader("Select Products to Compare")
    product_options = filtered_data['name'].unique()  # Use 'name' for product names
    selected_products = st.multiselect("Choose Products:", product_options, default=product_options[:2])

    if len(selected_products) >= 2:
        comparison_data = filtered_data[filtered_data['name'].isin(selected_products)]

        # Point-Based Comparison Table
        st.subheader("Point-Based Comparison Table")
        
        # Compute price points (cheaper products get more points)
        min_price = comparison_data['discount_price'].min()
        comparison_data['price_points'] = comparison_data['discount_price'].apply(lambda x: (1 / (x - min_price + 1)) * 100 if pd.notna(x) else 0)

        # Compute rating points (higher ratings get more points)
        max_rating = comparison_data['ratings'].max() if not comparison_data['ratings'].isnull().all() else 1  # Avoid division by zero
        comparison_data['rating_points'] = comparison_data['ratings'].apply(lambda x: (x / max_rating) * 100 if pd.notna(x) else 0)

        # Compute total points
        comparison_data['total_points'] = comparison_data['price_points'] + comparison_data['rating_points']

        # Display the points data
        points_data = comparison_data[['name', 'price_points', 'rating_points', 'total_points']]
        st.dataframe(points_data)

        # Recommendation: Product with the highest points
        best_product = points_data.loc[points_data['total_points'].idxmax()]
        st.subheader("Recommended Product")
        st.markdown(f"The product with the most points is **{best_product['name']}** with **{best_product['total_points']} points**!")

        # Improved Visualizations

        # 1. Bar Chart for Price and Rating Comparison
        st.subheader("Price vs Ratings Comparison")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(comparison_data['name'], comparison_data['discount_price'], alpha=0.7, label='Discount Price', color='blue')
        ax.bar(comparison_data['name'], comparison_data['ratings'] * 10, alpha=0.7, label='Ratings x10', color='orange')
        ax.set_xlabel('Product')
        ax.set_ylabel('Value')
        ax.set_title('Price vs Ratings for Selected Products')
        ax.legend()
        st.pyplot(fig)

        # 2. Scatter Plot for Price vs Rating
        st.subheader("Scatter Plot of Price vs Rating")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(comparison_data['discount_price'], comparison_data['ratings'], color='green', s=100)
        ax.set_xlabel('Discount Price')
        ax.set_ylabel('Ratings')
        ax.set_title('Price vs Rating Scatter Plot')
        st.pyplot(fig)

        # 3. Radar Chart for Product Comparison
        st.subheader("Radar Chart: Price vs Ratings")
        categories = ['Discount Price', 'Ratings']
        values = [comparison_data['discount_price'].mean(), comparison_data['ratings'].mean()]
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        ax.plot(categories, values, linewidth=2, linestyle='solid')
        ax.fill(categories, values, alpha=0.25)
        ax.set_title('Radar Chart of Price and Rating Comparison')
        st.pyplot(fig)

    else:
        st.warning("Please select at least 2 products for comparison.")

    st.markdown("---")
    st.markdown("© 2024 ProdRec Inc. | Built with ❤️ using Streamlit")





#<------------LOG MODIFICATIONS IN GITHUB--------->



    
# Load the phone data
phone_data = pd.read_csv('prp.csv')



def show_phone_comparison():
    """Render Phone Comparison Section with Advanced and Aesthetically Pleasing Visuals."""
    st.title("📱 Compare Phones")

    # Step 1: Select Phones for Comparison (Multiple Brands)
    brands = phone_data['Brand'].unique()
    selected_brands = st.multiselect("Select Brands", brands, default=brands[:1], key="brand_selector")

    # Prepare list to store selected phones
    selected_phones = []

    for brand in selected_brands:
        brand_data = phone_data[phone_data['Brand'] == brand]
        models = brand_data['Model'].unique()
        selected_model = st.selectbox(f"Select Phone from {brand}", models, key=f"model_selector_{brand}")
        selected_phones.append(selected_model)

    if len(selected_phones) >= 2:
        # Filter the data for selected models
        comparison_data = phone_data[phone_data['Model'].isin(selected_phones)]

        # Convert 'Memory' and 'Storage' to numeric (removing 'GB' and converting to integer)
        comparison_data['Memory'] = comparison_data['Memory'].str.replace('GB', '').astype(int)
        comparison_data['Storage'] = comparison_data['Storage'].str.replace('GB', '').astype(int)

        # Assign points for each feature (optional, based on your logic)
        def assign_points(phone):
            points = 0
            points += phone['Memory']  # Points for Memory (1 point per GB of RAM)
            points += phone['Storage'] / 64  # Points for Storage (1 point per 64 GB of Storage)
            points += phone['Rating'] * 2  # Points for Rating (Maximum 10 points for a 5-star rating)
            points += 100000 / phone['Selling Price']  # Inverse scoring: lower price gets more points
            return points

        # Calculate points for each phone
        comparison_data['Points'] = comparison_data.apply(assign_points, axis=1)

        # Display comparison table
        st.subheader("Phone Comparison Table")
        table_data = comparison_data[['Brand', 'Model', 'Color', 'Memory', 'Storage', 'Rating', 'Selling Price', 'Original Price', 'Points']]
        table_data = table_data.rename(columns={
            'Brand': 'Brand',
            'Model': 'Model',
            'Color': 'Color',
            'Memory': 'Memory (GB)',
            'Storage': 'Storage (GB)',
            'Rating': 'Rating',
            'Selling Price': 'Selling Price (₹)',
            'Original Price': 'Original Price (₹)',
            'Points': 'Points'
        })
        st.dataframe(table_data)

        # **Phone Recommendation: Best Overall Score**
        best_phone = comparison_data.loc[comparison_data['Points'].idxmax()]
        st.markdown("### 📱 **Recommended Phone with the Best Features**")
        st.write(f"The phone with the **best features** is **{best_phone['Model']}** by {best_phone['Brand']}.")
        st.write(f"**Total Points**: {best_phone['Points']}")
        st.write(f"**Selling Price**: ₹{best_phone['Selling Price']}")
        st.write(f"**Rating**: {best_phone['Rating']} stars")
        st.write(f"**Best Buy**: This phone offers the most balanced combination of **features, performance**, and **price**!")

        # Visualizations

        # **Visual 1: Violin Plot of Rating Distribution by Model**
        st.subheader("Rating Distribution by Model (Violin Plot)")
        fig = px.violin(comparison_data, y='Rating', x='Model', color='Model', box=True, points="all", title="Rating Distribution by Model")
        st.plotly_chart(fig)

        # **Visual 2: Violin Plot of Selling Price Distribution by Model**
        st.subheader("Selling Price Distribution by Model (Violin Plot)")
        fig = px.violin(comparison_data, y='Selling Price', x='Model', color='Model', box=True, points="all", title="Selling Price Distribution by Model")
        st.plotly_chart(fig)

        # **Visual 3: Violin Plot of Memory (RAM) Distribution by Model**
        st.subheader("Memory (RAM) Distribution by Model (Violin Plot)")
        fig = px.violin(comparison_data, y='Memory', x='Model', color='Model', box=True, points="all", title="Memory (RAM) Distribution by Model")
        st.plotly_chart(fig)

        # **Visual 4: Parallel Coordinates Plot (for feature comparison)**
        st.subheader("Parallel Coordinates Plot")
        fig = px.parallel_coordinates(
            comparison_data, color="Points", dimensions=["Memory", "Storage", "Rating", "Selling Price", "Points"],
            title="Parallel Coordinates Plot for Feature Comparison"
        )
        st.plotly_chart(fig)

        # **Visual 5: Radar Chart for Feature Comparison**
        st.subheader("Radar Chart for Feature Comparison")
        radar_data = comparison_data[['Model', 'Memory', 'Storage', 'Rating', 'Selling Price', 'Points']]
        radar_data = radar_data.set_index('Model')
        fig = px.line_polar(radar_data, r='Memory', theta=radar_data.index, line_close=True, title="Radar Chart of Phone Features")
        st.plotly_chart(fig)

        # **Visual 6: Correlation Heatmap (Numerical Data)**
        st.subheader("Correlation Heatmap")
        corr = comparison_data[['Memory', 'Storage', 'Rating', 'Selling Price', 'Original Price', 'Points']].corr()
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
        st.pyplot(plt)

        # **Visual 7: Distribution of Points (Histogram)**
        st.subheader("Points Distribution")
        fig = px.histogram(comparison_data, x='Points', title="Distribution of Points across Phones", color='Model')
        st.plotly_chart(fig)

        # **Visual 8: Line Plot of Selling Price vs Rating (Trend analysis)**
        st.subheader("Selling Price vs Rating Trend (Line Plot)")
        fig = px.line(comparison_data, x='Selling Price', y='Rating', color='Model', markers=True, title="Selling Price vs Rating Trend")
        st.plotly_chart(fig)

        # **Visual 9: Line Plot of Storage vs Points (Trend analysis)**
        st.subheader("Storage vs Points Trend (Line Plot)")
        fig = px.line(comparison_data, x='Storage', y='Points', color='Model', markers=True, title="Storage vs Points Trend")
        st.plotly_chart(fig)

        # **Visual 10: Line Plot of Memory vs Selling Price (Trend analysis)**
        st.subheader("Memory (RAM) vs Selling Price Trend (Line Plot)")
        fig = px.line(comparison_data, x='Memory', y='Selling Price', color='Model', markers=True, title="Memory (RAM) vs Selling Price Trend")
        st.plotly_chart(fig)

# Call the function to show phone comparison when running the app







# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Compare Products", "Compare Phones"])

if page == "Home":
    load_css()
    show_home()

elif page == "Compare Products":
    load_css()
    show_compare()

elif page == "Compare Phones":
    load_css()
    show_phone_comparison()
