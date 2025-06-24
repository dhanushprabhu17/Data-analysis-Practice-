# import xarray as xr
# import rasterio
# from rasterio.transform import from_origin

# # _Load the NetCDF file
filepath = "D:\\flood prediction\\datasetnetcdf.nc"

# # Select the variable you want to convert to TIFF (e.g., 'temperature')
# data_array = dataset['cp']

# # Define the spatial resolution and transformation matrix
# transform = from_origin(west=dataset['lon'].min(), 
#                         north=dataset['lat'].max(), 
#                         xsize=dataset['lon'].diff('lon').mean(), 
#                         ysize=dataset['lat'].diff('lat').mean())

# # Write the data to a TIFF file
# with rasterio.open('D:\\flood prediction\\output.tiff', 'w', 
#                    driver='GTiff', 
#                    height=data_array.shape[0], 
#                    width=data_array.shape[1], 
#                    count=1, 
#                    dtype=data_array.dtype, 
#                    crs='+proj=latlong', 
#                    transform=transform) as dst:
#     dst.write(data_array.values, 1)

# print('Conversion complete!')


import xarray as xr

# Open the NetCDF file
# file_path = 'your_file.nc'
dataset = xr.open_dataset(filepath)

# Print the dataset information
print(dataset)

# Access variables
print(dataset.data_vars)  # Lists all data variables

# Access a specific variable, for example 'temperature'
temperature_data = dataset['cp']
print(temperature_data)

# Perform operations or read the data into a NumPy array
temperature_array = temperature_data.values
print(temperature_array)

# Close the dataset (optional, but good practice)
dataset.close()

