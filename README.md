# modcam
Multi camera system field of view modeller

The config file contains a line per camera, with each field separated by space or tabulations.
The parameters are as follow:

 1. Focal length of the lens in millimeters
 2. Lens type. Either one of `rectilinear`, `stereographic`, `equidistant`, `equisolid` or `orthographic`, or a comma-separated list of polynomial coefficients to apply to the `rectilinear` type. The various lens types are described [here](http://michel.thoby.free.fr/Fisheye_history_short/Projections/Models_of_classical_projections.html).
 3. The sensor's width in millimeters.
 4. The sensor's height in millimeters.
 5. The camera angle from the central direction in degrees.
 6. The camera azimuth angle in degrees.
 7. The camera rotation in degrees or one of `H`, `V`, `h` or `v` for horizontal or vertical position with respect to the center (upper case) or on a grid (lower case).

Here is an example line:

    50 rectilinear 35.8 23.9 20 60 V
