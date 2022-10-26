import sqlite3
from sqlite3 import Error

# part 3


class PersonDB():
    def __init__(self, db_file=''):
        """Store DB file."""
        self.db_file = db_file

    def __enter__(self):
        """
        Method called when class object of type PersonDB is used within a “with” context.
        Initiates connection to DB indicated by self.db_file.
        """
        self.conn = sqlite3.connect(self.db_file)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Method called after the last line of a with block is executed."""
        self.conn.close()

    def load_person(self, id):
        """Load a `people` record by ID."""
        sql = "SELECT * FROM people WHERE id=?"
        cursor = self.conn.cursor()
        cursor.execute(sql, (id,))
        records = cursor.fetchall()
        # Note: the execute command accepts the sql command string and a tuple of parameters to
        # substitute for the question marks in the command string.
        # Notice the comma with nothing after it? That is to ensure (id,) results in a tuple,
        # not a single evaluated value.

        result = (-1, '', '')  # id = -1, first_name = '', last_name = ''
        if records is not None and len(records) > 0:
            result = records[0]

        cursor.close()
        return result


def test_PersonDB(db_file):
    with PersonDB(db_file) as db:
        print(db.load_person(10000))  # Should print the default
        print(db.load_person(122))
        print(db.load_person(300))


if __name__ == "__main__":
    people_db_file = "sqlite.db"
    test_PersonDB(people_db_file)


# Return of this file:
# (-1, '', '')
# (122, 'JAMIE', 'PHILLIPS')
# (300, 'BESS', 'CRANE')
