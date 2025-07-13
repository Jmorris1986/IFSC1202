import requests
import re

def render_unicode_grid_from_doc(url):
    # Step 1: Retrieve document content
    response = requests.get(url)
    response.raise_for_status()
    html = response.text

    # Step 2: Extract plain text (remove HTML tags)
    text = re.sub(r'<[^>]+>', '', html)

    # Step 3: Parse the coordinates and characters
    pattern = re.compile(r"x:\s*(\d+),\s*y:\s*(\d+),\s*char:\s*(.)")
    data = pattern.findall(text)

    # Step 4: Build grid dimensions
    coords = [(int(x), int(y), ch) for x, y, ch in data]
    max_x = max(x for x, _, _ in coords)
    max_y = max(y for _, y, _ in coords)

    # Step 5: Initialize and populate the grid
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y, ch in coords:
        grid[y][x] = ch  # y is row, x is column

    # Step 6: Print the grid
    for row in grid:
        print(''.join(row))
url = 'https://docs.google.com/document/d/e/2PACX-1vTjCEXAMPLE/pub'
render_unicode_grid_from_doc(url)
# Note: Replace the URL with the actual document URL you want to process.
# Ensure you have the requests library installed in your Python environment.
# You can install it using pip if it's not already installed.
# Example: pip install requests
# The above code will print the grid based on the coordinates and characters extracted from the document.