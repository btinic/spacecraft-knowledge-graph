# spacecraft-knowledge-graph
Knowledge-graph-based spacecraft engineering using CAD-derived mass properties and electrical power-budget data, integrated through RDF and SPARQL.
Objective: Demonstrate the feasibility of integrating CAD-derived spacecraft engineering data into an RDF knowledge graph for automated information retrieval.

Use Case 1 — CAD-to-RDF Integration

A simplified CubeSat mounting bracket was modeled in AutoCAD.

The workflow has been implemented as follows:

Extract volume, unit-density mass, center of mass, and moments of inertia from the CAD model using AutoCAD's MASSPROP.
Export the mass-property report to data/mounting_bracket.mpr.
Import the engineering properties using Python.
Represent the component and its properties as RDF triples using RDFLib.
Query the generated knowledge graph using SPARQL.
Validate the retrieved values against the original CAD results.

The initial implementation uses a file-based export. The workflow is now repeatable, allowing updated CAD properties to be imported without manually re-entering the measurements.

The Python scripts cad_to_rdf.py and interrogate_the_bracket.py perform the RDF conversion and SPARQL retrieval, respectively. 

Both can be executed through dedicated VS Code debugger configurations.Two automated pytest tests verify the extracted mechanical properties and SPARQL query results against the original AutoCAD data. 

Use Case 2 — Power-Budget Integration

Extend the approach to an past Sabanci Uni CubeSat electrical power system-budget spreadsheet, integrating solar-array generation, battery energy storage, and subsystem consumption data into RDF. You are welcome Sabanci.