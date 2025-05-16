# import astropy.astropy.table.table as test

# test.read('test.qdp',format='ascii.qdp')

# import sys
# import os

# # Add the Phase 2 folder to the Python path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'astropy')))

from astropy.table import Table

# Path to the QDP file
qdp_file = 'test.qdp'  # Ensure this file exists and is valid

try:
    # Read the QDP file
    table = Table.read(qdp_file, format='ascii.qdp')
    
    # Print the table to verify the output
    print(table)
    
    # Add assertions to validate the output (example)
    assert len(table) > 0, "Table is empty"
    assert 'a' in table.colnames, "Column 'a' is missing"
except Exception as e:
    print(f"Error reading QDP file: {e}")