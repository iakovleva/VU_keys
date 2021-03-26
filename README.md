# VU_keys

1. cleanup.py - script for standardizing search query.
It includes remove_symbols, remove_phones, remove_cities, remove_regions, remove_countries, change_abbr functions. 

Receives a string as input, returns the same string with:
- correct abbreviations
- special symbols removed
- Russian cities and regions removed
- phone numbers removed

2. morpher_script.py is suplementary, it is used for forming lists of cities and
regions in diffrerent cases.

3. values.py contains ready lists of values that are passed to cleanup. 

4. The script reads and writes from PostgreSQL DB, table 'keys'. Initial value - column 'key', updated value is written to the column 'newkey'.
```
CREATE TABLE keys(
        key text,
        source text,
        newkey text);
```
