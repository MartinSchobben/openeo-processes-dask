import numpy as np
import xarray as xr

from openeo_processes_dask.process_implementations.data_model import RasterCube

__all__ = ["mask"]

def mask(
    data: RasterCube,
    mask: RasterCube,
    replacement = np.nan
) -> RasterCube:
    return data.where(mask)