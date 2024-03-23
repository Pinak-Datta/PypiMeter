# 📈 PypiMeter 📈

[**PypiMeter**](https://pypimeter.streamlit.app/) is a web application built using Streamlit that provides statistics and insights about Python packages from PyPI (Python Package Index).

## 🔍 Overview 🔍

PypiMeter fetches data from the PyPI Stats API to display various statistics including recent downloads, overall downloads, system stats, and Python version stats for a given Python package. It allows users to input the package name and view the relevant statistics in an interactive and user-friendly manner.

<p>
  <a href="https://imgur.com/AOGi7GX"><img src="https://i.imgur.com/2YfdwWR.png" title="source: imgur.com" width="600" height="500"></a>
</p>

## 💻 Features 💻 

- **Recent Download Stats:** Displays the recent download statistics for the specified package.
- **Overall Stats:** Provides overall download statistics with and without mirrors for the specified package.
- **System Stats:** Shows download statistics based on different operating systems.
- **Python Version Stats:** Displays download statistics based on Python major and minor versions.

## 💽 Caching Mechanism Implented 💽 

PypiMeter implements a caching mechanism to prevent unnecessary calls to the PyPI Stats API. Since the data is updated daily, the application caches the fetched data locally. If the user requests the same package statistics within the same day, the application retrieves the data from the cache instead of making a new API call, thus reducing server load and improving performance.

## 🌐 Usage 🌐 

To use [**PypiMeter**](https://pypimeter.streamlit.app/), simply input the name of the Python package you're interested in, then click **Submit**, and the app will fetch and display the relevant statistics. You can see the progress of retrieval using the Progress box.

If any invalid package name is provided (basically a package name that does not exist on PyPI library), it throws a relevant warning message!

## ✏️ Contributing ✏️

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## 📜 License 📜

This project is licensed under the [MIT License](LICENSE).

