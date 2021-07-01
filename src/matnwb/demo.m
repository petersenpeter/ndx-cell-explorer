%% generate extension (only needs to be done when extenion is changed)
generateExtension('../../spec/ndx-cell-explorer.namespace.yaml')

%% write
nwb = NwbFile( ...
    'session_description', 'mouse in open exploration',...
    'identifier', 'Mouse5_Day3', ...
    'session_start_time', datetime(2018, 4, 25, 2, 30, 3), ...
    'general_experimenter', 'My Name', ... % optional
    'general_session_id', 'session_1234', ... % optional
    'general_institution', 'University of My Institution', ... % optional
    'general_related_publications', 'DOI:10.1016/j.neuron.2016.12.011'); % optional

cell_explorer_general = types.ndx_cell_explorer.CellExplorerGeneral( ...
    'chanCoords_layout', 'test', ...
    'chanCoords_source', 'test', ... % doc for source
    'chanCoords_x', [1,2,3]', ... % doc for x
    'saveAs', 'test_save', ... % doc for saveAs %'session_sessionType', 'Chronic', ... % doc for sessionType
    'session_spikeSortingMethod', 'kilosort' ...
    );

nwb.general.set('cell_explorer_general', cell_explorer_general)

nwbExport(nwb, 'test_file.nwb')

%% read

nwb2 = nwbRead('test_file.nwb');

nwb2.general.get('cell_explorer_general').chanCoords_x.load