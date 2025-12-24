# Prefix Word Finder - Web Interface

Last letter prefix word finer, do note some a few of the words do not work but most of them do. Also still missing some words. There are also some duplicates that I cant be boehtered to deal with. Maybe in the future ill make it all one text file
By Grobusk

## Features

-  Fast prefix search using Trie data structure
-  Sort results by longest, shortest, or no sorting
-  Scrollable results with "Load More" pagination

## Setup

1. Install dependencies:
   ```bash
   pip install Flask
   ```
   Or use the requirements file:
   ```bash
   pip install -r requirements.txt
   ```

2. Make sure you have the word list files
   - `dinos (1).txt`
   - `word.txt`
   - `words_alpha.txt`

## Running the Web Interface

Start the Flask server:
```bash
python app.py
```

Then open your web browser and go to:
```
http://localhost:5000
```

## Usage

1. Enter a prefix in the search box (e.g., "saur", "q", "pneumono")
2. Select a sort order (No Sorting, Longest First, or Shortest First)
3. Click "Search" or press Enter
4. Scroll through the results
5. Click "Load More" to see additional results
6. Click on any word to search for words starting with that word

## Files

- `app.py` - Flask backend server
- `prefix_finder.py` - Core Trie-based prefix finder
- `templates/index.html` - Web interface frontend
- `requirements.txt` - Python dependencies

## Notes

- The word lists are loaded when the server starts
- If you add new words to the text files, restart the server to include them
- The server runs on port 5000 by default

