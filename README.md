# merriam_scraper

The Merriam Webster's Online Dictionary API does not provide a way to retrieve a word's syllable division. That is, which letters are part of which syllable in a multisyllabic word.

**merriamScraper.py** scrapes Merriam Webster's Online Dictionary (collegiate) for requested words' syllable division and first listed phonetic spelling. 

If a word's first listed phonetic spelling depends on its part of speech, a line for each phonetic spelling and associated part of speech will be returned.

Returned info is printed to standard output.

## Usage: 
   ```
   python3.6 merriamScraper.py REQUEST
   ```
```REQUEST``` may be a word or a text file. If a text file, **merriamScraper.py** will scrape Merriam Webster's for each line of the text file.
