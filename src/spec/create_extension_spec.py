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
        version="""0.1.0""",
        author=list(map(str.strip, """Ben Dichter""".split(','))),
        contact=list(map(str.strip, """ben.dichter@catalystneuro.com""".split(',')))
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
        neurodata_type_def='CellExplorerGeneral',
        neurodata_type_inc='LabMetaData',
        doc="metadata necessary for full round trip in CellExplorer",
        name="cell_explorer_general",
        groups=[
            NWBGroupSpec(
                doc="holds session info",
                name="session",
                datasets=[
                    NWBDatasetSpec(
                        doc="doc for sessionType",
                        dtype="text",
                        name="sessionType",
                    ),
                    NWBDatasetSpec(
                        doc="doc for spikeSortingMethod",
                        dtype="text",
                        name="spikeSortingMethod",
                    )
                ]
            ),
            NWBGroupSpec(
                doc="channel coordinates",
                name="chanCoords",
                datasets=[
                    NWBDatasetSpec(
                        doc="doc for source",
                        dtype="text",
                        name="source",
                    ),
                    NWBDatasetSpec(
                        doc="doc for layout",
                        dtype="text",
                        name="layout",
                    ),
                    NWBDatasetSpec(
                        doc="doc for x",
                        dtype="float",
                        shape=(None,),
                        name="x"
                    )
                ]
            )
        ],
        datasets=[
            NWBDatasetSpec(
                doc="doc for saveAs",
                dtype="text",
                name="saveAs",
            ),

        ]
    )

    # TODO: add all of your new data types to this list
    new_data_types = [CellExplorerGeneral]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == '__main__':
    # usage: python create_extension_spec.py
    main()
