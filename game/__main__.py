import sys

from game import patterns, views
from game.cli import get_command_line_args
from game.pygame_view import PygameView

def main():
    args = get_command_line_args()
    if args.view == "PygameView":
        View  =PygameView
    else:
        View = getattr(views, args.view)
    if args.all:
        for pattern in patterns.get_all_patterns():
            _show_pattern(View, pattern, args)
    else:
        _show_pattern(
            View,
            patterns.get_pattern(name=args.pattern),
            args
        )
    # View = getattr(views, args.view)
    # if args.all:
    #     for pattern in patterns.get_all_patterns():
    #         _show_pattern(View, pattern, args)
    # else:
    #     _show_pattern(
    #         View,
    #         patterns.get_pattern(name=args.pattern),
    #         args
    #     )

def _show_pattern(View, pattern, args):
    try:
        View(pattern=pattern, gen=args.gen, frame_rate=args.fps).show()
    except Exception as error:
        print(error, file=sys.stderr)


if __name__ == "__main__":
    main()