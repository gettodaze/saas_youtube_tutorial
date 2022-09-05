from __future__ import annotations

import argparse
import openai

from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def get_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("idea", type=str)
    return parser


def get_openai_text(idea: str):
    return openai.Completion.create(
        model="davinci-instruct-beta-v3",
        prompt=f"Generate a snippet about a cat {idea}:",
        max_tokens=32,
        temperature=0,
    )["choices"][0]["text"]


def main(argv: list[str] | None = None) -> None:
    parser = get_argparser()
    config = parser.parse_args(argv)
    print(get_openai_text(config.idea))


if __name__ == "__main__":
    main()
