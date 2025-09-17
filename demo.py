from vpython import box, rate, vector, scene

scene.title = "Rotating 3D Cube (VPython)"
scene.background = vector(0.1, 0.1, 0.2)
scene.width = 600
scene.height = 400

cube = box(pos=vector(0,0,0), size=vector(2,2,2), color=vector(0.2,0.7,1))

while True:
    rate(60)
    cube.rotate(angle=0.03, axis=vector(0,1,0))
    cube.rotate(angle=0.01, axis=vector(1,0,0))