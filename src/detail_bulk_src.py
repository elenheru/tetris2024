from parameters import PARAMETERS
from pygame.colordict import THECOLORS


class Bulk:
    empty_block_color = THECOLORS["black"]
    grid_color = THECOLORS["gray10"]

    def __init__(self):
        self.field_size = (
            PARAMETERS["playground_width"],
            PARAMETERS["playground_height"]
        )
        self.block_size = PARAMETERS["block_size"]
        self.occupation_mask = list()
        self.color_mask = list()
        self.clean_bulk()
        self.complete_lines = list()

    def check_collision(self, blocks: set[tuple[int]]):
        for b in blocks:
            if b[0] < 0:
                return True
            if b[1] < 0:
                return True
            if b[0] >= self.field_size[0]:
                return True
            if b[1] >= self.field_size[1]:
                return True
            if self.occupation_mask[b[0]][b[1]]:
                return True
        return False

    def join_block(self, position: tuple[int], color: tuple[int]):
        if self.occupation_mask[position[0]][position[1]]:
            raise Exception("block %d %d is already in bulk" % position)
        else:
            self.occupation_mask[position[0]][position[1]] = True
            self.color_mask[position[0]][position[1]] = color

    def get_complete_lines(self):
        self.complete_lines.clear()
        for y in range(self.field_size[1]):
            line = tuple(
                self.occupation_mask[x][y] for x in range(self.field_size[0])
            )
            if all(line):
                self.complete_lines.append(y)
        return self.complete_lines

    def clean_complete_lines_and_return_score(self):
        score_to_add = self._count_score_add()
        for y in self.complete_lines:
            for x in range(self.field_size[0]):
                row = self.occupation_mask[x][0:y]
                self.occupation_mask[x][1:y + 1] = row
                self.occupation_mask[x][0] = False
                c_row = self.color_mask[x][0:y]
                self.color_mask[x][1:y + 1] = c_row
                self.color_mask[x][0] = Bulk.empty_block_color
        self.complete_lines.clear()
        return score_to_add

    def _count_score_add(self):
        return len(self.complete_lines)

    def clean_bulk(self):
        self.occupation_mask = list(
            list(False for _h in range(PARAMETERS["playground_height"]))
            for _w in range(PARAMETERS["playground_width"])
        )
        self.color_mask = list(
            list(Bulk.empty_block_color for _h in range(PARAMETERS["playground_height"]))
            for _w in range(PARAMETERS["playground_width"])
        )