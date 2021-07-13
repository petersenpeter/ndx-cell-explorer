# -*- coding: utf-8 -*-
import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec, NWBDatasetSpec
# TODO: import other spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc="""Extension for saving metadata necessary for full round trip in CellExplorer""",
        name="""ndx-cell-explorer""",
        version="""0.1.1""",
        author=list(map(str.strip, """Peter Petersen""".split(','))),
        contact=list(map(str.strip, """petersen.peter@gmail.com""".split(',')))
    )

    # TODO: specify the neurodata_types that are used by the extension as well
    # as in which namespace they are found.
    # this is similar to specifying the Python modules that need to be imported
    # to use your new data types.
    # all types included or used by the types specified here will also be
    # included.
    ns_builder.include_type('LabMetaData', namespace='core')

    # TODO: define your new data types
    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb
    # for more information
    CellExplorerGeneral = NWBGroupSpec(
        name="cell_explorer_general",
        neurodata_type_def='CellExplorerGeneral',
        neurodata_type_inc='LabMetaData',
        doc="metadata necessary for full round trip in CellExplorer",
        groups=[
            NWBGroupSpec(
                name="session",
                doc="holds session info",
                datasets=[
                    NWBDatasetSpec(
                        name="sessionType",
                        dtype="text",
                        doc="doc for sessionType",
                        quantity='?'
                    ),
                    NWBDatasetSpec(
                        name="spikeSortingMethod",
                        dtype="text",
                        doc="doc for spikeSortingMethod",
                        quantity='?'
                    ),
                    NWBDatasetSpec(
                        name="investigator",
                        dtype="text",
                        doc="doc for investigator",
                        quantity='?'
                    )
                ]
            ),
            NWBGroupSpec(
                name="isis",
                doc="holds ISI info",
                datasets=[
                    NWBDatasetSpec(
                        name="log10",
                        dtype="float",
                        doc="doc for log10",
                        shape=(None,),
                        dims=('nbins',),
                        quantity='?'
                    )
                ]
            ),
            NWBGroupSpec(
                name="acgs",
                doc="holds ACG info",
                datasets=[
                    NWBDatasetSpec(
                        name="log10",
                        dtype="float",
                        doc="doc for log10",
                        shape=(None,),
                        dims=('nbins',),
                        quantity='?'
                    )
                ]
            )
        ],
        datasets=[
            NWBDatasetSpec(
                name="saveAs",
                dtype="text",
                doc="doc for saveAs",
                quantity='?'
            )
        ]
    )

    # # # # # # # # # # # # # # # # # # # #
    # chanCoords - channel coordinates
    chanCoords = NWBGroupSpec(neurodata_type_def='chanCoords',
        neurodata_type_inc='LabMetaData',
        name='chanCoords',
        doc="channel coordinates",
        datasets=[
            NWBDatasetSpec(
                name="source",
                dtype="text",
                doc="doc for source",
                quantity='?'
            ),
            NWBDatasetSpec(
                name="layout",
                dtype="text",
                doc="doc for layout",
                quantity='?'
            ),
            NWBDatasetSpec(
                name="shankSpacing",
                dtype="float",
                doc="doc for shankSpacing",
                quantity='?'
            ),
            NWBDatasetSpec(
                name="x",
                dtype="float",
                doc="doc for x",
                shape=(None,),
                dims=('nchans',),
                quantity='?'
            ),
            NWBDatasetSpec(
                name="y",
                dtype="float",
                doc="doc for y",
                shape=(None,),
                dims=('nchans',),
                quantity='?'
            )
        ]
    )

    # # # # # # # # # # # # # # # # # # # #
    # Firing rate maps
    firingRateMap = NWBGroupSpec(neurodata_type_def='firingRateMap',
        neurodata_type_inc='NWBDataInterface',
        doc='Firing rate map attributes', quantity='*',
        datasets=[
            NWBDatasetSpec(
                name="name",
                dtype="text",
                doc="name of firingRateMap",
            ),
            NWBDatasetSpec(
                name="x_bins",
                dtype="float",
                doc="bins of the firing rate map",
                shape=(None,),
                dims=('x_bins',),
                quantity='?'
            ),
            NWBDatasetSpec(
                name="boundaries",
                dtype="float",
                doc="boundaries of firing rate map",
                shape=(None,),
                dims=('boundaries',),
                quantity='?'
            ),
            NWBDatasetSpec(
                name="labels",
                dtype="text",
                doc="labels of firing rate map",
                quantity='?'
            )
                ]
        )

    firingRateMaps = NWBGroupSpec(neurodata_type_def='firingRateMaps',
       neurodata_type_inc='LabMetaData',
       name='firingRateMaps',
       doc='A group of firing rate maps', 
       quantity='?',
       groups=[firingRateMap])

    # # # # # # # #
    # Event data
    eventdata = NWBGroupSpec(neurodata_type_def='eventdata',
        neurodata_type_inc='NWBDataInterface',
        doc='event data attributes', quantity='*',
        datasets=[
            NWBDatasetSpec(
                name="name",
                dtype="text",
                doc="name of events",
            ),
            NWBDatasetSpec(
                name="x_bins",
                dtype="float",
                doc="bins of the event",
                shape=(None,),
                dims=('x_bins',),
                quantity='?'
            ),
            NWBDatasetSpec(
                name="event_file",
                dtype="text",
                doc="source file of events",
                quantity='?'
            ),
            NWBDatasetSpec(
                name="x_label",
                dtype="text",
                doc="x_label (with unit)",
                quantity='?'
            ),
            NWBDatasetSpec(
                name="alignment",
                dtype="text",
                doc="alignment of events (peaks, start, center)",
                quantity='?'
            )
        ]
    )

    Events = NWBGroupSpec(neurodata_type_def='Events',
       neurodata_type_inc='LabMetaData',
       name='Events',
       doc='A group of events', 
       quantity='?',
       groups=[eventdata])

    # # # # # # # #
    # Manipulation data
    manipulationdata = NWBGroupSpec(neurodata_type_def='manipulationdata',
        neurodata_type_inc='NWBDataInterface',
        doc='manipulation data attributes', quantity='*',
        datasets=[
            NWBDatasetSpec(
                name="name",
                dtype="text",
                doc="name of manipulation data",
            ),
            NWBDatasetSpec(
                name="x_bins",
                dtype="float",
                doc="bins of the firing rate map",
                shape=(None,),
                dims=('x_bins',),
                quantity='?'
            ),
            NWBDatasetSpec(
                name="event_file",
                dtype="text",
                doc="source file of events",
                quantity='?'
            ),
            NWBDatasetSpec(
                name="x_label",
                dtype="text",
                doc="x_label (with unit)",
                quantity='?'
            ),
            NWBDatasetSpec(
                name="alignment",
                dtype="text",
                doc="alignment of events (peaks, start, center)",
                quantity='?'
            )
        ]
    )

    manipulations = NWBGroupSpec(neurodata_type_def='manipulations',
       neurodata_type_inc='LabMetaData',
       name='manipulations',
       doc='A group of manipulations', 
       quantity='?',
       groups=[manipulationdata])

    # # # # # # # # # 
    # Response curves
    responseCurve = NWBGroupSpec(neurodata_type_def='responseCurve',
        neurodata_type_inc='NWBDataInterface',
        doc='ResponseCurve attributes', quantity='*',
        datasets=[
            NWBDatasetSpec(
                name="name",
                dtype="text",
                doc="name of response curve",
            ),
            NWBDatasetSpec(
                name="x_bins",
                dtype="float",
                doc="bins of the firing rate map",
                shape=(None,),
                dims=('x_bins',),
                quantity='?'
            ),
            NWBDatasetSpec(
                name="x_edges",
                dtype="float",
                doc="edges of the firing rate map",
                shape=(None,),
                dims=('x_edges',),
                quantity='?'
            )
                ]
        )

    responseCurves = NWBGroupSpec(neurodata_type_def='responseCurves',
       neurodata_type_inc='LabMetaData',
       name='responseCurves',
       doc='A group of response curves', 
       quantity='?',
       groups=[responseCurve])

    # TODO: add all of your new data types to this list
    new_data_types = [CellExplorerGeneral,chanCoords,firingRateMaps,responseCurves, Events, manipulations]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == '__main__':
    # usage: python create_extension_spec.py
    main()
