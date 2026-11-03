# Knowledge-graph-based spacecraft engineering using
# CAD-derived mass properties and electrical power-budget data,
# integrated through RDF and SPARQL.
# this uses dummy data for now, autocad modelling can wait
import re
from pathlib import Path

from rdflib import Graph

report = next(Path(__file__).resolve().parents[1].rglob("*.mpr")).read_text()

graph = Graph().parse(
    data=f"""
    @prefix sc: <https://example.org/cubesat#> .

    sc:MountingBracket
        sc:volumeMm3 {re.search(r"Volume:\s*([\d.]+)", report).group(1)} ;
        sc:massUnitDensity {re.search(r"Mass:\s*([\d.]+)", report).group(1)} ;
        sc:inertiaXUnitDensity {re.search(r"Moments of inertia:\s*X:\s*([\d.]+)", report).group(1)} .
    """,
    format="turtle",
)

graph.serialize(destination=Path(__file__).with_suffix(".ttl"), format="turtle")

print(graph.serialize(format="turtle"))
