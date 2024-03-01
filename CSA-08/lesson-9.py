import pandas as pd
data = {
    'ID': [1,2,3],
    'Names': ["Nguyen Van A", "Tran van V", "Vu Thi C"],
    'City': ['Hanoi', 'TPHCM', 'DaNang'] 
}
df = pd.DataFrame(data)
# print(df)

# df.to_excel("data.xlsx", index=False)

# TRUY XUẤT DỮ LIỆU

# THEO CỘT
print(df['ID'])

# THEO HÀNG
# iloc loc
print(df.iloc[0])
print(df.iloc[0,2])

print(df.loc[df['Names'] == 'Nguyen Van A'])
print(df.loc[df['ID'] == 2])


