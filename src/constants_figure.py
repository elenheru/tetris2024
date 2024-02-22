from pygame.colordict import THECOLORS

figures_shapes_tuple = ("i", "s", "z", "l", "j", "o", "t")

figures_colors = {
    figures_shapes_tuple[0]: THECOLORS["linen"],
    figures_shapes_tuple[1]: THECOLORS["gold"],
    figures_shapes_tuple[2]: THECOLORS["forest" + "green"],
    figures_shapes_tuple[3]: THECOLORS["dodger" + "blue"],
    figures_shapes_tuple[4]: THECOLORS["turquoise2"],
    figures_shapes_tuple[5]: THECOLORS["purple"],
    figures_shapes_tuple[6]: THECOLORS["red2"]
}

figures_structures = {
    figures_shapes_tuple[0]: (
        {(0, 0), (1, 0), (2, 0), (3, 0)},
        {(0, 0), (0, 1), (0, 2), (0, 3)}
    ),
    figures_shapes_tuple[1]: (
        {(0, 0), (0, 1), (1, 1), (1, 2)},
        {(0, 1), (1, 1), (1, 0), (2, 0)}
    ),
    figures_shapes_tuple[2]: (
        {(0, 1), (1, 0), (1, 1), (0, 2)},
        {(0, 0), (1, 0), (1, 1), (2, 1)}
    ),
    figures_shapes_tuple[3]: (
        {(0, 0), (0, 1), (0, 2), (1, 2)},
        {(0, 0), (1, 0), (2, 0), (0, 1)},
        {(0, 0), (1, 0), (1, 1), (1, 2)},
        {(2, 0), (0, 1), (1, 1), (2, 1)}
    ),
    figures_shapes_tuple[4]: (
        {(1, 0), (1, 1), (0, 2), (1, 2)},
        {(0, 0), (0, 1), (1, 1), (2, 1)},
        {(0, 0), (1, 0), (0, 1), (0, 2)},
        {(0, 0), (1, 0), (2, 0), (2, 1)}
    ),
    figures_shapes_tuple[5]: (
        {(0, 0), (1, 0), (0, 1), (1, 1)},
    ),
    figures_shapes_tuple[6]: (
        {(0, 0), (1, 0), (2, 0), (1, 1)},
        {(0, 1), (1, 0), (1, 1), (1, 2)},
        {(0, 1), (1, 0), (1, 1), (2, 1)},
        {(0, 0), (0, 1), (0, 2), (1, 1)}
    )
}

figures_shapes_list = list(figures_shapes_tuple)
