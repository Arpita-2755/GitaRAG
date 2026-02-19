import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


class GitaRetriever:
    def __init__(self,
                 index_path="gita_index.faiss",
                 metadata_path="metadata.npy"):

        self.index = faiss.read_index(index_path)
        self.metadata = np.load(metadata_path, allow_pickle=True)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def expand_query(self, query):
        expansions = {
            "dear": "beloved devotion bhakti",
            "cosmic form": "universal form vishvarupa divine form",
            "soul": "self atman eternal immortal",
            "duty": "karma action obligation",
        }

        expanded = query.lower()

        for k, v in expansions.items():
            if k in expanded:
                expanded += " " + v

        return expanded

    def search(self, query, top_k=5, similarity_threshold=0.45):

        expanded_query = self.expand_query(query)

        query_embedding = self.model.encode(
            [expanded_query],
            convert_to_numpy=True
        )

        faiss.normalize_L2(query_embedding)

        similarities, indices = self.index.search(query_embedding, top_k)

        results = []
        similarity_scores = []

        for i, idx in enumerate(indices[0]):
            similarity = float(similarities[0][i])

            if similarity >= similarity_threshold:
                verse_data = self.metadata[idx]

                similarity_scores.append(similarity)

                results.append({
                    "chapter": verse_data["chapter"],
                    "verse": verse_data["verse"],
                    "verse_text": verse_data["verse_text"],
                    "commentary": verse_data["commentary"],
                    "similarity": round(similarity, 4)
                })

        if not results:
            return {
                "status": "insufficient_context",
                "confidence": 0.0,
                "results": []
            }

        confidence = float(np.mean(similarity_scores))

        return {
            "status": "success",
            "confidence": round(confidence, 4),
            "results": results
        }
