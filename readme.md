# [Stanford drone dataset](http://cvgl.stanford.edu/projects/uav_data/):
Each line in the annotations.txt file corresponds to an annotation. Each line contains 10+ columns, separated by spaces. The definition of these columns are:

Values      |    Name     |   Description
----- | ----- | --------
1  |  Track ID. | All rows with the same ID belong to the same path.
2  |  xmin. | The top left x-coordinate of the bounding box.
3  |  ymin. | The top left y-coordinate of the bounding box.
4  |  xmax. | The bottom right x-coordinate of the bounding box.
5  |  ymax. | The bottom right y-coordinate of the bounding box.
6  |  frame. | The frame that this annotation represents.
7  |  lost. | If 1, the annotation is outside of the view screen.
8  |  occluded. | If 1, the annotation is occluded.
9  |  generated. | If 1, the annotation was automatically interpolated.
10 |  label. | The label for this annotation, enclosed in quotation marks.

# [Kitti format](https://github.com/NVIDIA/DIGITS/tree/master/digits/extensions/data/objectDetection):
Values      |    Name     |   Description
-------------|----------------|-----------------------------------------------
   1  |  type    |     Describes the type of object: 'Car', 'Van', 'Truck', 'Pedestrian', 'Person_sitting', 'Cyclist', 'Tram',  'Misc' or 'DontCare'
   1   | truncated |   Float from 0 (non-truncated) to 1 (truncated), where truncated refers to the object leaving image boundaries
   1   | occluded  |   Integer (0,1,2,3) indicating occlusion state:  0 = fully visible, 1 = partly occluded 2 = largely occluded, 3 = unknown
   1   | alpha     |   Observation angle of object, ranging [-pi..pi]
   4   | bbox       |  2D bounding box of object in the image (0-based index): contains left, top, right, bottom pixel coordinates
   3   | dimensions |  3D object dimensions: height, width, length (in meters)
   3    | location   |  3D object location x,y,z in camera coordinates (in meters)
   1   | rotation_y  | Rotation ry around Y-axis in camera coordinates [-pi..pi]
   1   | score      |  Only for results: Float, indicating confidence in detection, needed for p/r curves, higher is better.
# Mapping between the two:
sdd     |    kitti |    Name
--- | --- | ---
10  | 1    |    label(type)
2:5 | 5:8  |    axis
7(if 1) | 3(3) | occluded(outside the screen)
8(if 1) | 3(1) | occluded(partly occluded)
7,8(if 0) | 3(0) | occluded(fully visible)


# Running
1. In convertVideo2image.py:

    Change the "originalfolder" to the path: <your_standford_drone_dataset>/videos/

    Change the "destinationfolder" to the path: <your_destinationfolder>

2. In ssd2kitti.py:

    Change the "originalfolder" to the path: <your_standford_drone_dataset>/annotations/

    Change the "destinationfolder" to the path: <your_destinationfolder>

3. Run the two python scripts




