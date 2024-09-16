import datetime
import unittest

from generate_sales_data import generate_random_date, generate_sales_data


class TestGenerateSalesData(unittest.TestCase):
    def test_generate_random_date(self):
        """Test that the generate_random_date function returns a date within the specified range."""
        start_date = datetime.datetime(2023, 1, 1)
        end_date = datetime.datetime(2023, 12, 31)
        rand_date = generate_random_date(start_date, end_date)

        self.assertTrue(
            start_date <= rand_date <= end_date, "Random date is out of range"
        )

    def test_generate_sales_data_structure(self):
        """Test that the generated data has the correct structure and columns."""
        start_date = datetime.datetime(2023, 1, 1)
        end_date = datetime.datetime(2023, 12, 31)
        num_rows = 100

        df = generate_sales_data(num_rows, start_date, end_date)
        expectedColumns = ["date", "product", "quantity", "price", "total"]

        self.assertEqual(len(df), num_rows, "The number of rows does not match")
        self.assertListEqual(
            list(df.columns), expectedColumns, "The columns are not as expected"
        )

    def test_quantity_values(self):
        """Test that the quantity values are within the correct range."""
        start_date = datetime.datetime(2023, 1, 1)
        end_date = datetime.datetime(2023, 12, 31)
        num_rows = 100

        df = generate_sales_data(num_rows, start_date, end_date)

        self.assertTrue(
            df["quantity"].between(1, 10).all(), "Quantities are out of range."
        )

    def test_price_values(self):
        """Test that the price values are within the correct range."""
        start_date = datetime.datetime(2023, 1, 1)
        end_date = datetime.datetime(2023, 12, 31)
        num_rows = 100

        df = generate_sales_data(num_rows, start_date, end_date)
        self.assertTrue(
            df["price"].between(5.00, 100.00).all(), "Prices are out of range."
        )

    def test_total_calculation(self):
        """Test that the 'total' column is correctly calculated as quantity * price."""
        start_date = datetime.datetime(2023, 1, 1)
        end_date = datetime.datetime(2023, 12, 31)
        num_rows = 100

        df = generate_sales_data(num_rows, start_date, end_date)
        self.assertTrue(
            (df["total"] == df["quantity"] * df["price"]).all(),
            "'total' column is not calculated correctly",
        )


if __name__ == "__main__":
    unittest.main()
