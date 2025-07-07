class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def paint(self, new_color):
        self.color = new_color

    def add_room(self):
        self.rooms += 1

    def show_details(self):
        print(f"Color: {self.color}, Rooms: {self.rooms}")

result=House("yellow",3)
result.paint("white")
result.add_room()
result.show_details()
