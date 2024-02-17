import pandas as pd
import plotly.express as px

# Load the dataset
file_path = 'transactions.xlsx'
transactions = pd.read_excel(file_path)

# 1. Convert 'amount' column to numeric (removing commas)
transactions['amount'] = transactions['amount'].str.replace(',', '').astype(float)

# 2. Ensure 'date' is in datetime format
transactions['date'] = pd.to_datetime(transactions['date'])

# 3. Handle missing values
# For this example, we'll leave missing values as is, but you may choose to fill or drop them based on your analysis needs.

# 4. Standardize text and categorical data
transactions['status'] = transactions['status'].str.lower().str.strip()
transactions['txn_description'] = transactions['txn_description'].str.upper().str.strip()
transactions['movement'] = transactions['movement'].str.capitalize().str.strip()

# 5. Convert 'card_present_flag' to a boolean type, where NaN indicates a non-applicable condition
# Note: This conversion depends on domain knowledge of the data. Here, NaNs are left as is.
transactions['card_present_flag'] = transactions['card_present_flag'].apply(lambda x: bool(x) if pd.notnull(x) else x)

# 6. Remove duplicate rows if any (based on a subset of columns that uniquely identify a transaction)
unique_columns = ['transaction_id', 'date', 'amount']
transactions.drop_duplicates(subset=unique_columns, inplace=True)

# 7. Create derived time-based features from the 'date' column
transactions['month'] = transactions['date'].dt.month
transactions['day_of_week'] = transactions['date'].dt.day_name()

# 8. Validate and clean specific columns if necessary (not shown here as it depends on external data or specific rules)

# Display the cleaned dataframe and data types for verification
print(transactions.head())
print(transactions.dtypes)



# Assuming 'transactions' is your DataFrame and it's already loaded and cleaned
# Ensure 'date' and 'amount' columns are in the correct format
# transactions['date'] = pd.to_datetime(transactions['date'])
# transactions['amount'] = transactions['amount'].astype(float)

# Create a new column for year-month
transactions['year_month'] = transactions['date'].dt.to_period('M')

# Calculate the cumulative sum of amounts by month
transactions_sorted = transactions.sort_values(by='year_month')
transactions_sorted['cumulative_amount'] = transactions_sorted.groupby('year_month')['amount'].cumsum()

# Group by the new year-month column to get the last cumulative value for each month
cumulative_monthly = transactions_sorted.groupby('year_month')['cumulative_amount'].last().reset_index()

# Convert 'year_month' back to datetime to ensure Plotly handles it correctly
cumulative_monthly['year_month'] = cumulative_monthly['year_month'].dt.to_timestamp()

# Create the plot
fig = px.line(cumulative_monthly, x='year_month', y='cumulative_amount',
              title='Cumulative Sum of Amounts by Month',
              labels={'year_month': 'Month', 'cumulative_amount': 'Cumulative Amount'},
              markers=True)

# Improve layout
fig.update_layout(xaxis_title='Month',
                  yaxis_title='Cumulative Amount',
                  xaxis=dict(tickformat='%b\n%Y'),
                  hovermode='x')

# Show the figure
fig.show()
