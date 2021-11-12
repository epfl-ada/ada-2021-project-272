import pandas as pd
import numpy as np


def delete_non_complete_entries(chunk):
    '''
    The function replaces 'None' values in the chunk by numpy NaN and deletes entries with missing quotation or speaker.
    It returns the modified chunk.
    '''
    chunk = chunk.replace('None', np.NaN)
    chunk = chunk.dropna(subset=['quotation', 'speaker'])
    return chunk

def delete_duplicates(chunk):
    '''
    The function deletes duplicates in the chunk and returns the modified chunk.
    '''
    chunk = chunk.drop_duplicates(subset=['quoteID','speaker', 'date'])
    return chunk