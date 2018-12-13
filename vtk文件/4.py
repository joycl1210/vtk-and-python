import vtk

cube=vtk.vtkCubeSource()
cube.SetCenter(0.0,0.0,0.0)
cube.SetXLength(10)
cube.SetZLength(10)
cube.SetYLength(10)

cubeMapper = vtk.vtkPolyDataMapper()
cubeMapper.SetInputConnection(cube.GetOutputPort())

cubeActor = vtk.vtkActor()
cubeActor.SetMapper(cubeMapper)
cubeActor.GetProperty().SetColor(1.0,1.0,1.0)

point1_1=vtk.vtkCylinderSource()
point1_1.SetCenter(0.0,2.0,0.0)
point1_1.SetHeight(6.2)
point1_1.SetRadius(1.8)
point1_1.SetResolution(16)

point1_1Mapper=vtk.vtkPolyDataMapper()
point1_1Mapper.SetInputConnection(point1_1.GetOutputPort())

point1_1Actor = vtk.vtkActor()
point1_1Actor.SetMapper(point1_1Mapper)
point1_1Actor.GetProperty().SetColor(1.0,0.0,0.0)

point6_1=vtk.vtkCylinderSource()
point6_1.SetCenter(1.5,-2.0,2.5)
point6_1.SetHeight(6.2)
point6_1.SetRadius(1)
point6_1.SetResolution(16)

point6_1Mapper=vtk.vtkPolyDataMapper()
point6_1Mapper.SetInputConnection(point6_1.GetOutputPort())

point6_1Actor = vtk.vtkActor()
point6_1Actor.SetMapper(point6_1Mapper)
point6_1Actor.GetProperty().SetColor(1.0,0.0,0.0)

point6_2=vtk.vtkCylinderSource()
point6_2.SetCenter(1.5,-2.0,0.0)
point6_2.SetHeight(6.2)
point6_2.SetRadius(1)
point6_2.SetResolution(16)

point6_2Mapper=vtk.vtkPolyDataMapper()
point6_2Mapper.SetInputConnection(point6_2.GetOutputPort())

point6_2Actor = vtk.vtkActor()
point6_2Actor.SetMapper(point6_2Mapper)
point6_2Actor.GetProperty().SetColor(1.0,0.0,0.0)

point6_3=vtk.vtkCylinderSource()
point6_3.SetCenter(1.5,-2.0,-2.5)
point6_3.SetHeight(6.2)
point6_3.SetRadius(1)
point6_3.SetResolution(16)

point6_3Mapper=vtk.vtkPolyDataMapper()
point6_3Mapper.SetInputConnection(point6_3.GetOutputPort())

point6_3Actor = vtk.vtkActor()
point6_3Actor.SetMapper(point6_3Mapper)
point6_3Actor.GetProperty().SetColor(1.0,0.0,0.0)

point6_4=vtk.vtkCylinderSource()
point6_4.SetCenter(-1.5,-2.0,2.5)
point6_4.SetHeight(6.2)
point6_4.SetRadius(1)
point6_4.SetResolution(16)

point6_4Mapper=vtk.vtkPolyDataMapper()
point6_4Mapper.SetInputConnection(point6_4.GetOutputPort())

point6_4Actor = vtk.vtkActor()
point6_4Actor.SetMapper(point6_4Mapper)
point6_4Actor.GetProperty().SetColor(1.0,0.0,0.0)

point6_5=vtk.vtkCylinderSource()
point6_5.SetCenter(-1.5,-2.0,0.0)
point6_5.SetHeight(6.2)
point6_5.SetRadius(1)
point6_5.SetResolution(16)

point6_5Mapper=vtk.vtkPolyDataMapper()
point6_5Mapper.SetInputConnection(point6_5.GetOutputPort())

point6_5Actor = vtk.vtkActor()
point6_5Actor.SetMapper(point6_5Mapper)
point6_5Actor.GetProperty().SetColor(1.0,0.0,0.0)

point6_6=vtk.vtkCylinderSource()
point6_6.SetCenter(-1.5,-2.0,-2.5)
point6_6.SetHeight(6.2)
point6_6.SetRadius(1)
point6_6.SetResolution(16)

point6_6Mapper=vtk.vtkPolyDataMapper()
point6_6Mapper.SetInputConnection(point6_6.GetOutputPort())

point6_6Actor = vtk.vtkActor()
point6_6Actor.SetMapper(point6_6Mapper)
point6_6Actor.GetProperty().SetColor(1.0,0.0,0.0)

point2_1=vtk.vtkCylinderSource()
point2_1.SetCenter(0.0,2.0,2.0)
point2_1.SetHeight(6.2)
point2_1.SetRadius(1.30)
point2_1.SetResolution(16)

point2_1Mapper=vtk.vtkPolyDataMapper()
point2_1Mapper.SetInputConnection(point2_1.GetOutputPort())

