# zotnote: extracting Zotero notes


### Introduction

- When reviewing literature it's nice to have the notes linked to Zotero references, but we would also want to extract all the notes and compare then in more systematic way. That way, we can keep our notes in Zotero (what is nice because all of us can have access to or edit them), but also we can create an Excel to explore notes in a more systematic way (i.e., text analysis).
- This small package extracts notes from a collection, and create a CSV file that can be easily read using Excel. 
- You only need to specify the collection id: https://www.zotero.org/groups/2406179/csic-echo/collections/M8N2VMAP. In this case: `M8N2VMAP`.
- The headers of notes have to start with #, text with headers cannot include #. For instance: 

```
# Research question

Estimates interaction effects between PGS of obesity and cohorts using HRS.

# Data

HRS

# Methods

Uses a HLM whereby they estimate effects of age and cohorts while making the intercepts and slopes a function of individual factors.

# Conclusions

# The good

# Limitations

Pays little attention to selection due to survival.
```

## Installation

```
pip install git+https://github.com/sdaza/zotnote.git
```

## Credentials

You can save the credentials in a `config.py` and import it (`import config`): 

````
library_id = "0000000"
api_key = "key"
library_type = "group"
````

## Example

```
import config
import zotnote as zn
zn.exportNotes(collection = "M8N2VMAP", library_id = config.library_id, 
    api_key = config.api_key, file = "mynotes.csv")

```

