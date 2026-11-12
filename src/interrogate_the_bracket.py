# Query the RDF knowledge graph for CAD-derived bracket properties using SPARQL :)
from rdflib import Graph


def run() -> None:
    print(
        *Graph()
        .parse("rdf/mounting_bracket.ttl", format="turtle")
        .query("""
        PREFIX sc: <https://github.com/btinic/spacecraft-knowledge-graph#>

        SELECT ?volume ?centroidX ?inertiaI
        WHERE {
            sc:MountingBracket
                sc:volumeMm3 ?volume ;
                sc:centroidXmm ?centroidX ;
                sc:principalInertiaIUnitDensity ?inertiaI .
        }
    """)
    )


run()
