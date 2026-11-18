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
            sc:hasMassProperties sc:BracketMassProperties ;
            sc:modeledIn sc:BracketCADModel .

        sc:BracketMassProperties
            sc:volumeMm3 {re.search(r"Volume:\s*([-\d.E+]+)", report).group(1)} ;
            sc:massUnitDensity {re.search(r"Mass:\s*([-\d.E+]+)", report).group(1)} ;
            sc:inertiaXUnitDensity {re.search(r"Moments of inertia:\s*X:\s*([-\d.E+]+)", report).group(1)} ;
            sc:hasCentroid sc:BracketCentroid ;
            sc:hasPrincipalInertia sc:BracketPrincipalInertia ;
            sc:extractedFrom sc:BracketMassReport .

        sc:BracketCentroid
            sc:xMm {centroid.group(1)} ;
            sc:yMm {centroid.group(2)} ;
            sc:zMm {centroid.group(3)} .

        sc:BracketPrincipalInertia
            sc:iUnitDensity {re.search(r"I:\s*([-\d.E+]+)", report).group(1)} ;
            sc:jUnitDensity {re.search(r"J:\s*([-\d.E+]+)", report).group(1)} ;
            sc:kUnitDensity {re.search(r"K:\s*([-\d.E+]+)", report).group(1)} .

        sc:BracketMassReport
            sc:exportedFrom sc:BracketCADModel ;
            sc:fileName "mounting_bracket.mpr" .

        sc:BracketCADModel
            sc:fileName "mounting_bracket.dwg" .

        """,
        format="turtle",
    )


def run() -> None:
    to_rdf(next(Path("data").glob("*.mpr")).read_text()).serialize(
        destination="rdf/mounting_bracket.ttl",
        format="turtle",
    )


run()
