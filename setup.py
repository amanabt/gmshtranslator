from distutils.core import setup
setup(
    name = "gmshtranslator",
    packages = ["gmshtranslator"],
    version = "0.1",
    description = "gmsh .msh file parser",
    author = "Jose Abell",
    author_email = "info@joseabell.com",
    url = "http://www.joseabell.com",
    download_url = "http://github.com/amanabt/gmshtranslator",
    keywords = ["parsing", "gmsh", "msh", "mesh generation"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics"
        ],
    long_description = """\
gmshtranslator
-------------------------------------

Parser for gmsh `.msh` files.

"""
)
