# spacecraft-knowledge-graph
Knowledge-graph-based spacecraft engineering using CAD-derived mass properties and electrical power-budget data, integrated through RDF and SPARQL.
Objective: Demonstrate the feasibility of integrating CAD-derived spacecraft engineering data into an RDF knowledge graph for automated information retrieval.

Use Case 1 — CAD-to-RDF Integration

A simplified CubeSat mounting bracket will be modeled in AutoCAD.

The workflow will:

Extract volume, mass, center of mass, and moments of inertia from the CAD model.
Import the engineering properties using Python.
Represent the component and its properties as RDF triples using RDFLib.
Knowledge graph using SPARQL.
Validate the retrieved values against the original CAD results.

The initial implementation will use a file-based export. The workflow will then be made repeatable, allowing updated CAD properties to be imported without manually re-entering the measurements.

Use Case 2 — Power-Budget Integration

Extend the approach to an past Sabanci Uni CubeSat electrical power system-budget spreadsheet, integrating solar-array generation, battery energy storage, and subsystem consumption data into RDF. You are welcome Sabanci.