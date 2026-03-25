import streamlit as st

# Function to display current time
def display_time():
    now = datetime.now(timezone.utc)
    st.write('Current Time (UTC): ', now.strftime('%Y-%m-%d %H:%M:%S'))

# Main function
if __name__ == '__main__':
    st.title('US Bond Clock')
    display_time()