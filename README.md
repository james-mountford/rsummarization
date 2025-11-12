# Recursive Semantic Knowledge Graph (WIP)

> **Status:** Active Work-in-Progress  
> This repository is in early development. Core modules are under construction.

## Project Goals
- Recursive summarization pipeline – automatically build hierarchical summaries from raw text (sentence → paragraph → section → document).
- Lateral semantic linking – connect related concepts across documents using embeddings and similarity thresholds.
- Graph-based exploration – enable both machine traversal (for reasoning/explanation) and human exploration via a visual UI.
- Explainable substrate for LLMs – provide an interpretable, pre-computed graph of meaning for reasoning, provenance, and evidence tracing.

---

## Project Summary

The system ingests one or more documents and builds a hierarchical, traceable knowledge graph by recursively summarizing text from atomic facts (sentences) up through paragraphs, sections, and full documents.  
Each summary node contains hyperlinks to its source nodes, allowing vertical navigation (“drill-down”) and provenance tracking.

After this vertical tree is built, a second pass computes lateral links — semantic connections between related concepts or examples across or within documents — using embeddings and similarity thresholds.  
The result is a multi-layer graph where ideas are connected both hierarchically and associatively.

A local or API-connected LLM can then navigate the graph via a traversal tool, following hyperlinks (constrained by depth ≈20–30 steps and contextual metadata) to answer queries, trace reasoning paths, or cite evidence.

Users can also explore the same structure through a visual UI that lets them zoom from high-level topics down to original text fragments.

---

## Current Focus
- Text ingestion and paragraph/sentence segmentation (`IngestChunkStore`)
- Architecture for recursive summarization
- Prototype schema for graph nodes and links

---

## Vision
The system aims to become a pre-computed, interpretable knowledge substrate — a map of meaning that enables fast, explainable reasoning for both humans and LLMs.