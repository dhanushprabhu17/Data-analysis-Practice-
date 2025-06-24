import xarray as xr

ds = xr.open_dataset('your_file.grib', engine='cfgrib')
print(ds)
