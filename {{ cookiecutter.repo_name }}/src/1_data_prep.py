import pandas as pd
from simple_salesforce import Salesforce, format_soql
import os
from dotenv import load_dotenv
from ct_snippets.load_sf_class import SF_SOQL, SF_Report
from ct_snippets.sf_bulk import (
    sf_bulk,
    sf_bulk_handler,
    generate_data_dict,
    process_bulk_results,
)
from reportforce import Reportforce
import numpy as np
import soql_queries as soql
import variables


load_dotenv()


SF_PASS = os.environ.get("SF_PASS")
SF_TOKEN = os.environ.get("SF_TOKEN")
SF_USERNAME = os.environ.get("SF_USERNAME")

sf = Salesforce(username=SF_USERNAME, password=SF_PASS, security_token=SF_TOKEN)
rf = Reportforce(session_id=sf.session_id, instance_url=sf.sf_instance)


# Sample for loading from SOQL
# query = """ """
# data = SF_SOQL("data", query)
# data.load_from_sf_soql(sf)
# data.write_file()


# Sample for saving data
# data.write_file(subfolder="interim", file_type=".pkl")


# Sample for pushing data to SFDC
# data_dict = {"C_Id": "Id"}

# data = generate_data_dict(data.df, data_dict)
# results_df = sf_bulk("Contact", data, sf, batch_size=50, use_serial=True)
# fail_df = process_bulk_results(results_df, data.df)

