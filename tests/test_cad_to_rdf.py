from pathlib import Path

from rdflib import Namespace

from src.cad_to_rdf import to_rdf


def test_cad_to_rdf():
    graph = to_rdf(Path("data/mounting_bracket.mpr").read_text())

    assert (
        str(
            graph.value(
                Namespace(
                    "https://github.com/btinic/spacecraft-knowledge-graph#"
                ).MountingBracket,
                Namespace(
                    "https://github.com/btinic/spacecraft-knowledge-graph#"
                ).volumeMm3,
            )
        )
        == "103889.3464"
    )
    assert (
        str(
            graph.value(
                Namespace(
                    "https://github.com/btinic/spacecraft-knowledge-graph#"
                ).MountingBracket,
                Namespace(
                    "https://github.com/btinic/spacecraft-knowledge-graph#"
                ).centroidXmm,
            )
        )
        == "-991.0149"
    )
    assert (
        str(
            graph.value(
                Namespace(
                    "https://github.com/btinic/spacecraft-knowledge-graph#"
                ).MountingBracket,
                Namespace(
                    "https://github.com/btinic/spacecraft-knowledge-graph#"
                ).principalInertiaIUnitDensity,
            )
        )
        == "35770804.0520"
    )
