import pandas as pd
import re

# Read the extracted text content
file_path = "C:/Users/KIIT/Desktop/haryana.pdf"

# Read the text manually (already extracted in previous step)
with open(file_path, "rb") as f:
    content = f.read().decode(errors="ignore")

# Extract institute names using regex pattern
pattern = re.compile(r"\d-\d+\s+([A-Z][A-Z0-9\s\.\-&']+(?:INSTITUTE|COLLEGE|UNIVERSITY|SCHOOL|POLYTECHNIC|GROUP|DEPARTMENT|ACADEMY|INSTITUTION|TRUST)[A-Z0-9\s\.\-&']*)")
matches = pattern.findall(content)

# Clean and prepare the data
colleges = [name.strip().title() for name in matches if len(name.strip()) > 4]
df = pd.DataFrame(colleges, columns=["College Name"])

# Save to Excel
excel_path = "C:/Users/KIIT/Desktop/haryana_colleges_list.xlsx"
df.to_excel(excel_path, index=False)

excel_path
