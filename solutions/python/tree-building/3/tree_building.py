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
    if not records:
        return None
    root: Node | None = None
    
    records = sorted(records, key=attrgetter("record_id", "parent_id"))

    if records[0].record_id != 0 or records[-1].record_id != len(records) - 1:
        raise ValueError("Record id is invalid or out of order.")

    nodes = {}

    for record in records:
        if record.record_id in nodes:
            raise ValueError("Duplicate record ID.")
        nodes[record.record_id] = Node(record.record_id)

    for record in records:
        if record.parent_id > record.record_id:
            raise ValueError("Node parent_id should be smaller than its record_id.")            
        if record.record_id == 0:
            if record.parent_id != 0:
                raise ValueError("Only root should have equal record and parent id.")
            root = nodes[0]
        else:
            if record.record_id == record.parent_id:
                raise ValueError("Only root should have equal record and parent id.")
            parent = nodes[record.parent_id]
            parent.children.append(nodes[record.record_id])
    return root