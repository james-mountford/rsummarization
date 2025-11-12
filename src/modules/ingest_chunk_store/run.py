from ingest_chunk_store import IngestChunkStore
import argparse
import json

def main():
    parser = argparse.ArgumentParser(description="Run IngestChunkStore on a text file.")
    parser.add_argument("--input", require=True, help="Path to the input file to ingest")
    parser.add_argument("--output", help="Path to the output representation file")
    args = parser.parse_args()

    store = IngestChunkStore()
    chunks = store.chunk_text(args.input)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as output:
            json.dump(chunks, output, indent=2, ensure_ascii=False)
        print(f"Saved chunked structure to {args.output}.")
    else:
        print(json.dumps(chunks, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()