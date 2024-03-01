import pandas as pd

data = {
    'StudentID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [21, 22, 20, 23, 21],
    'Grade': [85, 90, 78, 95, 88],
    'Subject': ['Math', 'English', 'History', 'Physics', 'Chemistry']
}

df = pd.DataFrame(data)

# 1
# print(df.info())
# print(df.describe())

# 2
# older_than_21 = df[df['Age'] > 21][['Name', 'Grade']]
# print(older_than_21)

# 3
# average_age = df['Age'].mean()
# print(average_age)

# 4
# above_85_grade = df[df['Grade'] > 85]
# print(above_85_grade)

# 5
# subject_counts = df['Subject'].value_counts()
# print(subject_counts)


# 6
# a = df.loc[df['Grade'].idxmax(), 'Name']

# print(a)

# # 7
print(df[(df['Age'] > 21) & (df['Grade'] > 85)])