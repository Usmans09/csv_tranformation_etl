import data_transformation
import extract_data
import postgres_loader


def main():
    try:
        print("ETL Pipeline Started..........")

        df = extract_data.extract_data("Data/customers-10000.csv")

        if df is None:
            print("Extraction failed. Stopping pipeline.")
            return

        df = data_transformation.column_cleaning(df)
        df = data_transformation.duplicate_handling(df)
        df = data_transformation.handle_missing_values(df)
        df = data_transformation.type_conversion(df)

        print("Data transformation completed.")

        connection = postgres_loader.get_postgres_connection()

        if connection is None:
            print("Database connection failed. Stopping pipeline.")
            return

        cursor = connection.cursor()

        postgres_loader.create_table(cursor)
        postgres_loader.insert_data(connection, cursor, df)

        cursor.close()
        connection.close()

        print("ETL Pipeline Execution Completed Successfully")

    except Exception as e:
        print(f"Pipeline failed due to error: {e}")


if __name__ == "__main__":
    main()
