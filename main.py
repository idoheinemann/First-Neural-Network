import numpy
import math
import random
import json
import os
import struct
import time

SET_STRING_JSON = ('[{"x":[0.154,0.334],"y":0},{"x":[0.164,0.312],"y":0},{"x":[0.178,0.28],"y":0},{"x":[0.232,0.242],"y":0},{"x":[0.246,0.224],"y":0},{"x":[0.3,0.212],"y":0},{"x":[0.344,0.204],"y":0},{"x":[0.208,0.248],"y":0},{"x":[0.276,0.206],"y":0},{"x":[0.384,0.204],"y":0},{"x":[0.42,0.234],"y":0},{"x":[0.442,0.262],"y":0},{"x":[0.46,0.302],"y":0},{"x":[0.474,0.35],"y":0},{"x":[0.31,0.322],"y":1},{"x":[0.314,0.35],"y":1},{"x":[0.302,0.394],"y":1},{"x":[0.326,0.428],"y":1},{"x":[0.326,0.47],"y":1},{"x":[0.356,0.48],"y":1},{"x":[0.384,0.496],"y":1},{"x":[0.416,0.502],"y":1},{"x":[0.44,0.494],"y":1},{"x":[0.478,0.484],"y":1},{"x":[0.508,0.478],"y":1},{"x":[0.546,0.46],"y":1},{"x":[0.586,0.45],"y":1},{"x":[0.594,0.43],"y":1},{"x":[0.604,0.41],"y":1},{"x":[0.63,0.37],"y":1},{"x":[0.64,0.33],"y":1}]'
,'[{"x":[0.4,0.758],"y":0},{"x":[0.352,0.758],"y":0},{"x":[0.318,0.73],"y":0},{"x":[0.292,0.716],"y":0},{"x":[0.248,0.704],"y":0},{"x":[0.222,0.668],"y":0},{"x":[0.206,0.644],"y":0},{"x":[0.18,0.602],"y":0},{"x":[0.164,0.59],"y":0},{"x":[0.156,0.556],"y":0},{"x":[0.138,0.522],"y":0},{"x":[0.136,0.498],"y":0},{"x":[0.142,0.456],"y":0},{"x":[0.154,0.404],"y":0},{"x":[0.174,0.356],"y":0},{"x":[0.214,0.308],"y":0},{"x":[0.266,0.278],"y":0},{"x":[0.326,0.274],"y":0},{"x":[0.368,0.246],"y":0},{"x":[0.388,0.268],"y":0},{"x":[0.448,0.276],"y":0},{"x":[0.512,0.29],"y":0},{"x":[0.564,0.322],"y":0},{"x":[0.626,0.326],"y":0},{"x":[0.648,0.37],"y":0},{"x":[0.678,0.418],"y":0},{"x":[0.682,0.458],"y":0},{"x":[0.676,0.506],"y":0},{"x":[0.67,0.55],"y":0},{"x":[0.642,0.62],"y":0},{"x":[0.644,0.646],"y":0},{"x":[0.6,0.69],"y":0},{"x":[0.574,0.732],"y":0},{"x":[0.512,0.744],"y":0},{"x":[0.452,0.752],"y":0},{"x":[0.458,0.756],"y":0},{"x":[0.546,0.728],"y":0},{"x":[0.584,0.718],"y":0},{"x":[0.608,0.682],"y":0},{"x":[0.644,0.638],"y":0},{"x":[0.654,0.616],"y":0},{"x":[0.67,0.584],"y":0},{"x":[0.682,0.554],"y":0},{"x":[0.67,0.376],"y":0},{"x":[0.646,0.346],"y":0},{"x":[0.614,0.322],"y":0},{"x":[0.568,0.322],"y":0},{"x":[0.41,0.508],"y":1},{"x":[0.45,0.508],"y":1},{"x":[0.424,0.538],"y":1},{"x":[0.404,0.54],"y":1},{"x":[0.394,0.494],"y":1},{"x":[0.464,0.464],"y":1},{"x":[0.444,0.508],"y":1},{"x":[0.434,0.546],"y":1},{"x":[0.386,0.538],"y":1},{"x":[0.414,0.492],"y":1},{"x":[0.452,0.474],"y":1},{"x":[0.42,0.528],"y":1},{"x":[0.392,0.548],"y":1},{"x":[0.414,0.51],"y":1},{"x":[0.452,0.51],"y":1},{"x":[0.392,0.544],"y":1},{"x":[0.374,0.562],"y":1},{"x":[0.418,0.562],"y":1},{"x":[0.43,0.55],"y":1},{"x":[0.376,0.516],"y":1},{"x":[0.38,0.52],"y":1},{"x":[0.42,0.468],"y":1},{"x":[0.428,0.476],"y":1},{"x":[0.744,0.158],"y":2},{"x":[0.702,0.18],"y":2},{"x":[0.74,0.146],"y":2},{"x":[0.788,0.162],"y":2},{"x":[0.766,0.182],"y":2},{"x":[0.708,0.194],"y":2},{"x":[0.712,0.17],"y":2},{"x":[0.756,0.158],"y":2},{"x":[0.772,0.194],"y":2},{"x":[0.742,0.192],"y":2},{"x":[0.728,0.178],"y":2},{"x":[0.748,0.142],"y":2},{"x":[0.768,0.138],"y":2},{"x":[0.808,0.134],"y":2},{"x":[0.736,0.178],"y":2},{"x":[0.718,0.162],"y":2}]'
,'[{"x":[0.24,0.524],"y":0},{"x":[0.264,0.486],"y":0},{"x":[0.27,0.458],"y":0},{"x":[0.27,0.45],"y":0},{"x":[0.278,0.424],"y":0},{"x":[0.298,0.394],"y":0},{"x":[0.312,0.362],"y":0},{"x":[0.324,0.354],"y":0},{"x":[0.342,0.32],"y":0},{"x":[0.352,0.298],"y":0},{"x":[0.37,0.266],"y":0},{"x":[0.42,0.228],"y":0},{"x":[0.466,0.196],"y":0},{"x":[0.506,0.188],"y":0},{"x":[0.554,0.182],"y":0},{"x":[0.598,0.176],"y":0},{"x":[0.668,0.196],"y":0},{"x":[0.72,0.218],"y":0},{"x":[0.756,0.25],"y":0},{"x":[0.778,0.302],"y":0},{"x":[0.81,0.338],"y":0},{"x":[0.822,0.398],"y":0},{"x":[0.822,0.446],"y":0},{"x":[0.834,0.476],"y":0},{"x":[0.576,0.352],"y":1},{"x":[0.566,0.386],"y":1},{"x":[0.574,0.43],"y":1},{"x":[0.566,0.484],"y":1},{"x":[0.558,0.538],"y":1},{"x":[0.584,0.612],"y":1},{"x":[0.594,0.664],"y":1},{"x":[0.63,0.702],"y":1},{"x":[0.714,0.734],"y":1},{"x":[0.754,0.746],"y":1},{"x":[0.84,0.764],"y":1},{"x":[0.876,0.756],"y":1},{"x":[0.894,0.746],"y":1},{"x":[0.944,0.702],"y":1},{"x":[0.986,0.654],"y":1},{"x":[0.978,0.618],"y":1},{"x":[0.988,0.562],"y":1},{"x":[0.992,0.502],"y":1},{"x":[0.982,0.454],"y":1},{"x":[0.984,0.422],"y":1},{"x":[0.998,0.372],"y":1},{"x":[0.99,0.278],"y":1},{"x":[0.996,0.378],"y":1},{"x":[0.998,0.476],"y":1},{"x":[0.998,0.39],"y":1},{"x":[0.994,0.28],"y":1},{"x":[0.99,0.508],"y":1},{"x":[0.986,0.542],"y":1},{"x":[0.976,0.606],"y":1},{"x":[0.972,0.624],"y":1},{"x":[0.96,0.662],"y":1},{"x":[0.988,0.314],"y":1},{"x":[0.998,0.356],"y":1},{"x":[0.986,0.396],"y":1},{"x":[0.99,0.416],"y":1},{"x":[0.99,0.33],"y":1},{"x":[0.988,0.304],"y":1},{"x":[0.994,0.454],"y":1},{"x":[0.998,0.488],"y":1},{"x":[0.988,0.636],"y":1},{"x":[0.95,0.688],"y":1},{"x":[0.934,0.718],"y":1},{"x":[0.914,0.734],"y":1},{"x":[0.892,0.75],"y":1},{"x":[0.874,0.754],"y":1},{"x":[0.838,0.75],"y":1},{"x":[0.804,0.752],"y":1},{"x":[0.762,0.75],"y":1},{"x":[0.726,0.748],"y":1},{"x":[0.674,0.732],"y":1},{"x":[0.638,0.704],"y":1},{"x":[0.63,0.658],"y":1},{"x":[0.604,0.63],"y":1},{"x":[0.576,0.598],"y":1},{"x":[0.574,0.58],"y":1},{"x":[0.57,0.538],"y":1},{"x":[0.574,0.538],"y":1},{"x":[0.568,0.394],"y":1},{"x":[0.574,0.356],"y":1},{"x":[0.826,0.472],"y":0},{"x":[0.838,0.448],"y":0},{"x":[0.842,0.428],"y":0},{"x":[0.818,0.4],"y":0},{"x":[0.81,0.358],"y":0},{"x":[0.8,0.338],"y":0},{"x":[0.796,0.316],"y":0},{"x":[0.786,0.312],"y":0},{"x":[0.766,0.298],"y":0},{"x":[0.76,0.284],"y":0},{"x":[0.75,0.272],"y":0},{"x":[0.748,0.242],"y":0},{"x":[0.724,0.224],"y":0},{"x":[0.68,0.218],"y":0},{"x":[0.65,0.186],"y":0},{"x":[0.602,0.174],"y":0},{"x":[0.576,0.174],"y":0},{"x":[0.538,0.174],"y":0},{"x":[0.486,0.202],"y":0},{"x":[0.456,0.216],"y":0},{"x":[0.392,0.262],"y":0},{"x":[0.33,0.334],"y":0},{"x":[0.272,0.426],"y":0},{"x":[0.248,0.508],"y":0},{"x":[0.808,0.62],"y":2},{"x":[0.79,0.618],"y":2},{"x":[0.776,0.602],"y":2},{"x":[0.768,0.59],"y":2},{"x":[0.758,0.58],"y":2},{"x":[0.744,0.57],"y":2},{"x":[0.738,0.55],"y":2},{"x":[0.738,0.532],"y":2},{"x":[0.74,0.526],"y":2},{"x":[0.73,0.5],"y":2},{"x":[0.718,0.474],"y":2},{"x":[0.716,0.464],"y":2},{"x":[0.714,0.454],"y":2},{"x":[0.712,0.434],"y":2},{"x":[0.698,0.426],"y":2},{"x":[0.694,0.406],"y":2},{"x":[0.692,0.394],"y":2},{"x":[0.688,0.378],"y":2},{"x":[0.69,0.358],"y":2},{"x":[0.684,0.342],"y":2},{"x":[0.684,0.328],"y":2},{"x":[0.678,0.318],"y":2},{"x":[0.67,0.306],"y":2},{"x":[0.658,0.298],"y":2},{"x":[0.646,0.286],"y":2},{"x":[0.642,0.276],"y":2},{"x":[0.634,0.274],"y":2},{"x":[0.598,0.274],"y":2},{"x":[0.592,0.268],"y":2},{"x":[0.578,0.268],"y":2},{"x":[0.546,0.282],"y":2},{"x":[0.516,0.292],"y":2},{"x":[0.5,0.314],"y":2},{"x":[0.482,0.346],"y":2},{"x":[0.47,0.37],"y":2},{"x":[0.462,0.41],"y":2},{"x":[0.438,0.484],"y":2},{"x":[0.43,0.54],"y":2},{"x":[0.426,0.562],"y":2},{"x":[0.426,0.56],"y":2},{"x":[0.438,0.528],"y":2},{"x":[0.438,0.504],"y":2},{"x":[0.45,0.476],"y":2},{"x":[0.456,0.456],"y":2},{"x":[0.462,0.42],"y":2},{"x":[0.458,0.406],"y":2},{"x":[0.688,0.75],"y":1},{"x":[0.698,0.726],"y":1},{"x":[0.676,0.708],"y":1},{"x":[0.646,0.692],"y":1},{"x":[0.61,0.672],"y":1},{"x":[0.628,0.642],"y":1},{"x":[0.61,0.626],"y":1},{"x":[0.592,0.58],"y":1},{"x":[0.584,0.562],"y":1},{"x":[0.576,0.528],"y":1},{"x":[0.57,0.498],"y":1},{"x":[0.578,0.472],"y":1},{"x":[0.576,0.442],"y":1},{"x":[0.574,0.398],"y":1},{"x":[0.574,0.378],"y":1},{"x":[0.568,0.422],"y":1},{"x":[0.564,0.498],"y":1},{"x":[0.56,0.542],"y":1},{"x":[0.57,0.586],"y":1},{"x":[0.596,0.646],"y":1},{"x":[0.638,0.668],"y":1},{"x":[0.66,0.702],"y":1},{"x":[0.7,0.708],"y":1},{"x":[0.708,0.73],"y":1},{"x":[0.718,0.75],"y":1},{"x":[0.874,0.746],"y":1},{"x":[0.832,0.75],"y":1},{"x":[0.798,0.748],"y":1},{"x":[0.754,0.746],"y":1},{"x":[0.776,0.302],"y":0},{"x":[0.766,0.268],"y":0},{"x":[0.742,0.246],"y":0},{"x":[0.71,0.224],"y":0},{"x":[0.692,0.208],"y":0},{"x":[0.67,0.192],"y":0},{"x":[0.65,0.178],"y":0},{"x":[0.62,0.182],"y":0},{"x":[0.576,0.18],"y":0},{"x":[0.55,0.176],"y":0},{"x":[0.518,0.186],"y":0},{"x":[0.476,0.208],"y":0},{"x":[0.434,0.228],"y":0},{"x":[0.394,0.26],"y":0},{"x":[0.342,0.326],"y":0},{"x":[0.294,0.382],"y":0},{"x":[0.252,0.47],"y":0},{"x":[0.526,0.772],"y":3},{"x":[0.526,0.782],"y":3},{"x":[0.56,0.776],"y":3},{"x":[0.582,0.76],"y":3},{"x":[0.562,0.764],"y":3},{"x":[0.526,0.76],"y":3},{"x":[0.528,0.76],"y":3},{"x":[0.546,0.784],"y":3},{"x":[0.546,0.81],"y":3},{"x":[0.542,0.778],"y":3},{"x":[0.562,0.75],"y":3},{"x":[0.566,0.762],"y":3},{"x":[0.536,0.786],"y":3},{"x":[0.53,0.78],"y":3},{"x":[0.544,0.768],"y":3}]'
,'[{"x":[0.138,0.752],"y":0},{"x":[0.102,0.73],"y":0},{"x":[0.116,0.7],"y":0},{"x":[0.178,0.668],"y":0},{"x":[0.21,0.716],"y":0},{"x":[0.23,0.774],"y":0},{"x":[0.168,0.792],"y":0},{"x":[0.13,0.752],"y":0},{"x":[0.146,0.714],"y":0},{"x":[0.198,0.758],"y":0},{"x":[0.198,0.778],"y":0},{"x":[0.15,0.778],"y":0},{"x":[0.166,0.694],"y":0},{"x":[0.206,0.742],"y":0},{"x":[0.198,0.746],"y":0},{"x":[0.142,0.718],"y":0},{"x":[0.17,0.714],"y":0},{"x":[0.43,0.722],"y":1},{"x":[0.476,0.77],"y":1},{"x":[0.422,0.77],"y":1},{"x":[0.398,0.77],"y":1},{"x":[0.464,0.74],"y":1},{"x":[0.502,0.764],"y":1},{"x":[0.454,0.802],"y":1},{"x":[0.416,0.766],"y":1},{"x":[0.464,0.722],"y":1},{"x":[0.51,0.736],"y":1},{"x":[0.488,0.776],"y":1},{"x":[0.422,0.758],"y":1},{"x":[0.464,0.71],"y":1},{"x":[0.478,0.742],"y":1},{"x":[0.468,0.748],"y":1},{"x":[0.422,0.774],"y":1},{"x":[0.482,0.764],"y":1},{"x":[0.492,0.716],"y":1},{"x":[0.45,0.734],"y":1},{"x":[0.412,0.608],"y":2},{"x":[0.398,0.56],"y":2},{"x":[0.438,0.546],"y":2},{"x":[0.444,0.516],"y":2},{"x":[0.42,0.518],"y":2},{"x":[0.406,0.554],"y":2},{"x":[0.412,0.574],"y":2},{"x":[0.424,0.57],"y":2},{"x":[0.42,0.524],"y":2},{"x":[0.42,0.488],"y":2},{"x":[0.404,0.43],"y":2},{"x":[0.424,0.37],"y":2},{"x":[0.414,0.344],"y":2},{"x":[0.39,0.304],"y":2},{"x":[0.378,0.272],"y":2},{"x":[0.352,0.238],"y":2},{"x":[0.322,0.29],"y":2},{"x":[0.298,0.326],"y":2},{"x":[0.258,0.378],"y":2},{"x":[0.248,0.458],"y":2},{"x":[0.238,0.502],"y":2},{"x":[0.23,0.548],"y":2},{"x":[0.218,0.554],"y":2},{"x":[0.224,0.474],"y":2},{"x":[0.258,0.426],"y":2},{"x":[0.264,0.39],"y":2},{"x":[0.29,0.326],"y":2},{"x":[0.33,0.272],"y":2},{"x":[0.368,0.254],"y":2},{"x":[0.37,0.284],"y":2},{"x":[0.354,0.268],"y":2},{"x":[0.318,0.302],"y":2},{"x":[0.278,0.346],"y":2},{"x":[0.274,0.398],"y":2},{"x":[0.262,0.448],"y":2},{"x":[0.244,0.498],"y":2},{"x":[0.234,0.54],"y":2},{"x":[0.23,0.548],"y":2},{"x":[0.226,0.542],"y":2},{"x":[0.274,0.402],"y":2},{"x":[0.302,0.354],"y":2},{"x":[0.342,0.274],"y":2},{"x":[0.388,0.308],"y":2},{"x":[0.414,0.38],"y":2},{"x":[0.434,0.424],"y":2},{"x":[0.426,0.504],"y":2},{"x":[0.422,0.546],"y":2},{"x":[0.402,0.574],"y":2},{"x":[0.41,0.482],"y":2},{"x":[0.438,0.318],"y":2},{"x":[0.458,0.226],"y":2},{"x":[0.44,0.166],"y":2},{"x":[0.416,0.086],"y":2},{"x":[0.412,0.03],"y":2},{"x":[0.352,0.01],"y":2},{"x":[0.322,0.064],"y":2},{"x":[0.306,0.242],"y":2},{"x":[0.27,0.44],"y":2},{"x":[0.27,0.534],"y":2},{"x":[0.284,0.612],"y":2},{"x":[0.282,0.608],"y":2},{"x":[0.394,0.588],"y":2},{"x":[0.434,0.564],"y":2},{"x":[0.282,0.576],"y":2},{"x":[0.322,0.348],"y":2},{"x":[0.362,0.418],"y":2},{"x":[0.334,0.178],"y":2},{"x":[0.374,0.076],"y":2},{"x":[0.352,0.158],"y":2},{"x":[0.374,0.238],"y":2},{"x":[0.342,0.488],"y":2},{"x":[0.35,0.524],"y":2},{"x":[0.318,0.392],"y":2},{"x":[0.478,0.266],"y":2},{"x":[0.442,0.264],"y":2},{"x":[0.444,0.312],"y":2},{"x":[0.42,0.368],"y":2},{"x":[0.398,0.308],"y":2},{"x":[0.388,0.238],"y":2},{"x":[0.42,0.224],"y":2},{"x":[0.424,0.182],"y":2},{"x":[0.416,0.11],"y":2},{"x":[0.422,0.082],"y":2},{"x":[0.39,0.034],"y":2},{"x":[0.352,0.03],"y":2},{"x":[0.34,0.098],"y":2},{"x":[0.326,0.126],"y":2},{"x":[0.322,0.18],"y":2},{"x":[0.316,0.26],"y":2},{"x":[0.278,0.326],"y":2},{"x":[0.266,0.29],"y":2},{"x":[0.362,0.182],"y":2},{"x":[0.398,0.168],"y":2},{"x":[0.374,0.13],"y":2},{"x":[0.362,0.086],"y":2},{"x":[0.366,0.11],"y":2},{"x":[0.394,0.2],"y":2},{"x":[0.366,0.21],"y":2},{"x":[0.348,0.234],"y":2},{"x":[0.326,0.246],"y":2},{"x":[0.31,0.272],"y":2},{"x":[0.282,0.306],"y":2},{"x":[0.294,0.268],"y":2},{"x":[0.322,0.188],"y":2},{"x":[0.318,0.114],"y":2},{"x":[0.33,0.062],"y":2},{"x":[0.37,0.082],"y":2},{"x":[0.398,0.118],"y":2},{"x":[0.394,0.164],"y":2},{"x":[0.402,0.22],"y":2},{"x":[0.342,0.534],"y":2},{"x":[0.322,0.516],"y":2},{"x":[0.334,0.48],"y":2},{"x":[0.394,0.482],"y":2},{"x":[0.362,0.472],"y":2},{"x":[0.412,0.292],"y":2},{"x":[0.418,0.302],"y":2},{"x":[0.328,0.392],"y":2},{"x":[0.286,0.46],"y":2},{"x":[0.282,0.5],"y":2},{"x":[0.274,0.534],"y":2},{"x":[0.31,0.492],"y":2},{"x":[0.322,0.43],"y":2},{"x":[0.326,0.402],"y":2},{"x":[0.358,0.36],"y":2},{"x":[0.366,0.346],"y":2},{"x":[0.402,0.404],"y":2},{"x":[0.39,0.434],"y":2},{"x":[0.378,0.512],"y":2},{"x":[0.402,0.586],"y":2},{"x":[0.344,0.582],"y":2},{"x":[0.32,0.598],"y":2},{"x":[0.168,0.734],"y":0},{"x":[0.17,0.746],"y":0},{"x":[0.162,0.744],"y":0},{"x":[0.182,0.734],"y":0},{"x":[0.454,0.75],"y":1},{"x":[0.45,0.762],"y":1},{"x":[0.442,0.772],"y":1},{"x":[0.472,0.76],"y":1},{"x":[0.484,0.736],"y":1},{"x":[0.146,0.76],"y":0},{"x":[0.19,0.772],"y":0},{"x":[0.156,0.778],"y":0}]'
                   )

