from datetime import datetime
import re

def xml_to_dict(element):
    # Namespace to use for finding elements
    ns = {'ss': 'urn:schemas-microsoft-com:office:spreadsheet'}

    # Dictionary to store data
    data_dict = {}

    # Find all rows in the sheet
    rows = element.findall('.//ss:Row', ns)

    # Extract header (row 2) for keys if available
    header = []
    if len(rows) > 1:  # Ensure there's at least a header row
        header = [cell.text.strip() if cell.text else '' for cell in rows[1].findall('ss:Cell/ss:Data', ns)]

    # Update header for specific fields
    if 'Organizational Affiliation' in header:
        idx = header.index('Organizational Affiliation')
        header[idx] = 'Organizational Affiliation Hebrew'
        header.insert(idx + 1, 'Organizational Affiliation English')
    header.append('bank account hebrew')
    header.append('bank account english')

    # Iterate through each data row starting from row 3
    for i, row in enumerate(rows[2:], start=1):
        # Dictionary for this row's data
        row_data = {}
        cells = row.findall('ss:Cell', ns)

        # Track the current position in the row
        current_col = 0
        
        for cell in cells:
            # Check if the cell has an index attribute (meaning it's skipping columns)
            index = cell.get(f'{{{ns["ss"]}}}Index')
            if index is not None:
                current_col = int(index) - 1  # Set the column index (0-based)
            else:
                # If no index is found, we assume sequential filling
                current_col = len(row_data)  # Fill at the next available position

            # Get cell data text or use an empty string if missing
            cell_data = cell.find('ss:Data', ns)
            cell_text = cell_data.text.strip() if cell_data is not None and cell_data.text else ''

            # Set value to None if the cell is empty or contains '-'
            row_data[header[current_col]] = None if cell_text == '-' or cell_text == '' else cell_text

        # Fill in any remaining headers with None if the row is short
        for j in range(current_col + 1, len(header)):
            row_data[header[j]] = None

        # Add row data to main dictionary with row index as key, only if 'Number' is not '-'
        if row_data.get('Number') != '-':
            data_dict[i] = row_data

    return data_dict


def convert_date_to_ymd(date_str):
    date_str = re.split(r"[T ]", date_str)[0]
    # Try parsing with different possible formats
    for fmt in ("%d/%m/%Y", "%d.%m.%Y", "%d-%m-%Y", "%Y-%m-%d", "%Y.%m.%d", "%Y/%m/%d"):
        try:
            # Parse the date and format to 'YYYY/MM/DD'
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    # If the date format is not recognized, raise an error or handle accordingly
    return None