point2_1Actor = vtk.vtkActor()
point2_1Actor.SetMapper(point2_1Mapper)
point2_1Actor.GetProperty().SetColor(1.0,0.0,0.0)
point2_1Actor.RotateX(90)

point2_2=vtk.vtkCylinderSource()
point2_2.SetCenter(0.0,2.0,-2.0)
point2_2.SetHeight(6.2)
point2_2.SetRadius(1.30)
point2_2.SetResolution(16)

point2_2Mapper=vtk.vtkPolyDataMapper()
point2_2Mapper.SetInputConnection(point2_2.GetOutputPort())

point2_2Actor = vtk.vtkActor()
point2_2Actor.SetMapper(point2_2Mapper)
point2_2Actor.GetProperty().SetColor(1.0,0.0,0.0)
point2_2Actor.RotateX(90)

point5_1=vtk.vtkCylinderSource()
point5_1.SetCenter(0.0,2.0,0.0)
point5_1.SetHeight(6.2)
point5_1.SetRadius(1.2)
point5_1.SetResolution(16)

point5_1Mapper=vtk.vtkPolyDataMapper()
point5_1Mapper.SetInputConnection(point5_1.GetOutputPort())

point5_1Actor = vtk.vtkActor()
point5_1Actor.SetMapper(point5_1Mapper)
point5_1Actor.GetProperty().SetColor(1.0,0.0,0.0)
point5_1Actor.RotateX(-90)

point5_2=vtk.vtkCylinderSource()
point5_2.SetCenter(2.3,2.0,2.3)
point5_2.SetHeight(6.2)
point5_2.SetRadius(1.2)
point5_2.SetResolution(16)

point5_2Mapper=vtk.vtkPolyDataMapper()
point5_2Mapper.SetInputConnection(point5_2.GetOutputPort())

point5_2Actor = vtk.vtkActor()
point5_2Actor.SetMapper(point5_2Mapper)
point5_2Actor.GetProperty().SetColor(1.0,0.0,0.0)
point5_2Actor.RotateX(-90)

point5_3=vtk.vtkCylinderSource()
point5_3.SetCenter(2.3,2.0,-2.3)
point5_3.SetHeight(6.2)
point5_3.SetRadius(1.2)
point5_3.SetResolution(16)

point5_3Mapper=vtk.vtkPolyDataMapper()
point5_3Mapper.SetInputConnection(point5_3.GetOutputPort())

point5_3Actor = vtk.vtkActor()
point5_3Actor.SetMapper(point5_3Mapper)
point5_3Actor.GetProperty().SetColor(1.0,0.0,0.0)
point5_3Actor.RotateX(-90)

point5_4=vtk.vtkCylinderSource()
point5_4.SetCenter(-2.3,2.0,2.3)
point5_4.SetHeight(6.2)
point5_4.SetRadius(1.2)
point5_4.SetResolution(16)

point5_4Mapper=vtk.vtkPolyDataMapper()
point5_4Mapper.SetInputConnection(point5_4.GetOutputPort())

point5_4Actor = vtk.vtkActor()
point5_4Actor.SetMapper(point5_4Mapper)
point5_4Actor.GetProperty().SetColor(1.0,0.0,0.0)
point5_4Actor.RotateX(-90)

point5_5=vtk.vtkCylinderSource()
point5_5.SetCenter(-2.3,2.0,-2.3)
point5_5.SetHeight(6.2)
point5_5.SetRadius(1.2)
point5_5.SetResolution(16)

point5_5Mapper=vtk.vtkPolyDataMapper()
point5_5Mapper.SetInputConnection(point5_5.GetOutputPort())

point5_5Actor = vtk.vtkActor()
point5_5Actor.SetMapper(point5_5Mapper)
point5_5Actor.GetProperty().SetColor(1.0,0.0,0.0)
point5_5Actor.RotateX(-90)

point4_1=vtk.vtkCylinderSource()
point4_1.SetCenter(2.2,2.0,2.2)
point4_1.SetHeight(6.2)
point4_1.SetRadius(1.3)
point4_1.SetResolution(16)

point4_1Mapper=vtk.vtkPolyDataMapper()
point4_1Mapper.SetInputConnection(point4_1.GetOutputPort())

point4_1Actor = vtk.vtkActor()
point4_1Actor.SetMapper(point4_1Mapper)
point4_1Actor.GetProperty().SetColor(1.0,0.0,0.0)
point4_1Actor.RotateY(90)
point4_1Actor.RotateX(90)

point4_2=vtk.vtkCylinderSource()
point4_2.SetCenter(-2.2,2.0,2.2)
point4_2.SetHeight(6.2)
point4_2.SetRadius(1.3)
point4_2.SetResolution(16)