def main():
    global SET_STRING_JSON
    nn = NeuralNetwork(784,50,40,30,20,10)
    #set_j = json.loads(SET_STRING_JSON[3])
    #set = []
    #for i in set_j:
    #    set.append(SetItem(numpy.matrix(i["x"]).T,i["y"],len(nn.layers[len(nn.layers)-1])-1))
    #var = read()
    set = None
    a = None
    b = None
    c = None
    rate = 10
    for i in fixSet(read()):
        try:
            minimize(nn,i,rate,1)
        except KeyboardInterrupt:
            rate = input("enter new rate: ")
            print(cost(nn,i))
            while True:
                try:
                    minimize(nn, i, rate, 1)
                    break
                except KeyboardInterrupt:
                    pass
        print("finished iteration")
    while True:
        try:
            print(input(">>> "))
        except Exception as e:
            print(e)

def fixSet(set):
    for i in xrange(60000/100):
        l = []
        for i in xrange(100):
            y,x = set.next()
            l.append(SetItem(join(x),y,10))
        yield l

def join(arr):
    l = []
    for i in arr:
        for j in i:
            l.append(j)
    return l

def generate_vct_1(length):
    l = []
    for i in xrange(length):
        l.append(1)
    return vector(l)


def log(vec):
    global EPSILON
    l = []
    for i in vec.items:
        l.append(math.log(i if (i != 0) else EPSILON))
    return vector(l)

