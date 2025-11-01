import pandas as pd

df = pd.read_csv("C:/Users/Student/Desktop/zunaira/pythonprogramming/pythonprogramming/1112025/sampleData.csv")
dept_avg = df.groupby("Department")["Bill-Amount"].mean().round(2)
highest = df.loc[df["Bill-Amount"].idxmax()]

summary = dept_avg.reset_index()
summary.columns = ["Department","AverageBill"]


with open("hospital_summary.csv", "w", newline="") as f:
    summary.to_csv(f, index=False)
    f.write("\n")  # blank line
    f.write(f"Highest Paying Patient,{highest['PatientID']},{highest['Bill-Amount']:.2f}\n")

print("✅ Summary written to hospital_summary.csv successfully.")