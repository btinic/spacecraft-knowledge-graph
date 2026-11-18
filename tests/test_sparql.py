# Simple test for sparql
from decimal import Decimal

from rdflib import Graph


def test_sparql():
    result = next(
        iter(
            Graph()
            .parse("rdf/mounting_bracket.ttl")
            .query("""
        PREFIX sc: <https://github.com/btinic/spacecraft-knowledge-graph#>

        SELECT ?volume ?centroidX ?inertiaI
        WHERE {
            sc:MountingBracket sc:hasMassProperties ?properties .

            ?properties
                sc:volumeMm3 ?volume ;
                sc:hasCentroid/sc:xMm ?centroidX ;
                sc:hasPrincipalInertia/sc:iUnitDensity ?inertiaI .
        }
    """)
        )
    )

    assert result.volume.value == Decimal("103889.3464")
    assert result.centroidX.value == Decimal("-991.0149")
    assert result.inertiaI.value == Decimal("35770804.0520")