EPSILON = 0.001


def cost(network, set):
    j = 0
    h = None
    y = None
    vct1 = generate_vct_1(len(network.layers[len(network.layers)-1].neurons)-1)
    for i in set:
        h = vector(network.hypot(i.x))
        y = vector(i.y)
        j -= (dmul(y,log(h)) + dmul(vct1 - y, log(vct1 - h))).sum()
    return j/len(set)



def manual_cost_derivative(set,network,weight):
    global EPSILON
    weight.value += EPSILON
    j = cost(network,set)
    weight.value -= 2*EPSILON
    j -= cost(network,set)
    weight.value += EPSILON
    return j/(2*EPSILON)



def minimize_manual(network,set,rate = 0.1,max_iter = 1000):
    for iter in xrange(max_iter):
        for l in network.layers:
            for n in l.neurons:
                for w in n.inputWeights:
                    w.value -= rate*manual_cost_derivative(set,network,w)
    return cost(network,set);


def minimize(network,set,rate = 0.1,max_iter = 1000):
    full_derivs = {}
    derivs = {}
    for iter in xrange(max_iter):
        for i in network.layers:
            for j in i.neurons:
                for k in j.inputWeights:
                    full_derivs[str(k)] = 0
        for i in set:
            h = vector(network.hypot(i.x))

            for n in xrange(len(network.layers[len(network.layers)-1].neurons)):
                if network.layers[len(network.layers)-1].neurons[n].isBios:
                    continue
                costtag = (h.items[n - 1] - i.y[n - 1])*(h[n-1])*(1-h[n-1]) # n.value*(1-n.value)
                for w in network.layers[len(network.layers)-1].neurons[n].inputWeights:
                    derivs[str(w)] = costtag*w.input.value

            for l in xrange(len(network.layers)-2,0,-1):
                for n in network.layers[l].neurons:
                    for w in n.inputWeights:
                        sigma = 0
                        for k in w.output.outputWeights:
                            sigma += derivs[str(k)]*k.value
                        derivs[str(w)] = sigma*w.input.value*(1-w.output.value)
            for i in network.layers:
                for j in i.neurons:
                    for k in j.inputWeights:
                        full_derivs[str(k)] += derivs[str(k)]
        for i in network.layers:
            for j in i.neurons:
                for k in j.inputWeights:
                    k.value -= rate*full_derivs[str(k)]/len(set)
    #return cost(network,set)


