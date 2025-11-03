import pandas as pd

# Function to clean a CSV file
print("=== CSV Data Cleaner ===\n")

def clean_csv(file_path):
    df = pd.read_csv(file_path)
    print("Before cleaning:", len(df), "rows")

    # Remove duplicates
    df = df.drop_duplicates()

    # Trim whitespace from text columns
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.strip()

    print("After cleaning:", len(df), "rows")
    print("\nMissing values per column:")
    print(df.isna().sum())
    df.to_csv("cleaned.csv", index=False)
    print("Cleaned file saved as cleaned.csv")

# Run the function using the sample file
file_name = input("Enter the CSV file name (for example, sample.csv): ")
clean_csv(file_name)

input("Press Enter to close...")
