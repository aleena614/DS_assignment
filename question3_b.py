
import pandas as pd

# Create a DataFrame of six students
data = {
    "Name": ["Aleena", "Ahmed", "Sana", "Bilal", "Hira", "Usman"],
    "Section": ["A", "A", "B", "B", "A", "B"],
    "City": ["Kamra", "Attock", "Kamra", "Attock", "Rawalpindi", "Kamra"],
    "Marks": [85, 72, 90, 55, 78, 65]
}

dfOrbit = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(dfOrbit)

# (i) Students with marks greater than 70
print("\nStudents with marks greater than 70:")
print(dfOrbit[dfOrbit["Marks"] > 70])

# (ii) Average marks of each section
print("\nAverage marks of each section:")
print(dfOrbit.groupby("Section")["Marks"].mean())

# (iii) Add the Grade column
dfOrbit["Grade"] = dfOrbit["Marks"].apply(
    lambda marks: "A" if marks >= 80
    else "B" if marks >= 60
    else "C"
)

print("\nDataFrame with grades:")
print(dfOrbit)

# (iv) Sort by marks in descending order
dfOrbit = dfOrbit.sort_values(
    by="Marks", ascending=False
)

print("\nDataFrame sorted by marks:")
print(dfOrbit)

dfOrbit['Name'] = dfOrbit['Name'].str.strip()
