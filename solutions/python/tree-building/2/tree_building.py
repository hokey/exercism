"""
Tree Building
"""
from __future__ import annotations
from operator import attrgetter
from dataclasses import dataclass, field


@dataclass
class Record:
    """
    Records to ingest
    """
    record_id: int
    parent_id: int


@dataclass
class Node:
    """
    Node of a tree
    """
    node_id: int
    children: list[Node] = field(default_factory=list)


def BuildTree(records: list[Record]) -> Node | None:
    """
    Given a list of Records, build a tree of Nodes representing the relationships.

    Assumptions: The records only contain an ID number and a parent ID number. The ID number is always between 0 (inclusive) and the length of the record list (exclusive). All records have a parent ID lower than their own ID, except for the root record, which has a parent ID that's equal to its own ID.

    :param list[Record] records: The list of Records to parse
    :return Node: The root Node of the tree
    """
    root: Node | None = None
    records: list[Record] = sorted(records, key=attrgetter("record_id", "parent_id"))
    
    if not records:
        return root
    if records[0].record_id != 0 or records[-1].record_id != len(records) - 1:
        raise ValueError("Record id is invalid or out of order.")
        
    current_parent_id: int = 0
    current_node: Node | None = None
    while records:
        current_record = records.pop(0)
        if current_record.parent_id > current_record.record_id:
            raise ValueError("Node parent_id should be smaller than its record_id.")
        if current_record.record_id > 0 and current_record.record_id == current_record.parent_id:
            raise ValueError("Only root should have equal record and parent id.")
        if current_record.record_id == 0:
            root = Node(current_record.record_id)
            current_node = root
        else:
            if current_record.parent_id == current_parent_id:
                current_node.children.append(Node(current_record.record_id))
            else:
                current_node = find_node(root, current_record.parent_id)
                current_node.children.append(Node(current_record.record_id))
    return root


def find_node(node: Node, node_id: int) -> Node:
    """
    Let's search through a tree to find a Node

    :param Node node: The starting Node to search
    :param ind node_id: The ID of the Node to find
    :return Node: This will return the found node. Note:  The tree will have it, may add checks later.
    """
    if node.node_id == node_id:
        return node
    index: int = node.children.index(next(child_node for child_node in node.children if child_node.node_id == node_id))
    return find_node(node.children[index], node_id)