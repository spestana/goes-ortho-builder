# GOES Ortho Builder
This repository allows you to run [goespy](https://github.com/spestana/goes-py) and [goes-ortho](https://github.com/spestana/goes-ortho) utilities to download, orthorectify (apply a terrain correction), and build a zarr file of GOES-R ABI imagery through a Github Actions interface.


## How to use GOES Ortho Builder

* Fork this repository
* Make a user account and generate an API key for [OpenTopography.org](https://portal.opentopography.org/requestService?service=api)
* Create an [Actions secret](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions) for this API key: `OPENTOPO_API_KEY` (This allows the workflow to download a DEM from OpenTopography.org, used for the terrain correction applied to the imagery)

### Build
* Under the *Actions* repository tab, click on the *Build* workflow
* Select the *Run workflow* dropdown menu, and specify the required information:
  * **Use workflow from**: Branch: main (there is currently only one version of this workflow)
  * **startDatetime**: starting date and time to get GOES imagery (in the format `YYYY-MM-DDThh:mm:ssZ`, all times UTC)
  * **endDatetime**: end date and time to get GOES imagery
  * **min_lon**: minimum longitude bound of the region to retrieve imagery of
  * **min_lat**: minimum latitude bound
  * **max_lon**: maximum longitude bound
  * **max_lat**: maximum longitude bound
  * **satellite**: goes16, goes17, or goes18 (each satellite has different dates of data availiability, view angles, and varying spatial resolutions)
  * **product**: ABI imagery product (currently limited to top of atmosphere radiance products for CONUS and Full Disk)
  * **band**: ABI band if applicable for the selected product (otherwise this field is ignored, spatial resolutions vary by band)
  * **variable**: Variable from the selected product if applicable (otherwise this field is ignored, currently limited to Radiance and Data Quality Field variables)
* The time it takes for the workflow to run depends on the product, band, spatial extents, and start & end times. Progress can be monitored by clicking on the 'goes-build-zarr' job within the 'Build' run.
* Upon completion, you will see an item within the action run under *Artifacts*. This is a zip folder containing the zarr file, a json file specifying the details of the workflow run, and a gif animation to preview the imagery.

### Build Merged
* Under the *Actions* repository tab, click on the *Build Merged* workflow
* Select the *Run workflow* dropdown menu, and specify the required information:
  * **Use workflow from**: Branch: main (there is currently only one version of this workflow)
  * **startDatetime**: starting date and time to get GOES imagery (in the format `YYYY-MM-DDThh:mm:ssZ`, all times UTC)
  * **endDatetime**: end date and time to get GOES imagery
  * **min_lon**: minimum longitude bound of the region to retrieve imagery of
  * **min_lat**: minimum latitude bound
  * **max_lon**: maximum longitude bound
  * **max_lat**: maximum longitude bound
  * **product**: ABI imagery product (in the format `ABI-L1b-RadF` or `ABI-L2-LSTC`)
  * **band**: ABI band if applicable for the selected product (otherwise this field is ignored, spatial resolutions vary by band)
  * **variable**: Variable from the selected product if applicable, e.g. `Rad`, `LST`, or `DQF` (otherwise this field is ignored)
* The time it takes for the workflow to run depends on the product, band, spatial extents, and start & end times. Progress can be monitored by clicking on the 'goes-build-zarr' job within the 'Build' run.
* Upon completion, you will see an item within the action run under *Artifacts*. This is a zip folder containing three zarr files, two json files specifying the details of the workflow run that downloaded goes16 and goes18 imagery, and three gif animations to preview the imagery.



## Ackowledgments
* [University of Washington eScience Winter Incubator 2024](https://escience.washington.edu/incubator-24-glacial-lakes/)
* This was developed using the [actions-batch-demo](https://github.com/relativeorbit/actions-batch-demo)
* Improvements to GOES data processing with zarr from [summerfog](https://github.com/autumn-yng/summerfog) REU project at UW Friday Harbor Labs
* Utilities from [Geospatial Time Series Analysis](https://github.com/friedrichknuth/gtsa)
