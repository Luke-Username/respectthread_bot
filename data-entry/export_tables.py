# This script exports each table in the database to a CSV format.
# The CSVs can be used in case a backup of the data is needed.
# They are formatted as such: HEADER TRUE, QUOTE '\"', ESCAPE '`'.
# This script should be run fairly frequently when changes to the database are made.

# Modules
import os                           # To get the absolute path for exporting
import psycopg2                     # Interface with PostgreSQL
import sys                          # For terminal arguments and to import from different folders
sys.path.insert(1, "../main-bot")   # This path is to import modules the bot uses. It is relative to the shell script that runs the tests.

# Custom modules
import config

con = psycopg2.connect(
            host = config.host,
            database = config.database,
            user = config.d_user,
            password = config.d_password
)
cur = con.cursor()

csv_format = "(FORMAT CSV, HEADER TRUE, QUOTE '\"', ESCAPE '`')"
relative_export_path = "../csv-data"
export_path = os.path.abspath(relative_export_path)
export_respectthread = "COPY respectthread TO '{}/respectthread_data.csv' WITH {};".format(export_path, csv_format)
print("respectthread exported.")
export_character = "COPY character TO '{}/character_data.csv' WITH {};".format(export_path, csv_format)
print("character exported.")
export_character_name = "COPY character_name TO '{}/character_name_data.csv' WITH {};".format(export_path, csv_format)
print("character_name exported.")
export_name_conflict = "COPY name_conflict TO '{}/name_conflict_data.csv' WITH {};".format(export_path, csv_format)
print("name_conflict exported.")
query = export_respectthread + export_character + export_character_name + export_name_conflict 
cur.execute(query)
con.commit()
print("Tables exported.")

# Close the cursor and connection
cur.close()
con.close()
