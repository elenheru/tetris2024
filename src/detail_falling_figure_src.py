import constants_figure
from parameters import PARAMETERS
from random import shuffle


class FallingFigure:
    def __init__(self):
        self.top_left_block_position = None
        self.shape = None
        self.orientation = None
        self.attach_requested = False
        self.start_point = (PARAMETERS["playground_width"] // 2 - 1, 0)

    def spawn_figure(self, shape):
        self.top_left_block_position = self.start_point
        self.shape = shape
        self.orientation = 0
        self.attach_requested = False

    def build_set_of_blocks(self, figure_shape=None, figure_position=None, figure_orientation=None):
        if figure_orientation is None:
            if self.orientation is None:
                figure_orientation = 0
            else:
                figure_orientation = self.orientation
        if figure_shape is None:
            figure_shape = self.shape
        if figure_position is None:
            figure_position = self.top_left_block_position
        block_set = set()
        for b in constants_figure.figures_structures[figure_shape][figure_orientation]:
            block_set.add(
                (b[0] + figure_position[0],
                 b[1] + figure_position[1])
            )
        return block_set

    def build_complete_list_of_block_sets(self):
        shuffle(constants_figure.figures_shapes_list)
        blocks_list = list()
        for figure_shape in constants_figure.figures_shapes_list:
            blocks_list.append(self.build_set_of_blocks(figure_shape, self.start_point, None))
        return blocks_list

    def clean_figure(self):
        self.top_left_block_position = None
        self.shape = None
        self.orientation = None
        self.attach_requested = False
