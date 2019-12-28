import click

from lgtm.drawer import save_with_message
from lgtm.image_source import get_image


@click.command()
@click.option("--message", "-m", default="LGTM",
              show_default=True, help="画像に乗せる文字列")
@click.argument("keyword")
def cli(keyword, message):
    """LGTM画像生成ツール"""
    lgtm(keyword, message)


def lgtm(keyword, message):
    with get_image(keyword) as fp:
        save_with_message(fp, message)