point4_2Mapper=vtk.vtkPolyDataMapper()
point4_2Mapper.SetInputConnection(point4_2.GetOutputPort())

point4_2Actor = vtk.vtkActor()
point4_2Actor.SetMapper(point4_2Mapper)
point4_2Actor.GetProperty().SetColor(1.0,0.0,0.0)
point4_2Actor.RotateY(90)
point4_2Actor.RotateX(90)

point4_3=vtk.vtkCylinderSource()
point4_3.SetCenter(2.2,2.0,-2.2)
point4_3.SetHeight(6.2)
point4_3.SetRadius(1.3)
point4_3.SetResolution(16)

point4_3Mapper=vtk.vtkPolyDataMapper()
point4_3Mapper.SetInputConnection(point4_3.GetOutputPort())

point4_3Actor = vtk.vtkActor()
point4_3Actor.SetMapper(point4_3Mapper)
point4_3Actor.GetProperty().SetColor(1.0,0.0,0.0)
point4_3Actor.RotateY(90)
point4_3Actor.RotateX(90)

point4_4=vtk.vtkCylinderSource()
point4_4.SetCenter(-2.2,2.0,-2.2)
point4_4.SetHeight(6.2)
point4_4.SetRadius(1.3)
point4_4.SetResolution(16)

point4_4Mapper=vtk.vtkPolyDataMapper()
point4_4Mapper.SetInputConnection(point4_4.GetOutputPort())

point4_4Actor = vtk.vtkActor()
point4_4Actor.SetMapper(point4_4Mapper)
point4_4Actor.GetProperty().SetColor(1.0,0.0,0.0)
point4_4Actor.RotateY(90)
point4_4Actor.RotateX(90)

point3_1=vtk.vtkCylinderSource()
point3_1.SetCenter(2.2,2.0,2.2)
point3_1.SetHeight(6.2)
point3_1.SetRadius(1.3)
point3_1.SetResolution(16)

point3_1Mapper=vtk.vtkPolyDataMapper()
point3_1Mapper.SetInputConnection(point3_1.GetOutputPort())

point3_1Actor = vtk.vtkActor()
point3_1Actor.SetMapper(point3_1Mapper)
point3_1Actor.GetProperty().SetColor(1.0,0.0,0.0)
point3_1Actor.RotateY(90)
point3_1Actor.RotateX(-90)

point3_2=vtk.vtkCylinderSource()
point3_2.SetCenter(0.0,2.0,0.0)
point3_2.SetHeight(6.2)
point3_2.SetRadius(1.3)
point3_2.SetResolution(16)

point3_2Mapper=vtk.vtkPolyDataMapper()
point3_2Mapper.SetInputConnection(point3_2.GetOutputPort())

point3_2Actor = vtk.vtkActor()
point3_2Actor.SetMapper(point3_2Mapper)
point3_2Actor.GetProperty().SetColor(1.0,0.0,0.0)
point3_2Actor.RotateY(90)
point3_2Actor.RotateX(-90)

point3_3=vtk.vtkCylinderSource()
point3_3.SetCenter(-2.2,2.0,-2.2)
point3_3.SetHeight(6.2)
point3_3.SetRadius(1.3)
point3_3.SetResolution(16)

point3_3Mapper=vtk.vtkPolyDataMapper()
point3_3Mapper.SetInputConnection(point3_3.GetOutputPort())

point3_3Actor = vtk.vtkActor()
point3_3Actor.SetMapper(point3_3Mapper)
point3_3Actor.GetProperty().SetColor(1.0,0.0,0.0)
point3_3Actor.RotateY(90)
point3_3Actor.RotateX(-90)

ren1=vtk.vtkRenderer()
ren1.AddActor(cubeActor)
ren1.AddActor(point1_1Actor)
ren1.AddActor(point6_1Actor)
ren1.AddActor(point6_2Actor)
ren1.AddActor(point6_3Actor)
ren1.AddActor(point6_4Actor)
ren1.AddActor(point6_5Actor)
ren1.AddActor(point6_6Actor)
ren1.AddActor(point2_1Actor)
ren1.AddActor(point2_2Actor)
ren1.AddActor(point5_1Actor)
ren1.AddActor(point5_2Actor)
ren1.AddActor(point5_3Actor)
ren1.AddActor(point5_4Actor)
ren1.AddActor(point5_5Actor)
ren1.AddActor(point4_1Actor)
ren1.AddActor(point4_2Actor)
ren1.AddActor(point4_3Actor)
ren1.AddActor(point4_4Actor)
ren1.AddActor(point3_1Actor)
ren1.AddActor(point3_2Actor)
ren1.AddActor(point3_3Actor)
ren1.SetBackground(0.1,0.3,0.2)
renWin=vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(600,600)
renWin.Render()
ren1.GetActiveCamera().Zoom(0.4)
iren=vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.Initialize()
iren.Start()