def vminimize(network,set,rate = 0.1,max_iter = 1000):
    for iter in xrange(max_iter):
        pass #TODO complete







def dmul(v1,v2):
    l = []
    for i in xrange(v1.length):
        l.append(v1.items[i]*v2.items[i])
    return vector(l)




class vector():
    def __init__(self,items):
        self.items = items
        self.length = len(items)
    def __add__(self, other):
        l = []
        for i in xrange(self.length):
            l.append(self.items[i]+other.items[i])
        return vector(l)
    def __abs__(self):
        sum = 0;
        for i in self.items:
            sum += i*i
        return math.sqrt(sum)
    def __neg__(self):
        l = []
        for i in self.items:
            l.append(-i)
        return vector(l)
    def __sub__(self, other):
        l = []
        for i in xrange(self.length):
            l.append(self.items[i] - other.items[i])
        return vector(l)
    def __mul__(self, other):
        l = 0
        for i in xrange(self.length):
            l += self.items[i] * other.items[i]
        return l
    def __getitem__(self, item):
        return self.items[item]
    def sum(self):
        s = 0
        for i in self.items:
            s += i
        return s

class SetItem():
    def __init__(self,x,y,out):
        self.x = x;
        l = []
        for i in xrange(out):
            l.append(1 if i == y else 0)
        self.y = l
    def __str__(self):
        return "SetItem:[x:" + str(self.x) + ", y:" + str(self.y) + "]"


