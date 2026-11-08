# Application entry point / CLI interface
import sys
from .agent import PaperTrailAgent


def main():
    print("======================================================")
    print("   PaperTrail: Agentic GraphRAG Research Engine       ")
    print("======================================================\n")

    agent = PaperTrailAgent()

    while True:
        try:
            query = input("\nEnter your query (or 'exit' to quit): ").strip()
            if not query:
                continue
            if query.lower() in ["exit", "quit", "q"]:
                print("Exiting PaperTrail. Goodbye!")
                sys.exit(0)

            response = agent.run_with_evidence(query)
            print("\n---------------- RESPONSE ----------------")
            print(response.answer)
            print(
                "\n[Retrieval Evidence] "
                f"Neo4j: {response.retrieval['graph_result_count']} rows; "
                f"ChromaDB: {response.retrieval['vector_hit_count']} papers"
            )
            print("------------------------------------------")
        except KeyboardInterrupt:
            print("\nExiting PaperTrail. Goodbye!")
            sys.exit(0)


if __name__ == "__main__":
    main()
