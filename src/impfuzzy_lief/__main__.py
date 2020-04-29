from argparse import ArgumentParser

from .core import compute_impfuzzy_from_file


def _main() -> None:
    parser = ArgumentParser(description="compute impfuzzy of PE file")
    parser.add_argument("-i", "--in_file", action="store", type=str, required=True)
    args = parser.parse_args()
    impfuzzy = compute_impfuzzy_from_file(args.in_file)
    print(f"{args.in_file} -> {impfuzzy}")


if __name__ == "__main__":
    _main()
