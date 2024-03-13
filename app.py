import streamlit as st
import pandas as pd
import json
from backend import PyStatsAPI
from streamlit_extras.badges import badge

st.set_page_config(page_title="PypiMeter")

st.title("PypiMeter")
st.write("Get Download Statistics for any Python package!")
st.text("")
st.text("")

# Instantiate the PyStatsAPI class
pypi_api = PyStatsAPI()

# Collect package name from user input
user_input = st.text_input("Enter Pypi package name here:")


# Execute backend.py with the user input
button_flag = 0
if st.button("Submit"):
    button_flag = 1
    # Call the method of the PyStatsAPI class
    recent_stats = pypi_api.call_api("recent", user_input)
    overall_stats = pypi_api.call_api("overall", user_input)
    system_stats = pypi_api.call_api("system", user_input)
    python_minor_stats = pypi_api.call_api("python_minor", user_input)

    # Write JSON responses to files (optional)
    with open("recent_stats.json", "w") as outfile:
        json.dump(recent_stats, outfile, indent=4)
    with open("overall_stats.json", "w") as outfile:
        json.dump(overall_stats, outfile, indent=4)
    with open("system_stats.json", "w") as outfile:
        json.dump(system_stats, outfile, indent=4)
    with open("python_minor_stats.json", "w") as outfile:
        json.dump(python_minor_stats, outfile, indent=4)

    # st.write("Recent Stats:", recent_stats)
    # st.write("Overall Stats with Mirrors:", overall_stats)
    # st.write("System Stats for Windows:", system_stats)
    # st.write("Python Minor Stats:", python_minor_stats)
if button_flag == 1:
    st.write("Searching Statistics for package:", user_input)


    # ---------- Recent Download Stats ----------
    st.subheader("Recent Download Stats:")
    # Load JSON data
    with open('recent_stats.json', 'r') as file:
        recent_data = json.load(file)
    for period, count in recent_data['data'].items():
        st.write(f"Last {period.capitalize()}: {count}")

    st.write("\n\n")

    # ---------- Overall Stats ----------
    st.subheader("Overall Stats (With and Without Mirrors):")
    # Load JSON data
    with open('overall_stats.json', 'r') as file:
        overall_data = json.load(file)

    # Convert JSON data to DataFrame
    df = pd.DataFrame(overall_data['data'])

    # Convert date column to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Pivot DataFrame to have 'date' as index and 'category' as columns
    df_pivot = df.pivot(index='date', columns='category', values='downloads')

    # Display line chart with legends
    st.line_chart(df_pivot, use_container_width=True)

    # ---------- System Stats ----------
    st.subheader("System Stats :")
    # Load JSON data
    with open('system_stats.json', 'r') as file:
        system_data = json.load(file)

    # Convert JSON data to DataFrame
    df = pd.DataFrame(system_data['data'])

    # Convert date column to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Pivot DataFrame to have 'date' as index and 'category' as columns
    df_pivot = df.pivot(index='date', columns='category', values='downloads')

    # Display line chart with legends
    st.line_chart(df_pivot, use_container_width=True)

    # ---------- Python Stats ----------
    st.subheader("Python Stats :")
    # Load JSON data
    with open('python_minor_stats.json', 'r') as file:
        python_data = json.load(file)

    # Convert JSON data to DataFrame
    df = pd.DataFrame(python_data['data'])

    # Convert date column to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Pivot DataFrame to have 'date' as index and 'category' as columns
    df_pivot = df.pivot(index='date', columns='category', values='downloads')

    # Display line chart with legends
    st.line_chart(df_pivot, use_container_width=True)

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

# ------Footer ---------
st.markdown("[![MIT](https://badgen.net/github/license/Pinak-Datta/wiz-craft)]()")

st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor"
            "=white)]("
            "https://github.com/Pinak-Datta/PypiMeter)")

st.markdown("![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2FPinak-Datta"
            "%2FPypiMeter&label=Visitors&countColor=%23263759)")