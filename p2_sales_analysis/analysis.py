import pandas as pd


def load_sales_data(file_path):
    return pd.read_csv(file_path)


def filter_sales_by_date(df, start_date, end_date):
    df["date"] = pd.to_datetime(df["date"])
    return df[(df["date"] >= start_date) & (df["date"] <= end_date)]


def group_sales_by_month(df):
    df["date"] = pd.to_datetime(df["date"])
    df["year_month"] = df["date"].dt.to_period("M")
    return df.groupby("year_month")["total"].sum()


def calculate_total_sales(df):
    return df["total"].sum()


def main():
    df = load_sales_data("data/sales_data.csv")

    start_date = "2023-01-05"
    end_date = "2023-05-18"

    filtered_data = filter_sales_by_date(df, start_date, end_date)
    grouped_data = group_sales_by_month(filtered_data)
    total_sales = calculate_total_sales(df)

    print("Grouped Sales:")
    print(grouped_data)
    print(f"Total: {total_sales}")


if __name__ == "__main__":
    main()
