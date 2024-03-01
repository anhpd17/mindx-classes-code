import pandas as pd

# Đọc dữ liệu từ các sheet CHN, LAO, KHM trong file Excel
xls = pd.ExcelFile('E:\\CODING\\mindX\\Classes\\CSA-08\\pandas_overview\\borders.xls')
df_chn = pd.read_excel(xls, 'CHN')
df_lao = pd.read_excel(xls, 'LAO')
df_khm = pd.read_excel(xls, 'KHM')

# Tạo DataFrame df từ các dữ liệu
df = pd.DataFrame(columns=['Name', 'BorderWith', 'BorderCount'])

# Thêm dữ liệu từ sheet CHN
df_chn.rename(columns={'Tên tỉnh': 'Name', 'Tên địa phương giáp biên': 'BorderWith'}, inplace=True)
df_chn['BorderWith'] = 'Trung Quốc'
df = pd.concat([df, df_chn[['Name', 'BorderWith']]])

# Thêm dữ liệu từ sheet LAO
df_lao.rename(columns={'Tên tỉnh': 'Name', 'Tên địa phương giáp biên': 'BorderWith'}, inplace=True)
df_lao['BorderWith'] = 'Lào'
df = pd.concat([df, df_lao[['Name', 'BorderWith']]])

# Thêm dữ liệu từ sheet KHM
df_khm.rename(columns={'Tên tỉnh': 'Name', 'Tên địa phương giáp biên': 'BorderWith'}, inplace=True)
df_khm['BorderWith'] = 'Campuchia'
df = pd.concat([df, df_khm[['Name', 'BorderWith']]])


# Đếm số nước có biên giới giáp tỉnh
df['BorderCount'] = df.groupby('Name')['BorderWith'].transform('count')
df['BorderWith'] = df.groupby('Name')['BorderWith'].transform(', '.join)

df.drop_duplicates(inplace=True)
# Lọc các tỉnh có BorderCount = 2
df_filtered = df.loc[df['BorderCount'] == 2]

# Hiển thị các tỉnh đã lọc
print(df_filtered)

