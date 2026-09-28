# Weather CLI

A simple command-line weather application built with Python and the OpenWeather API.

## Features

- Accepts a city name from the user
- Fetches real-time weather data using an API
- Displays:
  - Temperature
  - Humidity
  - Weather condition
- Handles invalid cities and API request errors
- Uses environment variables to protect the API key
- Uses Git and GitHub for version control

## Technologies

- Python
- Requests
- OpenWeather API
- python-dotenv
- Git
- GitHub

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Shravani-1124/weather-cli.git
cd weather-cli
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment.

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install requests python-dotenv
```

### 4. Create a `.env` file

Create a file named `.env` in the project directory.

Add your OpenWeather API key:

```text
WEATHER_API_KEY=your_api_key_here
```

Do not share your API key publicly.

### 5. Run the application

```bash
python weather.py
```

## Example

```text
Enter your city here: Mumbai

Temperature: 28.06°C
Humidity: 79%
Condition: overcast clouds
```

## Project Structure

```text
weather-cli/
│
├── weather.py
├── .gitignore
├── README.md
└── .env
```

> `.env` and the virtual environment are excluded from Git using `.gitignore`.

## What I Learned

- Working with Python dictionaries
- Working with nested JSON data
- Accessing data from APIs
- Making HTTP requests using the `requests` library
- Handling exceptions using `try` and `except`
- Working with HTTP status codes
- Using environment variables to protect API keys
- Using `python-dotenv`
- Using Git for version control
- Pushing projects to GitHub
- Writing basic project documentation

## Future Improvements

- Add wind speed and feels-like temperature
- Add a 5-day weather forecast
- Add command-line arguments
- Improve the CLI interface
- Add weather icons
- Add unit selection between Celsius and Fahrenheit


