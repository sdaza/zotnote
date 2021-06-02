# zotnote: extracting Zotero notes


### Introduction

When reviewing the literature, it's nice to have the notes linked to Zotero references, but it would also be great to compare them more systematically. The idea is to keep our notes in Zotero (which is nice because everyone sharing a library can access or edit them) and create a data file to explore notes (e.g., text analysis).

- This small package extracts notes from a collection and creates a CSV file that can be easily read using Excel.
- You only need to specify the collection id: https://www.zotero.org/groups/2406179/csic-echo/collections/M8N2VMAP = `M8N2VMAP` and corresponding credentials.
- The headers of notes have to start with #. Text between headings cannot include #. For instance: 

```markdown
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

You can save the credentials in a `config.py` and load them using `import config`: 

```yaml
library_id = "0000000"
api_key = "key"
library_type = "group"
```

## Example

```python
import config
import zotnote as zn
zn.exportNotes(collection="M8N2VMAP", library_id=config.library_id, 
    api_key=config.api_key, file="mynotes.csv")
```

[See also this notebook.](https://github.com/sdaza/zotnote/blob/main/zotero-notes.ipynb)