def sigmoid(x):
    try:
        return 1/(1+math.exp(-x))
    except OverflowError:
        return 0







class NeuralNetwork():
    def __init__(self,*layersNum):
        self.layers = []
        layers = list(layersNum)
        lastLayer = None
        for i in layers:
            lastLayer = Layer(i,lastLayer)
            self.layers.append(lastLayer)
        for n in self.layers[0].neurons:
            n.isBios = True

    def hypot(self,inputs):
        for i in xrange(1,len(self.layers[0].neurons)):
            self.layers[0].neurons[i].value = inputs[i-1]
        # initializing the input layer

        for i in self.layers:
            if not i is self.layers[0]:
                i.hypot() # activating each layer
        l = []
        for i in self.layers[len(self.layers)-1].neurons:
            if not i.isBios:
                l.append(i.value) # result list
        return l










class Layer():
    def __init__(self,length,prev):
        self.neurons = [Neuron(None,True)]
        for i in xrange(length):
            self.neurons.append(Neuron(prev))

    def hypot(self):
        for i in self.neurons:
            i.hypot()















class Neuron():
    def __init__(self,layer,isBios = False):
        self.inputWeights = []
        self.outputWeights = []
        self.value = 1 if isBios else 0
        self.isBios = isBios
        if not layer is None:
            tmpwieght = None
            for i in layer.neurons:
                tmpwieght = Weight(i,self)
                self.inputWeights.append(tmpwieght)
                i.outputWeights.append(tmpwieght)

    def hypot(self):
        if not self.isBios:
            self.value = 0
            for i in self.inputWeights:
                self.value += i.hypot()
            self.value = sigmoid(self.value)

















