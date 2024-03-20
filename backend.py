import json
import os
import requests
from datetime import datetime


class PyStatsAPI:
    def __init__(self):
        # Define the base URL for the API
        self.base_url = "https://pypistats.org/api/packages/"
        # Define cache directory
        self.cache_dir = "cache"

        # Ensure cache directory exists
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def load_cache(self, filename):
        filepath = os.path.join(self.cache_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, "r") as file:
                return json.load(file)
        else:
            return None

    def save_cache(self, filename, data):
        filepath = os.path.join(self.cache_dir, filename)
        with open(filepath, "w") as file:
            json.dump(data, file)

    def is_cache_outdated(self, filename):
        filepath = os.path.join(self.cache_dir, filename)
        if os.path.exists(filepath):
            modification_date = datetime.fromtimestamp(os.path.getmtime(filepath)).date()
            current_date = datetime.now().date()
            return current_date > modification_date
        return True

    def call_api(self, endpoint, package, params=None):
        """
        Function to call the PyPI Stats API

        Args:
        - endpoint: API endpoint (e.g., 'recent', 'overall', 'python_major')
        - package: Name of the package
        - params: Optional query parameters

        Returns:
        - JSON response from the API
        """
        # Check if cached data exists and if it's outdated
        cache_filename = f"{package}_{endpoint}.json"
        if not self.is_cache_outdated(cache_filename):
            cached_data = self.load_cache(cache_filename)
            if cached_data:
                # print("Using cached data for", endpoint)
                return cached_data

        # Fetch data from API
        url = f"{self.base_url}/{package}/{endpoint}"
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            # Cache the data
            self.save_cache(cache_filename, data)
            return data
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
