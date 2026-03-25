import pandas as pd
import json

df = pd.read_csv("expenses.csv")

df['Date'] = pd.to_datetime(df['Date'])

df['Date'] = df['Date'].astype(str)

print("Original Data:\n")
print(df)

total_expense = df['Amount'].sum()

highest_expense = df.loc[df['Amount'].idxmax()].to_dict()

lowest_expense = df.loc[df['Amount'].idxmin()].to_dict()

df['Month'] = pd.to_datetime(df['Date']).dt.month
monthly_expense = df.groupby('Month')['Amount'].sum().to_dict()

df.to_csv("processed_expenses.csv", index=False)

summary = {
    "Total Expense": int(total_expense),
    "Highest Expense": highest_expense,
    "Lowest Expense": lowest_expense,
    "Monthly Expense": monthly_expense
}

with open("expenses_summary.json", "w") as file:
    json.dump(summary, file, indent=4)

print("\n===== SUMMARY =====")
print("Total Expense:", total_expense)

print("\nHighest Expense:")
print(highest_expense)

print("\nLowest Expense:")
print(lowest_expense)

print("\nMonthly Expense:")
print(monthly_expense)

print("\nData successfully processed!")