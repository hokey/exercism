"""
Markdown Parser Utility
"""
import re
from collections.abc import Callable
from re import Match, Pattern
from dataclasses import dataclass
from functools import partial
from typing import Optional


@dataclass(frozen=True)
class MarkdownRule:
    """
    Markdown Rule Class
    """
    pattern: Pattern[str]
    handler: Callable
    is_list_item: bool = False

def render_block_tag(tag: str, text: str) -> str:
    """
    Renders a html block tag
    :param tag: Tag to render
    :param text: The text to render
    :return: Rendered html block
    """
    text = render_inline_tags(text)
    return f"<{tag}>{text}</{tag}>"

def render_inline_tag(tag: str, match: Match[str]) -> str:
    """
    Renders an inline html tag

    :param tag: Tag to render
    :param match: The matched group
    :return: The rendered tag
    """
    return f"<{tag}>{match.group(1)}</{tag}>"

def render_inline_tags(text: str) -> str:
    """
    Renders a group of inline tags
    :param text: The text to render
    :return: Rendered text
    """
    for rule in INLINE_RULES:
        text = rule.pattern.sub(rule.handler, text)
    return text

BLOCK_RULES: list[MarkdownRule] = [
    MarkdownRule(re.compile(r"^# (.*)"), partial(render_block_tag, "h1") ),
    MarkdownRule(re.compile(r"^## (.*)"), partial(render_block_tag, "h2")),
    MarkdownRule(re.compile(r"^### (.*)"), partial(render_block_tag, "h3")),
    MarkdownRule(re.compile(r"^#### (.*)"), partial(render_block_tag, "h4")),
    MarkdownRule(re.compile(r"^##### (.*)"), partial(render_block_tag, "h5")),
    MarkdownRule(re.compile(r"^###### (.*)"), partial(render_block_tag, "h6")),
    MarkdownRule(re.compile(r"^\* (.*)"), partial(render_block_tag, "li"), True)
]

INLINE_RULES: list[MarkdownRule] = [
    MarkdownRule(re.compile(r"(?<!_)_([^_]+)_(?!_)"), partial(render_inline_tag, "em")),
    MarkdownRule(re.compile(r"__(.*?)__"), partial(render_inline_tag, "strong"))
]

def parse(markdown:str) -> str:
    """
    Parse a markdown string and return a rendered html string
    :param markdown: Markdown string
    :return: html string
    """
    lines: list[str] = markdown.split("\n")
    result: list[str] = []
    in_list: bool = False
    for line in lines:
        matched: bool = False
        for rule in BLOCK_RULES:
            match: Optional[Match[str]] = rule.pattern.match(line)
            if not match:
                continue
            matched = True

            text: str  = match.group(1)

            if rule.is_list_item:
                if not in_list:
                    result.append("<ul>")
                    in_list = True
                result.append(rule.handler(text))
            else:
                if in_list:
                    result.append("</ul>")
                    in_list = False
                result.append(rule.handler(text))
            break
        if not matched:
            if in_list:
                result.append("</ul>")
                in_list = False
            result.append(render_block_tag("p", line))
    if in_list:
        result.append("</ul>")

    return "".join(result)