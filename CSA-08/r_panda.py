# Tạo 1 dataframe chứa các thông tin của các cột:
#     ID, Name, Age, Address, Email
    
# Tạo 10 dữ liệu với các cột trên

# 1. Truy xuất thông tin của những người có tuổi trên 25
# 2. Truy xuất thông tin của cột 'Name'
# 3. Truy xuất thông tin của người có độ tuổi lớn nhất

import pandas as pd
data = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 22, 35, 28],
    'Address': ['123 Main St', '456 Oak Ave', '789 Pine Ln', '101 Elm St', '202 Cedar Ave'],
    'Email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', 'david@email.com', 'emily@email.com']
}

df = pd.DataFrame(data)

# print(df.loc[df['Age'] > 25])

# print(df['Name'])

# ages = df['Age']
# max_age = ages.max()
# print(df.loc[df['Age'] == max_age])

# -------------  UPDATE  -------------------
df['Age'] = [25, 28, 22, 35, 28]
df.at[0, 'Age'] = 26


# ------------- CREATE/ADD -------------------
newData = {'ID': 6, 'Name': 'Fiona', 'Age': 29, 'Address': '303 Maple St', 'Email': 'fiona@email.com'}

df_dictionary = pd.DataFrame([newData])
df = pd.concat([df, df_dictionary], ignore_index=True)

df.loc[6] = [7, "ABC", 64, 'áds', 'ádkjasdh']

# df2 = df.append(df2, ignore_index=True)

# -------------- DELETE --------------------------------
# xóa hàng
df = df.drop(1)
# xóa cột
df = df.drop('ID', axis=1)

print(df)