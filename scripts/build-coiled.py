import goes_ortho as go
import xarray as xr
import geogif


go.get_data.make_request_json('goes-build-zarr', '${{ inputs.startDatetime }}', '${{ inputs.endDatetime }}', \
          [${{ inputs.min_lon }}, ${{ inputs.min_lat }}, ${{ inputs.max_lon }}, ${{ inputs.max_lat }}], \
          '${{ inputs.satellite }}', '${{ inputs.product }}', ${{ inputs.band }}, '${{ inputs.variable }}', '${{ secrets.OPENTOPO_API_KEY }}')

go.get_data.build_zarr('goes-build-zarr.json')

ds = xr.open_zarr('goes-build-zarr.zarr')
da = ds.${{ inputs.variable }}
gif_bytes = geogif.dgif(da, fps=5, cmap='Greys_r', date_format='%Y-%m-%d %H:%M:%S', date_position='ul', bytes=True).compute()
with open('goes.gif', 'wb') as f:
  f.write(gif_bytes)
