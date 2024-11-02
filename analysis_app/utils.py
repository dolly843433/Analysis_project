import xml.etree.ElementTree as ET


def xml_to_dict(element):
    # Namespace to use for finding elements
    ns = {'ss': 'urn:schemas-microsoft-com:office:spreadsheet'}

    # Dictionary to store data
    data_dict = {}

    # Find all rows in the sheet
    rows = element.findall('.//ss:Row', ns)

    # Extract header (row 2) for keys if available
    header = []
    if len(rows) > 1:  # Make sure there's at least a header row
        header = [cell.text.strip() for cell in rows[1].findall('ss:Cell/ss:Data', ns) if cell.text]
    idx = header.index('Organizational Affiliation')
    header[idx] = 'Organizational Affiliation Hebrew'
    header.insert(idx + 1, 'Organizational Affiliation English')
    header.insert(len(header), 'bank account hebrew')
    header.insert(len(header), 'bank account english')
    # Iterate through each data row starting from row 3
    for i, row in enumerate(rows[2:], start=1):
        # Dictionary for this row's data
        row_data = {}
        for j, cell in enumerate(row.findall('ss:Cell/ss:Data', ns)):
            # Only map cells where there's a header key
            if j < len(header) and cell.text:
                row_data[header[j]] = cell.text.strip()
        # Add row data to main dictionary with row index as key
        if row_data['Number'] != '-':
            data_dict[i] = row_data

    return data_dict

