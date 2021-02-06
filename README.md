# merriam_scraper

Scrapes Merriam Webster's Online Dictionary (collegiate) for requested words' syllable structure and first listed phonetic spelling. 

If a word's first listed phonetic spelling depends on its part of speech, a line for each phonetic spelling and associated part of speech will be returned.

Returned info is printed to standard output.

## Usage: 
   ```
   python3.6 merriamScraper.py REQUEST
   ```
```REQUEST``` may be a word or a text file. If a text file, **merriamScraper.py** will scrape Merriam Webster's for each line of the text file.
