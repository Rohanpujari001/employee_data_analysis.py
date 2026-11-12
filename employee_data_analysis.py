
# =====================================================
#       EMPLOYEE DATA ANALYSIS PROJECT
#              WEEK 4 CAPSTONE
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt
import os


# 1. FILE CONFIGURATION
FILE_NAME = "employees.csv"


# 2. CREATE SAMPLE DATASET
def create_dataset():

    if not os.path.exists(FILE_NAME):

        data = {
            "EmployeeID": [101, 102, 103, 104, 105,
                           106, 107, 108, 109, 110],

            "Name": ["Rohan", "Rahul", "Amit", "Priya",
                     "Sneha", "Vikas", "Neha", "Akash",
                     "Pooja", "Karan"],

            "Age": [24, 27, 25, 29, 26,
                    30, 28, 23, 31, 27],

            "Department": ["IT", "HR", "Finance", "IT",
                           "Sales", "Finance", "HR", "IT",
                           "Sales", "IT"],

            "Salary": [35000, 28000, 42000, 50000, 32000,
                       60000, 30000, 25000, 45000, 55000],

            "City": ["Pune", "Mumbai", "Delhi", "Pune",
                     "Mumbai", "Delhi", "Pune", "Nashik",
                     "Mumbai", "Pune"]
        }

        df = pd.DataFrame(data)

        df.to_csv(FILE_NAME, index=False)

        print("Sample Dataset Created Successfully!")


# 3. LOAD CSV DATA
def load_data():

    try:

        df = pd.read_csv(FILE_NAME)

        print("\nEmployee Dataset Loaded Successfully!")

        return df

    except FileNotFoundError:

        print("Dataset File Not Found!")

        return None

    except pd.errors.EmptyDataError:

        print("Dataset is Empty!")

        return None


# 4. DISPLAY EMPLOYEE DATA
def display_data(df):

    print("\n========== EMPLOYEE RECORDS ==========")

    print(df.to_string(index=False))

    print("\nTotal Employees:", len(df))


# 5. AVERAGE SALARY
def average_salary(df):

    avg = df["Salary"].mean()

    print("\n========== AVERAGE SALARY ==========")

    print("Average Employee Salary: Rs.", round(avg, 2))


# 6. DEPARTMENT-WISE EMPLOYEE COUNT
def department_count(df):

    print("\n========== DEPARTMENT-WISE COUNT ==========")

    result = df["Department"].value_counts()

    print(result.to_string())

    return result


# 7. FILTER EMPLOYEES BY SALARY
def filter_salary(df):

    print("\n========== SALARY FILTER ==========")

    try:

        threshold = float(
            input("Enter Minimum Salary: Rs. ")
        )

        filtered = df[df["Salary"] > threshold]

        if filtered.empty:

            print("No Employees Found Above This Salary!")

        else:

            print("\nEmployees Earning Above Rs.", threshold)

            print(filtered.to_string(index=False))

            filtered.to_csv(
                "high_salary_employees.csv",
                index=False
            )

            print("\nFiltered Data Exported Successfully!")

    except ValueError:

        print("Please Enter a Valid Salary!")


# 8. HIGHEST AND LOWEST SALARY
def salary_analysis(df):

    highest = df.loc[df["Salary"].idxmax()]

    lowest = df.loc[df["Salary"].idxmin()]

    print("\n========== SALARY ANALYSIS ==========")

    print("\nHighest Paid Employee:")
    print("Name:", highest["Name"])
    print("Department:", highest["Department"])
    print("Salary: Rs.", highest["Salary"])

    print("\nLowest Paid Employee:")
    print("Name:", lowest["Name"])
    print("Department:", lowest["Department"])
    print("Salary: Rs.", lowest["Salary"])


# 9. DEPARTMENT-WISE SALARY ANALYSIS
def department_salary(df):

    result = df.groupby("Department")["Salary"].mean()

    print("\n========== DEPARTMENT SALARY ==========")

    print(result.to_string())


# 10. CREATE BAR CHART
def create_chart(df):

    print("\nGenerating Department Chart...")

    department_data = df.groupby(
        "Department"
    )["Salary"].mean()

    plt.figure(figsize=(9, 5))

    department_data.plot(
        kind="bar",
        title="Average Salary by Department"
    )

    plt.xlabel("Department")
    plt.ylabel("Average Salary (Rs.)")

    plt.xticks(rotation=0)

    plt.tight_layout()

    plt.savefig("department_salary_chart.png")

    print("Chart Saved as department_salary_chart.png")

    plt.show()


# 11. EXPORT COMPLETE DATA
def export_data(df):

    df.to_csv("employee_analysis_report.csv", index=False)

    print("\nComplete Employee Data Exported Successfully!")

    print("File Name: employee_analysis_report.csv")


# 12. MAIN PROGRAM
def main():

    create_dataset()

    df = load_data()

    if df is None:
        return

    # Validate required columns
    required_columns = [
        "EmployeeID", "Name", "Age",
        "Department", "Salary", "City"
    ]

    if not all(column in df.columns for column in required_columns):

        print("Dataset does not contain all required columns!")
        return

    # Convert salary into numeric values
    df["Salary"] = pd.to_numeric(
        df["Salary"], errors="coerce"
    )

    df.dropna(subset=["Salary"], inplace=True)

    while True:

        print("\n======================================")
        print("       EMPLOYEE DATA ANALYSIS")
        print("======================================")

        print("1. Display Employee Data")
        print("2. Calculate Average Salary")
        print("3. Department-Wise Employee Count")
        print("4. Filter Employees by Salary")
        print("5. Highest and Lowest Salary")
        print("6. Department-Wise Salary Analysis")
        print("7. Generate Salary Chart")
        print("8. Export Complete Data")
        print("9. Exit")

        choice = input("\nEnter Your Choice (1-9): ")

        if choice == "1":

            display_data(df)

        elif choice == "2":

            average_salary(df)

        elif choice == "3":

            department_count(df)

        elif choice == "4":

            filter_salary(df)

        elif choice == "5":

            salary_analysis(df)

        elif choice == "6":

            department_salary(df)

        elif choice == "7":

            create_chart(df)

        elif choice == "8":

            export_data(df)

        elif choice == "9":

            print("\nThank You for Using Employee Data Analysis!")
            print("Project Closed Successfully!")

            break

        else:

            print("\nInvalid Choice! Please Select 1-9.")


# 13. PROGRAM EXECUTION
if __name__ == "__main__":

    main()


# =====================================================
#                   END OF PROJECT
# =====================================================
