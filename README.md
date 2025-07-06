# Academic grandfolks

Trace one's academic genealogy by crawling a dataset of academic advisors and students. It fetches data from [j2kun/math-genealogy-scraper](https://github.com/j2kun/math-genealogy-scraper) and recursively finds all academic ancestors for the specified individuals.

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
	You can find someone's ID by searching them on the [Mathematics Genealogy Project website](https://www.mathgenealogy.org/id.php?id=230926).

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

This project uses data from the [Mathematics Genealogy Project website](https://www.mathgenealogy.org/), scraped and provided in JSON format by [j2kun/math-genealogy-scraper](https://github.com/j2kun/math-genealogy-scraper).
