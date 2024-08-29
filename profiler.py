import goes_ortho as go
import xarray as xr
import geogif

startDatetime = '2024-08-10T00:00:00Z'
endDatetime = '2024-08-10T00:59:00Z'
[min_lon, min_lat, max_lon, max_lat] = [-123, 46, -121, 48]
#satellite = 'goes18'
product = 'ABI-L1b-RadC'
#band = 2
variable = 'Rad'
OPENTOPO_API_KEY = '585b1d1639bc5ef8a4a5bdea7e45a8d1'

for satellite in ['goes16', 'goes18']:
    for band in [1, 2, 3]:
        # Make request file from user input
        go.get_data.make_request_json(f'{satellite}-build-zarr-b{band}', startDatetime, endDatetime, \
                  [min_lon, min_lat, max_lon, max_lat], \
                  satellite, product, band, variable, OPENTOPO_API_KEY)
        
        # Download GOES imagery and build zarr file
        go.get_data.build_zarr(f'{satellite}-build-zarr-b{band}.json')
        
        # make preview gif animation
        ds = xr.open_zarr(f'{satellite}-build-zarr-b{band}.zarr')
        da = ds[variable]
        gif_bytes = geogif.dgif(da, fps=5, cmap='Greys_r', date_format='%Y-%m-%d %H:%M:%S', date_position='ul', bytes=True).compute()
        with open(f'{satellite}-b{band}.gif', 'wb') as f:
            f.write(gif_bytes)

