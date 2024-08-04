# Anime Watchlist Notion Project

This project uses Notion to create and manage an anime watch list. It automatically fetches anime details from the Jikan API (a MyAnimeList API wrapper) and updates a Notion database with the information.

## Table of Contents
- [Anime Watchlist Notion Project](#anime-watchlist-notion-project)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Setup](#setup)
    - [Prerequisites](#prerequisites)
- [Step-by-Step Guide to Setting Up Your Anime Watch List in Notion](#step-by-step-guide-to-setting-up-your-anime-watch-list-in-notion)
  - [Step 1: Set Up Notion Database Structure](#step-1-set-up-notion-database-structure)
    - [Main Anime Database](#main-anime-database)
    - [Seasons Database](#seasons-database)
    - [Episodes Database](#episodes-database)
    - [Characters Database](#characters-database)
  - [Step 2: Visual and Aesthetic Enhancements in Notion](#step-2-visual-and-aesthetic-enhancements-in-notion)
  - [Step 3: Integrate Notion API and Python Script](#step-3-integrate-notion-api-and-python-script)
    - [Set Up Notion API Integration](#set-up-notion-api-integration)
    - [Installation](#installation)
    - [Configuration](#configuration)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
    - [Detailed Explanation](#detailed-explanation)
  - [Testing](#testing)
  - [Contributing](#contributing)
  - [License](#license)

## Features
- Fetches anime details using the Jikan API.
- Updates a Notion database with the anime's English name, Japanese name, banner image, trailer link, story summary, genres, and more.
- Uses Python scripts to automate the process.
- Includes unit tests for key functionalities.

## Setup

### Prerequisites
- Python 3.6 or higher
- A Notion account
- Notion API integration and database IDs
- A GitHub account (optional, for CI/CD setup)

# Step-by-Step Guide to Setting Up Your Anime Watch List in Notion

## Step 1: Set Up Notion Database Structure

### Main Anime Database
Create a new table in Notion for your main Anime database and add the following properties:

- **Title (Default)**: Anime name
- **Japanese Name**: Text
- **Banner Image**: Files
- **Seasons**: Relation to "Seasons" database
- **Total Seasons**: Formula to count linked seasons
- **Total Episodes**: Formula to sum episodes from linked seasons
- **Characters**: Relation to "Characters" database
- **Trailer**: URL
- **Story Summary**: Text
- **Genres**: Multi-select
- **Watch Status**: Select (e.g., Watching, Completed)
- **Ratings**: Text
- **Tags**: Multi-select (optional)

### Seasons Database
Create a new table in Notion for your Seasons database and add the following properties:

- **Anime**: Relation to Main Anime database
- **Season Name**: Text
- **Total Episodes**: Number
- **Episodes**: Relation to "Episodes" database

### Episodes Database
Create a new table in Notion for your Episodes database and add the following properties:

- **Season**: Relation to Seasons database
- **Episode Number**: Number
- **Episode Name**: Text

### Characters Database
Create a new table in Notion for your Characters database and add the following properties:

- **Anime**: Relation to Main Anime database
- **Character Name**: Text
- **Character Image**: Files

## Step 2: Visual and Aesthetic Enhancements in Notion
Enhance the visual appeal and organization of your Notion database:

1. **Create a "Gallery" View**: 
   - For the main Anime database, create a "Gallery" view.
   - Configure the gallery to display the "Banner Image" as the card preview.
   - Select properties to show on the card, such as Title, Genres, Watch Status.

2. **Add Icons and Cover Images**:
   - Add icons and cover images to your Notion page for a more visually appealing look.
   - Click on "Add icon" at the top of the page to select an icon.
   - Click on "Add cover" to upload or choose a cover image that represents the theme of your anime watch list.

3. **Use Color-Coding and Toggles**:
   - Utilize Notion’s color-coding for tags and genres to make them stand out.
   - Use Notion’s "Toggle List" feature to group similar properties together for a cleaner look.

## Step 3: Integrate Notion API and Python Script
Automate the fetching of anime details by integrating the Notion API with a Python script.

### Set Up Notion API Integration

1. **Go to Notion Developers**:
   - Visit the [Notion Developers](https://www.notion.so/my-integrations) page and create a new integration.

2. **Copy the Integration Token**:
   - After creating the integration, copy the integration token for use in your Python script.

3. **Share the Database with Integration**:
   - Go to your Notion databases.
   - Click on "Share" and invite your integration to the database.

By following these steps, you will set up a detailed and visually appealing anime watch list in Notion and integrate it with a Python script to automate data fetching. In the next step, we will proceed with the Python script implementation to fetch anime details and update the Notion database.


### Installation
1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/anime-watchlist.git
    cd anime-watchlist
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

### Configuration
1. **Create a `.env` file in the root directory and add your Notion API token and database IDs:**
    ```env
    NOTION_TOKEN=your_notion_token_here
    ANIME_DATABASE_ID=your_anime_database_id_here
    SEASONS_DATABASE_ID=your_seasons_database_id_here
    EPISODES_DATABASE_ID=your_episodes_database_id_here
    CHARACTERS_DATABASE_ID=your_characters_database_id_here
    ```

2. **Setup your Notion database:**
   - Follow the structure provided in the [Project Structure](#project-structure) section to create and link your Notion databases for anime, seasons, and characters.

## Usage
1. **Run the script to fetch and update anime details:**
    ```sh
    python src/main.py
    ```

## Project Structure
anime-watchlist/
├── .gitignore
├── README.md
├── requirements.txt
├── src/
│ ├── init.py
│ ├── main.py
│ ├── notion_handler.py
│ └── config.py
├── tests/
│ ├── init.py
│ ├── test_main.py
│ └── test_notion_handler.py
├── .env
├── .github/
│ └── workflows/
│ └── ci.yml


### Detailed Explanation
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **README.md**: Provides information about the project.
- **requirements.txt**: Lists the Python packages required for the project.
- **src/**: Contains the main source code for the project.
  - **__init__.py**: Initializes the src module.
  - **main.py**: The main script to run the project.
  - **notion_client.py**: Contains functions to interact with the Notion API.
  - **config.py**: Loads configuration from the .env file.
- **tests/**: Contains unit tests for the project.
  - **__init__.py**: Initializes the tests module.
  - **test_main.py**: Tests for the main script.
  - **test_notion_client.py**: Tests for the Notion client functions.
- **.env**: Stores environment variables (not to be committed to Git).
- **.github/workflows/ci.yml**: GitHub Actions workflow for continuous integration.

## Testing
1. **Run the unit tests:**
    ```sh
    python -m unittest discover tests
    ```

## Contributing
1. **Fork the repository.**
2. **Create a new branch:**
    ```sh
    git checkout -b feature/your-feature-name
    ```
3. **Make your changes and commit them:**
    ```sh
    git commit -m "Add some feature"
    ```
4. **Push to the branch:**
    ```sh
    git push origin feature/your-feature-name
    ```
5. **Open a pull request.**

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
