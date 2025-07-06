# Academic grandfolks

Trace one's academic genealogy by crawling a dataset of academic advisors and students. It fetches data from [j2kun/math-genealogy-scraper](https://github.com/j2kun/math-genealogy-scraper) (providing scraped data from [Mathematics Genealogy Project](https://www.mathgenealogy.org/)) and recursively finds all academic ancestors for specified individuals.

## Features

- Fetches academic genealogy data from a public dataset.
- Traces academic ancestors for given starting individuals.
- Goes back many generations (configurable, defaults to 40).
- Outputs a sorted list of ancestors with their generational distance.

## Usage

1. **Install requirements**  
	This script requires Python 3 and the `requests` library.  
	Install dependencies with:
	```bash
	pip install requests
	```

2. **Configure ancestors**  
	Edit the `myancestors.py` file to set starting ancestor IDs in the `my_ancestors` dictionary.  
	You can find the IDs from the [Mathematics Genealogy Project](https://www.mathgenealogy.org/).

3. **Run the script**  
	Execute the script with:
	```bash
	python myancestors.py
	```

## Example Output

```
Guido Sciavicco (1)
Angelo Montanari (2)
Alberto Policriti (2)
...
```

## Data Source

This project uses data from [j2kun/math-genealogy-scraper](https://github.com/j2kun/math-genealogy-scraper).
