import distutils.ccompiler
from distutils.core import setup, Extension

desc = """\
blender-mathutils module
========================

overview
++++++++

This module originated from blender (the opensource 3d package), where it has
been used for some years in production as a utility module for use in areas
including animation, games and mesh manipulation.

This differs from 'numpy' in that it is computer graphics focused, combining
Matrix and Vector types with rotation classes which is very useful for use with
animation or anywhere Euler and Quaternion values are used frequently.

This project is mainly a build system around the actively maintained mathutils
code in blender to allow non blender related projects to make use of it. A link
to the blender repository is used so the source never gets out of sync. 
"""


include_dirs = [
    "src/stubs",
    "src/blenlib",
    ]

source_files = [
    # * stubs *
    "src/stubs/stubs.c",

    # * blenlib *
    "src/blenlib/intern/math_base.c",
    "src/blenlib/intern/math_base_inline.c",
    "src/blenlib/intern/math_color.c",
    "src/blenlib/intern/math_color_inline.c",
    "src/blenlib/intern/math_geom.c",
    "src/blenlib/intern/math_geom_inline.c",
    "src/blenlib/intern/math_matrix.c",
    "src/blenlib/intern/math_rotation.c",
    "src/blenlib/intern/math_vector.c",
    "src/blenlib/intern/math_vector_inline.c",

    # * mathutils *
    "src/mathutils/mathutils.c",
    "src/mathutils/mathutils_Color.c",
    "src/mathutils/mathutils_Euler.c",
    "src/mathutils/mathutils_Matrix.c",
    "src/mathutils/mathutils_Quaternion.c",
    "src/mathutils/mathutils_Vector.c",
    "src/mathutils/mathutils_geometry.c",
    ]


header_files = [
    # * stubs *
    "src/stubs/BLI_memarena.h",
    "src/stubs/MEM_guardedalloc.h",
    "src/stubs/MEM_sys_types.h",

    # * blenlib *
    "src/blenlib/BLI_compiler_attrs.h",
    "src/blenlib/BLI_compiler_compat.h",
    "src/blenlib/BLI_dynstr.h",
    "src/blenlib/BLI_math.h",
    "src/blenlib/BLI_math_base.h",
    "src/blenlib/BLI_math_color.h",
    "src/blenlib/BLI_math_color_blend.h",
    "src/blenlib/BLI_math_geom.h",
    "src/blenlib/BLI_math_inline.h",
    "src/blenlib/BLI_math_interp.h",
    "src/blenlib/BLI_math_matrix.h",
    "src/blenlib/BLI_math_rotation.h",
    "src/blenlib/BLI_math_vector.h",
    "src/blenlib/BLI_memarena.h",
    "src/blenlib/BLI_mempool.h",
    "src/blenlib/BLI_strict_flags.h",
    "src/blenlib/BLI_sys_types.h",
    "src/blenlib/BLI_utildefines.h",


    # * mathutils *
    "src/mathutils/mathutils.h",
    "src/mathutils/mathutils_Color.h",
    "src/mathutils/mathutils_Euler.h",
    "src/mathutils/mathutils_Matrix.h",
    "src/mathutils/mathutils_Quaternion.h",
    "src/mathutils/mathutils_Vector.h",
    "src/mathutils/mathutils_geometry.h",
]

compiler_name = distutils.ccompiler.get_default_compiler()

if compiler_name == "msvc":
    options = ["/J"]
elif compiler_name == "unix":
    options = ["-funsigned-char"]


setup(name="mathutils",
      version="2.70",
      maintainer="Campbell Barton",
      maintainer_email="ideasman42@gmail.com",
      url="http://code.google.com/p/blender-mathutils",
      ext_modules=[Extension("mathutils",
                             source_files,
                             include_dirs=include_dirs,
                             define_macros=[("MATH_STANDALONE", None)],
                             depends=header_files,
                             extra_compile_args=options,
                             )
                  ],
     )
