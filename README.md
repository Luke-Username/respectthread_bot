# respectthread_bot

---

### Dependencies

- [**Python**](https://www.python.org/downloads/) (Programming Language)

- [**PostgreSQL**](https://www.postgresql.org/download/) (Database Management System)

- [**PRAW**](https://praw.readthedocs.io/en/latest/getting_started/installation.html) (Python Library for Reddit)

- [**Psycopg2**](http://initd.org/psycopg/download/) (Python Library for PostgreSQL)

---

### What does respectthread_bot do?

- Automatically link **respect threads** on WhoWouldWin posts 
if the post hasn't linked the same thread already.

- Uses its database to determine which threads to link.

### What's a respect thread?

From [r/respectthreads](https://www.reddit.com/r/respectthreads/) sidebar:

> A Respect Thread is an educational resource meant to provide usable information 
on a character's capabilities for the purpose of "Who would win in a fight?"-style debate. 
Respect Threads should be clear, concise, and accurately portray the character in question.

Examples:

- [Respect Spider-Man](https://redd.it/cjhe01)

- [Respect Pikachu](https://redd.it/c22a7b)

- [Respect Mario](https://redd.it/9x1vll)

- [Respect Voldemort](https://redd.it/7xliez)

- [Respect John Wick](https://redd.it/hsx48x)

### Why make this bot?

WhoWouldWin posts often don't link RTs even though they're a good source of information.
By linking them, debaters can read them and be more informed on the characters they're debating.

### How does respectthread_bot work?

It looks at new posts on [r/whowouldwin](https://www.reddit.com/r/whowouldwin/). For each post,
it looks for a matching character name in its database,
and if it finds one, it then looks for what version the character is.
If both the character name and version name matches, 
it will link the corresponding respect thread.
Note that the database has to be populated and kept up to date *manually* to make sure results are correct.

There are other features to help prevent false positives,
to prevent linking threads that have already been linked,
and to link RTs when a version isn't specified.
