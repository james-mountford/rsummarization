Project summary: Recursive Semantic Knowledge Graph

The system ingests one or more documents and builds a hierarchical, traceable knowledge graph by recursively summarizing text from atomic facts (sentences) up through paragraphs, sections, and full documents. Each summary node contains hyperlinks to its source nodes, allowing vertical navigation (“drill-down”) and provenance tracking.

After this vertical tree is built, a second pass computes lateral links—semantic connections between related concepts or examples across or within documents—using embeddings and similarity thresholds. The result is a multi-layer graph where ideas are connected both hierarchically and associatively.

A local LLM (or API-connected one) can then navigate the graph via a traversal tool: following hyperlinks, constrained by depth (≈20–30 steps) and context metadata, to answer queries, trace reasoning paths, or cite evidence.

Users can also explore the same structure through a visual UI that lets them zoom from high-level topics down to original text fragments.

The system is essentially a pre-computed, interpretable knowledge substrate—a map of meaning that enables fast, explainable LLM reasoning and human exploration alike.