class Weight():

    def __init__(self,input = None,output = None):
        global EPSILON
        self.input = input
        self.output = output
        self.value = (random.random()-0.5)

    def hypot(self):
        return self.value*self.input.value;


def vsigmoid(x):
    return 1 / (1 + numpy.exp(-x))


class VNeuralNetwork():
    def __init__(self,*layersN):
        layers = list(layersN)
        self.weights = []
        self.input = layers[0]
        self.output = layers[len(layers)-1]
        for i in xrange(len(layers)-1):
            self.weights.append(numpy.matrix(numpy.random.rand(layers[i+1],layers[i]+1))-0.5)
    def hypot(self,input):
        for i in self.weights:
            input = numpy.concatenate((numpy.ones((1,int(input.shape[1]))),input))
            input = vsigmoid(i*input)
        return input
    def movement(self,input):
        l = []
        for i in self.weights:
            input = numpy.concatenate((numpy.ones((1, int(input.shape[1]))), input))
            l.append(input)
            input = vsigmoid(i * input)
        return l
    def __getitem__(self, item):
        return self.weights[item]
    def __len__(self):
        return len(self.weights)

def vcost(network,set):
    j = 0
    vct1 = numpy.matrix(numpy.ones(network.output))
    for i in set:
        h = network.hypot(i.x)
        y = numpy.matrix(i.y)
        j -= (numpy.multiply(y,numpy.log(h)) + numpy.multiply(vct1-y,numpy.log(1-h))).sum()
    return j / len(set)


