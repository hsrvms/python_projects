import datetime
import random

import pandas as pd

products = [
    "Product A",
    "Product B",
    "Product C",
    "Product D",
    "Product E",
    "Product F",
]


def generate_random_date(start, end):
    return start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )


def generate_sales_data(num_rows, start_date, end_date):
    data = {
        "date": [
            generate_random_date(start_date, end_date).strftime("%Y-%m-%d")
            for _ in range(num_rows)
        ],
        "product": [random.choice(products) for _ in range(num_rows)],
        "quantity": [random.randint(1, 10) for _ in range(num_rows)],
        "price": [
            round(random.uniform(5.00, 100.00), 2) for _ in range(num_rows)
        ],
    }

    df = pd.DataFrame(data)
    df["total"] = df["quantity"] * df["price"]
    return df


def save_sales_data_to_csv(num_rows, file_path):
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 12, 31)

    df = generate_sales_data(num_rows, start_date, end_date)
    df.to_csv(file_path, index=False)
    print(f"CSV file generated successfully: {file_path}")


if __name__ == "__main__":
    save_sales_data_to_csv(1000, "data/sales_data.csv")
