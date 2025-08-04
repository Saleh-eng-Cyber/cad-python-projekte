import FreeCAD as App
import Part

breite=100
hoehe=75
punkt1=App.Vector(0,0,0)
punkt2=App.Vector(breite,0,0)
punkt3=App.Vector(breite,hoehe,0)
punkt4=App.Vector(0,hoehe,0)


k1=Part.LineSegment(punkt1,punkt2).toShape()
k2=Part.LineSegment(punkt2,punkt3).toShape()
k3=Part.LineSegment(punkt3,punkt4).toShape()
k4=Part.LineSegment(punkt4,punkt1).toShape()

rechteck=Part.Compound([k1,k2,k3,k4])

Part.show(rechteck)