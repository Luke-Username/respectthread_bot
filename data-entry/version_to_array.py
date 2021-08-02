# This script was used to convert all strings from the 'version' column of the 'character' table
# into an array of one element. This is done because we want the bot to check multple regular expressions
# when evaluating each post, rather than just two.
# The script should only have been run once to change the database's schema,
# so the script is now commented out entirely.

"""
import psycopg2         # Interface with PostgreSQL
import config           # Login details

con = psycopg2.connect(
            host = config.host,
            database = config.database,
            user = config.d_user,
            password = config.d_password
)
cur = con.cursor()

cur.execute("SELECT DISTINCT version FROM character;")
rows = cur.fetchall()
for version in rows:
    version_array = '{"' + version[0] + '"}'
    cur.execute("UPDATE character SET version = '{}' WHERE version = '{}';".format(version_array, version[0]))
cur.execute("ALTER TABLE character ALTER COLUMN version TYPE text[] USING version::text[];")
con.commit()

# Close the cursor and connection
cur.close()
con.close()
"""