def vmanual_cost_derivative(set,network,layer,neuron,weight):
    global EPSILON
    network[layer][neuron,weight] += EPSILON
    j = vcost(network,set)
    network[layer][neuron,weight] -= 2*EPSILON
    j -= vcost(network,set)
    network[layer][neuron,weight] += EPSILON
    return j/(2*EPSILON)


def vminimize_manual(network,set,rate=0.1,max_iter = 1000):
    deriv = []
    for i in xrange(len(network)):
        deriv.append(numpy.zeros(network[i].shape))
    for iter in xrange(max_iter):
        for i in xrange(len(network)):
            for j in xrange(network[i].shape[0]):
                for k in xrange(network[i].shape[1]):
                    deriv[i][j,k] = rate*vmanual_cost_derivative(set,network,i,j,k)
        for i in xrange(len(deriv)):

            network.weights[i] -= deriv[i]

    return vcost(network,set)


def read(dataset = "training", path = "."):
    import numpy as np
    """
    Python function for importing the MNIST data set.  It returns an iterator
    of 2-tuples with the first element being the label and the second element
    being a numpy.uint8 2D array of pixel data for the given image.
    """

    if dataset is "training":
        fname_img = os.path.join(path, 'train-images.idx3-ubyte')
        fname_lbl = os.path.join(path, 'train-labels.idx1-ubyte')
    elif dataset is "testing":
        fname_img = os.path.join(path, 't10k-images.idx3-ubyte')
        fname_lbl = os.path.join(path, 't10k-labels.idx1-ubyte')
    else:
        raise ValueError, "dataset must be 'testing' or 'training'"

    # Load everything in some numpy arrays
    with open(fname_lbl, 'rb') as flbl:
        magic, num = struct.unpack(">II", flbl.read(8))
        lbl = np.fromfile(flbl, dtype=np.int8)

    with open(fname_img, 'rb') as fimg:
        magic, num, rows, cols = struct.unpack(">IIII", fimg.read(16))
        img = np.fromfile(fimg, dtype=np.uint8).reshape(len(lbl), rows, cols)

    get_img = lambda idx: (lbl[idx], img[idx])

    # Create an iterator which returns each image in turn
    for i in xrange(len(lbl)):
        yield get_img(i)


def show(image):
    """
    Render a given numpy.uint8 2D array of pixel data.
    """
    from matplotlib import pyplot
    import matplotlib as mpl
    fig = pyplot.figure()
    ax = fig.add_subplot(1,1,1)
    imgplot = ax.imshow(image, cmap=mpl.cm.Greys)
    imgplot.set_interpolation('nearest')
    ax.xaxis.set_ticks_position('top')
    ax.yaxis.set_ticks_position('left')
    pyplot.show()

if __name__ == "__main__":
    main()