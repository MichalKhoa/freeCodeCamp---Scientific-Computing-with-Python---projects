class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        if self.width == self.height:
            self.width = width
            self.height = width
        else:
            self.width = width

    def set_height(self, height):
        if self.height == self.width:
            self.height = height
            self.width = height
        else:
            self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*self.height + 2*self.width

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        picture = ""
        if self.width >= 50 or self.height >= 50:
            return "Too big for picture."
        for i in range(self.height):
            for j in range(self.width):
                picture += "*"
            picture += "\n"
        return picture

    def get_amount_inside(self, shape):
        amount_inside_horizontally = self.width//shape.width
        amount_inside_vertically = self.height//shape.height
        return amount_inside_horizontally * amount_inside_vertically

    def __str__(self):
        if self.width != self.height:
            return str("Rectangle(width={0}, height={1})".format(self.width, self.height))
        elif self.width == self.height:
            return str("Square(side={0})".format(self.width))


class Square(Rectangle):

    def __init__(self, side_length):
        super().__init__(width=side_length, height=side_length)

    def set_side(self, side_length):
        self.width = side_length
        self.height = self.width
