import pandas as pd
import sqlite3
from job_scraper import ScraperJobs


def main():
    print("Hello from jobspy!")

    searches = ["data analyst", "data scientist", "data engineer"]
    sites = ["indeed"]
    results = 1000
    old = 1000
    country = "USA"

    scraper_obj = ScraperJobs()
    df = scraper_obj.scraper_jobs(searches, sites, results, old, country)

    # Guardar datos en SQL
    db_connection = sqlite3.connect("jobs.db")
    df.to_sql("jobs_raw_table", db_connection, if_exists="append", index=False)
    db_connection.close

    # Guardar datos en CSV
    df.to_csv("jobs_raw_table.csv")


if __name__ == "__main__":
    main()
