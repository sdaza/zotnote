from requests import api
from pyzotero import zotero
import pandas
import re


def extractNotes(notes, separator = "#"):
    '''Extract notes using separator'''
    rows_list = []
    for k,txt in notes.items():
        tx = txt.split(separator)
        tx = list(filter(lambda x: x != "", tx))
        dtx = {"parent": k}
        for t in tx:
            v = t.strip().split("\n", 1)
            if (len(v) > 1):
                dtx[v[0].lower().replace(" ", "_")] = v[1]
            else: 
                dtx[v[0].lower().replace(" ", "_")] = ""
        rows_list.append(dtx)
    return pd.DataFrame(rows_list)      


def exportNotes(library_type="group", collection=None, library_id=None, 
    api_key=None, file="zotero-notes.csv", separator = "#"):
    '''Export notes to a CSV file'''
    zot = zotero.Zotero(library_id, library_type, api_key)
    notes = pandas.DataFrame(columns=["notes"])
    items = zot.collection_items(collection)
    for item in items:
        try:
            notes = notes.append(
                {"notes": item["data"]["note"], "parent": item["data"]["parentItem"]},
                ignore_index=True,
            )
        except:
            notes = notes.append({"notes": ""}, ignore_index=True)
        notes = notes.loc[[len(x) > 0 for x in notes["notes"]]]

    citations = pandas.DataFrame(columns=["citation"])
    for parent in notes["parent"]:
        citations = citations.append(
            {
                "citation": zot.item(
                    parent,
                    content="citation",
                    format="keys",
                    style="taylor-and-francis-council-of-science-editors-author-date",
                ),
            "parent": parent,
            "tags": zot.item_tags(parent), 
            "title": zot.item(parent)["data"]["title"] 
            },
            ignore_index=True,
        )
    
    res = citations.set_index("parent").join(notes.set_index("parent"))
    res["notes"] = [re.sub("<.*?>", "", str(x)) for x in res["notes"]]
    notes = extractNotes(res["notes"], separator=separator)

    ref = citations.set_index("parent")
    ref["citation"] = [re.sub("\[|\]|\(|\)|'", "", str(x)) for x in ref["citation"]]
    ref["citation"] = [re.sub("<.*?>", "", str(x)) for x in ref["citation"]]
    ref["title"] = [re.sub("\['|'\]", "", str(x)) for x in ref["title"]]
    ref["tags"] = [re.sub("\[|\]|']", "", str(x)) for x in ref["tags"]]
    ref["tags"] = [re.sub("'", "", str(x)) for x in ref["tags"]]
    ref = pandas.DataFrame(ref)
    
    return ref.merge(notes, left_on='parent', right_on='parent') \
        .rename(columns = {"parent" : "id"}, inplace=False) \
        .to_csv(file, index=False)