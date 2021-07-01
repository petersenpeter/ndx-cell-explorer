import datetime

from pynwb import NWBHDF5IO, NWBFile
from pynwb.testing import TestCase, remove_test_file

from ndx_cell_explorer import CellExplorerGeneral


def set_up_nwbfile():
    nwbfile = NWBFile(
        session_description='session_description',
        identifier='identifier',
        session_start_time=datetime.datetime.now(datetime.timezone.utc)
    )

    return nwbfile


class TestTetrodeSeriesConstructor(TestCase):

    def setUp(self):
        """Set up an NWB file. Necessary because TetrodeSeries requires references to electrodes."""
        self.nwbfile = set_up_nwbfile()

    def test_constructor(self):
        """Test that the constructor for CellExplorerGeneral sets values as expected."""
        cell_explorer_general = CellExplorerGeneral(
            session__sessionType="Chronic",
            session__spikeSortingMethod="KiloSort",
            chanCoords__source="probeImplants",
            chanCoords__layout="staggered",
            chanCoords__x=[1, 2, 3, 4, 5],
            saveAs="cell_metrics"
        )


class CellExplorerGeneralSeriesRoundtrip(TestCase):
    """Simple roundtrip test for TetrodeSeries."""

    def setUp(self):
        self.nwbfile = set_up_nwbfile()
        self.path = 'test.nwb'

    def tearDown(self):
        remove_test_file(self.path)

    def test_roundtrip(self):
        """
        Add a TetrodeSeries to an NWBFile, write it to file, read the file, and test that the TetrodeSeries from the
        file matches the original TetrodeSeries.
        """

        cell_explorer_general = CellExplorerGeneral(
            session__sessionType="Chronic",
            session__spikeSortingMethod="KiloSort",
            chanCoords__source="probeImplants",
            chanCoords__layout="staggered",
            chanCoords__x=[1, 2, 3, 4, 5],
            saveAs="cell_metrics"
        )

        self.nwbfile.add_lab_meta_data(cell_explorer_general)

        with NWBHDF5IO(self.path, mode='w') as io:
            io.write(self.nwbfile)

        with NWBHDF5IO(self.path, mode='r', load_namespaces=True) as io:
            read_nwbfile = io.read()
            self.assertContainerEqual(
                cell_explorer_general,
                read_nwbfile.lab_meta_data["cell_explorer_general"]
            )
