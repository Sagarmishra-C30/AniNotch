# Anime Notion Filler

Welcome to the Anime Notion Filler project! This project provides a logic to fetch anime data and fill it into Notion using Python through anime names or a file containing names.

## Features

- Fetch anime data from a reliable source.
- Fill the fetched data into Notion.
- Support for fetching data from a file containing anime names.

## Installation

1. Clone the repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set up your Notion API credentials. See the [Notion API documentation](https://developers.notion.com/docs/using-the-api) for more information.

## Usage

1. Import the necessary modules:

```python
from anime_notion_filler import AnimeNotionFiller
```

2. Create an instance of the `AnimeNotionFiller` class:

```python
filler = AnimeNotionFiller(api_key='YOUR_API_KEY')
```

3. Fetch anime data from a file containing anime names:

```python
anime_names = ['anime1', 'anime2', 'anime3']
filler.fill_from_file(anime_names)
```

4. Fetch anime data from anime names:

```python
anime_names = ['anime1', 'anime2', 'anime3']
filler.fill_from_names(anime_names)
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
