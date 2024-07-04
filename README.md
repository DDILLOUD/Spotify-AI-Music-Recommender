# AI-Powered Music Recommendation System using Spotify API and Streamlit

## Description
This project implements an AI-powered music recommendation system using the Spotify API and Streamlit. It allows users to input their favorite artists and receive personalized music recommendations based on their preferences. The system leverages the Spotify API to access a vast catalog of songs and uses machine learning algorithms to generate recommendations.

## Features

- Search for artists on Spotify
- Generate song recommendations based on the artist's top tracks
- Display recommended songs with artist information

## Installation

1. Clone this repository:
git clone https://github.com/your-username/spotify-music-recommender.git
cd spotify-music-recommender

2. Create a virtual environment (optional but recommended):
 python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

3. Install the required packages: pip install -r requirements.txt

4. Set up Spotify API credentials:
- Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
- Create a new application
- Note your Client ID and Client Secret
- In the `recommender.py` file, replace `'YOUR_CLIENT_ID'` and `'YOUR_CLIENT_SECRET'` with your actual credentials

## Usage

To run the Streamlit app: streamlit run app.py

This will start the application and open it in your default web browser. If it doesn't open automatically, you can access it at `http://localhost:8501`.

## How to Use

1. Enter the name of an artist you like in the search bar.
2. Click the "Get Recommendations" button.
3. The app will display a list of recommended songs based on the artist's top tracks.

## Project Structure

- `app.py`: Contains the Streamlit web application code
- `recommender.py`: Includes the recommendation logic and Spotify API interactions
- `requirements.txt`: Lists all the required Python packages
- `README.md`: Provides information about the project and how to use it

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

