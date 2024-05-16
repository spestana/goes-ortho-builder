# GOES Ortho Builder
This repository allows you to run [goespy](https://github.com/spestana/goes-py) and [goes-ortho](https://github.com/spestana/goes-ortho) utilities to download, orthorectify (apply a terrain correction), and build a zarr file of GOES-R ABI imagery through a Github Actions interface.

You can fork this repository and add your own secrets, then manually run the workflow from the '[Actions](https://github.com/spestana/goes-ortho-builder/actions/workflows/build-zarr.yml)' repository tab.


## Configuration

The workflow requires the following Actions secret:
* `OPENTOPO_API_KEY`
  * This allows the utilities to download a DEM from [OpenTopography.org](https://www.opentopography.org/), used for the terrain correction applied to the imagery
  * Make a user account and generate an API key [here](https://portal.opentopography.org/requestService?service=api).


## Ackowledgments
* [University of Washington eScience Winter Incubator 2024](https://escience.washington.edu/incubator-24-glacial-lakes/)
* This was developed using the [actions-batch-demo](https://github.com/relativeorbit/actions-batch-demo)
* Improvements to GOES data processing with zarr from [summerfog](https://github.com/autumn-yng/summerfog) REU project at UW Friday Harbor Labs
