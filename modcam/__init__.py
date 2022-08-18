try:
    from .Camera import Camera
    from .lens import lens_types
    from .main import plot
except ModuleNotFoundError:
    pass

__version__ = "0.0.1"
