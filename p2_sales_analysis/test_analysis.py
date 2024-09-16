import unittest
from io import StringIO

import pandas as pd
from pandas.testing import assert_frame_equal

from analysis import (
    calculate_total_sales,
    filter_sales_by_date,
    group_sales_by_month,
    load_sales_data,
)


class TestAnalysis(unittest.TestCase):
    def setUp(self):
        csv_data = StringIO("""
date,product,quantity,price,total
2023-01-15,Product A,2,10.00,20.00
2023-02-20,Product B,3,15.00,45.00
2023-03-10,Product C,1,25.00,25.00
2023-01-05,Product D,5,8.00,40.00
""")
        self.df = pd.read_csv(csv_data)

        self.df["date"] = pd.to_datetime(self.df["date"])

    def test_load_sales_data(self):
        """Test if load_sales_data can correctly load data."""
        csv_data = StringIO("""
date,product,quantity,price,total
2023-01-15,Product A,2,10.00,20.00
2023-02-20,Product B,3,15.00,45.00
""")
        df = load_sales_data(csv_data)

        self.assertEqual(len(df), 2)
        self.assertListEqual(
            list(df.columns), ["date", "product", "quantity", "price", "total"]
        )

    def test_filter_sales_by_date(self):
        """Test if filter_sales_by_date filters data within a date range."""
        start_date = "2023-01-01"
        end_date = "2023-01-31"

        filtered_df = filter_sales_by_date(self.df, start_date, end_date)

        expected_data = {
            "date": pd.to_datetime(["2023-01-15", "2023-01-05"]),
            "product": ["Product A", "Product D"],
            "quantity": [2, 5],
            "price": [10.00, 8.00],
            "total": [20.00, 40.00],
        }
        expected_df = pd.DataFrame(expected_data)

        assert_frame_equal(filtered_df.reset_index(drop=True), expected_df)

    def test_group_sales_by_month(self):
        """Test if group_sales_by_month groups data correctly by month."""
        grouped_sales = group_sales_by_month(self.df)

        expected_sales = {"2023-01": 60.00, "2023-02": 45.00, "2023-03": 25.00}

        for period, total in expected_sales.items():
            self.assertEqual(grouped_sales[period], total)

    def test_calculate_total_sales(self):
        """Test if calculate_total_sales correctly sums all sales."""
        total_sales = calculate_total_sales(self.df)

        self.assertEqual(total_sales, 130.00)


if __name__ == "__main__":
    unittest.main()
