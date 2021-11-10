import pandas as pd
import numpy as np


def delete_non_complete_entries(chunk):
    chunk = chunk.replace('None', np.NaN)
    chunk = chunk.dropna(subset=['quotation', 'speaker'])
    return chunk

def delete_duplicates(chunk):
    chunk = chunk.drop_duplicates(subset=['quoteID','speaker', 'date'])
    return chunk