import argparse
import random

from game import __version__, patterns, views

def get_command_line_args():
    parser =  argparse.ArgumentParser(
        prog="game",
        description="Conway's Game of Life in your terminal (or window)",
    )

    parser.add_argument(
        "-p",
        "--pattern",
        choices=[pat.name for pat in patterns.get_all_patterns()],
        default="Blinker",
        help="take a pattern for the Game of Life (default: %(default)s)",
    )

    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="show all available patterns in a sequence",
    )

    parser.add_argument(
        "-v",
        "--view",
        choices=views.__all__ + ["PygameView"],
        default="CursesView",
        help="display the life grid in a specific view (default: %(default)s)",
    )

    parser.add_argument(
        "-g",
        "--gen",
        metavar="NUM_GENERATIONS",
        type=int,
        default=10,
        help="number of generations (default: %(default)s)",
    )

    parser.add_argument(
        "-f",
        "--fps",
        metavar="FRAMES_PER_SECOND",
        type=int,
        default=7,
        help="frames per second (default: %(default)s)",
    )

    parser.add_argument(
        "-n",
        "--num-patterns",
        metavar="NUM_PATTERNS",
        type=int,
        default=1,
        help="number of each pattern to add (default: %(default)s)",
    )

    parser.add_argument(
        "-r",
        "--randomize",
        action="store_true",
        help="randomize the positions of the patterns",
    )

    parser.add_argument(
        "-sr",
        "--start-row",
        metavar="START_ROW",
        type=int,
        default=0,
        help="starting row for the pattern (default: %(default)s)",
    )

    parser.add_argument(
        "-sc",
        "--start-col",
        metavar="START_COL",
        type=int,
        default=0,
        help="starting column for the pattern (default: %(default)s)",
    )

    return parser.parse_args()