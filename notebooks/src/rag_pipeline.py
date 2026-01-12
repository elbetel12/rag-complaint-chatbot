
"""
RAG Pipeline for CrediTrust Financial
Task 3 Implementation
"""

import pandas as pd
from datetime import datetime

class SimpleRetriever:
    """Simple retriever for complaint data."""

    def __init__(self, complaints_df, top_k=3):
        self.complaints_df = complaints_df
        self.top_k = top_k

    def retrieve(self, query):
        """Retrieve relevant complaints based on keyword matching."""
        query_lower = query.lower()
        results = []

        for idx, row in self.complaints_df.iterrows():
            text = str(row.get('text', '')).lower()
            if query_lower in text:
                results.append({
                    'text': row.get('text', ''),
                    'product': row.get('product', 'Unknown'),
                    'company': row.get('company', 'Unknown'),
                    'similarity': 0.9
                })

        return results[:self.top_k]

class SimpleGenerator:
    """Simple generator for responses."""

    def generate_response(self, query, retrieved_complaints):
        """Generate response based on retrieved complaints."""
        if not retrieved_complaints:
            return "No relevant complaints found."

        products = list(set([r.get('product', 'Unknown') for r in retrieved_complaints]))

        response = f"Based on {len(retrieved_complaints)} complaints about {', '.join(products)}:\n\n"

        for i, complaint in enumerate(retrieved_complaints, 1):
            response += f"{i}. {complaint.get('product', 'Unknown')} - {complaint.get('text', '')}\n"

        return response

class CrediTrustRAG:
    """Main RAG pipeline class."""

    def __init__(self, complaints_data=None):
        """Initialize the RAG pipeline."""
        if complaints_data is None:
            # Sample data if none provided
            complaints_data = [
                {
                    'text': 'Unauthorized charge on credit card.',
                    'product': 'Credit card',
                    'company': 'Bank A'
                }
            ]

        self.complaints_df = pd.DataFrame(complaints_data)
        self.retriever = SimpleRetriever(self.complaints_df)
        self.generator = SimpleGenerator()

    def answer_question(self, question):
        """Answer a question using the RAG pipeline."""
        # Retrieve relevant complaints
        retrieved = self.retriever.retrieve(question)

        # Generate response
        answer = self.generator.generate_response(question, retrieved)

        # Return result
        return {
            'question': question,
            'answer': answer,
            'num_sources': len(retrieved),
            'timestamp': datetime.now().isoformat()
        }

# Example usage
if __name__ == "__main__":
    # Create pipeline
    pipeline = CrediTrustRAG()

    # Example query
    query = "What credit card issues exist?"
    result = pipeline.answer_question(query)

    print(f"Question: {result['question']}")
    print(f"Answer: {result['answer']}")
    print(f"Sources: {result['num_sources']}")
