class libraryItem:
    def __init__(self, library_item_id, title, location, checked_out, requested_by, date_checked_out ):
        self._library_item_id = library_item_id
        self._title = title
        self._location = location
        self._checked_out = checked_out
        self._requested_by = requested_by
        self._date_checked_out = date_checked_out

    def get_library_item_id(self):
        return self._library_item_id

    def set_library_item_id(self, new_id):
        self._library_item_id =  new_id

    def get_title(self):
        return self._title
    def set_title(self, new_title):
        self._title = new_title

    def get_location(self):
        return self._location

    def set_location(self):
        


        
      


class Book(libraryItem):
    super().__init__()