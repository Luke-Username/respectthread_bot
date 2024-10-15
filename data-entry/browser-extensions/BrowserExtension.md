Adding these custom browser extensions to help copy respect thread titles and URLs to clipboard while adding them to the database.

eg. 
```Python
id = get_rt_id(cur, 'Respect Sully (Monsters, Inc.)', 'https://redd.it/d2kwip')
```

Will want to escape apostrophes (') for Postgres
```Python
> id = get_rt_id(cur "Respect Dio Brando (JoJo''s Bizarre Adventure)", 'https://redd.it/4rjh9z')
```

The Chrome one should theoretically work in any Chromium browser, but I've only tested in Brave.
