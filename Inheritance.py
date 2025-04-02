class rectangle:
    def rec_area(self,length,width):
        area=length*width
        print("Area of a Rectangle:",area)
class circle(rectangle):
    def cir_area(self,radius):
        area=3.14*radius*radius
        print("Area of Circle:",area)
class triangle(circle):
    def tri_area(self,breadth,height):
        area=0.5*breadth*height
        print("Area of Triangle:",area)

obj=triangle()
obj.rec_area(12,8)
obj.cir_area(10)
obj.tri_area(9,15)
        
