import argparse
import maya.standalone
maya.standalone.initialize()
import maya.cmds

#load Arnold plugin
#maya.cmds.loadPlugin('mtoa')
#print('Arnold/mtoa plugin loaded.')

#arguments
parser = argparse.ArgumentParser()
parser.add_argument('-r', '--radius', default=1, help='Select radius for sphere.')
parser.add_argument('-c', '--color', default='red', help='Select red, green, or blue color for sphere.')

args = parser.parse_args()

#create sphere with given radius or default
maya.cmds.polySphere(n="MySphere", radius=args.radius)

#create shader and shading group
sphereMat = maya.cmds.shadingNode("lambert", asShader=True, name="Mat_Sphere")
shadingGrp = maya.cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name="Mat_SphereSG")
maya.cmds.connectAttr("Mat_Sphere.outColor", "Mat_SphereSG.surfaceShader", force=True)

#assign shader to sphere
maya.cmds.select("MySphere")
maya.cmds.hyperShade(assign=sphereMat)

#set shader color
maya.cmds.select("Mat_Sphere")
if args.color == 'red':
    maya.cmds.setAttr("Mat_Sphere.color", 1, 0, 0, type="double3")
if args.color == 'green':
    maya.cmds.setAttr("Mat_Sphere.color", 0, 1, 0, type="double3")
if args.color == 'blue':
    maya.cmds.setAttr("Mat_Sphere.color", 0, 0, 1, type="double3")

#save file
maya.cmds.file(rename=r"C:\Users\larar\OneDrive - Drexel University\Desktop\Drexel\DIGM T680 - TD for Anim\Assignments\Maya_a03.mb")
maya.cmds.file(save=True)

print(f"Created a sphere of size {args.radius} with color {args.color}.")