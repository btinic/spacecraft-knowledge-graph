# Knowledge-graph-based spacecraft engineering using
# CAD-derived mass properties and (later) electrical power-budget data,
# integrated through RDF and SPARQL.
import re
from pathlib import Path

from rdflib import Graph


def to_rdf(report: str) -> Graph:
    centroid = re.search(
        r"Centroid:\s*X:\s*([-\d.E+]+)\s*Y:\s*([-\d.E+]+)\s*Z:\s*([-\d.E+]+)",
        report,
    )
    return Graph().parse(
        data=f"""
        @prefix sc: <https://github.com/btinic/spacecraft-knowledge-graph#> .

        sc:MountingBracket
            sc:volumeMm3 {re.search(r"Volume:\s*([-\d.E+]+)", report).group(1)} ;
            sc:massUnitDensity {re.search(r"Mass:\s*([-\d.E+]+)", report).group(1)} ;
            sc:inertiaXUnitDensity {re.search(r"Moments of inertia:\s*X:\s*([-\d.E+]+)", report).group(1)} ;
            sc:centroidXmm {centroid.group(1)} ;
            sc:centroidYmm {centroid.group(2)} ;
            sc:centroidZmm {centroid.group(3)} ;
            sc:principalInertiaIUnitDensity {re.search(r"I:\s*([-\d.E+]+)", report).group(1)} ;
            sc:principalInertiaJUnitDensity {re.search(r"J:\s*([-\d.E+]+)", report).group(1)} ;
            sc:principalInertiaKUnitDensity {re.search(r"K:\s*([-\d.E+]+)", report).group(1)} .
        """,
        format="turtle",
    )


def run() -> None:
    to_rdf(next(Path("data").glob("*.mpr")).read_text()).serialize(
        destination="rdf/mounting_bracket.ttl",
        format="turtle",
    )


run()
