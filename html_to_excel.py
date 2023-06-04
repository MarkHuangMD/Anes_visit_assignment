import pandas as pd

## chapt GPT This code assumes that the HTML table is structured using the <table>, <tr>, and <td> tags. 
# If your HTML structure is different, you may need to modify the code to target the correct table element. 
# Additionally, ensure that the number of columns in the table matches your expected 11 columns.
# 所以我打開 .html 的原始碼看 => 確認是 <table> lable 沒有錯


# Read the HTML file and extract the tables
# Encoding with utf-8 for traditional Chineses character

PGY_tables = pd.read_html('PGY.html', encoding='utf-8')  # Adjust the encoding to match your HTML file C:/Users/User/Desktop/Anes_assignemnt_Program/
R_tables = pd.read_html('R.html', encoding='utf-8')  # Adjust the encoding to match your HTML file

# Assuming the desired table is the first one
df1 = PGY_tables[0]
df2 = R_tables[0]

# Write the DataFrame to an Excel file
df1.to_excel('PGY.xlsx', index=False, encoding='utf-8')  # Adjust the output file path and encoding
df2.to_excel('R.xlsx', index=False, encoding='utf-8')  # Adjust the output file path and encoding

## ok 2023.05.28 test 成功 ##
## 記得換檔名就好 ##

# Merge two files
merged_df = pd.concat([df1, df2])
output_file_path = 'need_to_visit.xlsx'
merged_df.to_excel(output_file_path, index=False)

print("Merged data exported to", output_file_path)