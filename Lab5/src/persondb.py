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