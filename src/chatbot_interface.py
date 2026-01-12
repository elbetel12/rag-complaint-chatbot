# src/chatbot_interface.py - SIMPLIFIED WORKING VERSION
"""
Chatbot Interface - WORKING VERSION
"""

import time

class ChatbotInterface:
    """Interface for the RAG chatbot."""
    
    def __init__(self, rag_pipeline):
        self.rag_pipeline = rag_pipeline
        self.conversation_history = []
        print(f"🤖 ChatbotInterface initialized")
    
    def process_query(self, question: str, show_sources: bool = True, 
                     show_timing: bool = True) -> str:
        """Process a user query."""
        print(f"💭 Processing: '{question}'")
        
        try:
            # Get response from RAG pipeline
            response = self.rag_pipeline.query(question, k=5)
            
            # Check if response is valid
            if response is None:
                return "Sorry, I couldn't process your question. Please try again."
            
            if 'answer' not in response:
                return "No answer generated. Please try a different question."
            
            # Extract answer
            answer = response.get('answer', 'No answer generated.')
            
            # Add sources if requested
            if show_sources and response.get('chunks'):
                answer += self._format_sources(response['chunks'])
            
            # Add timing if requested
            if show_timing:
                total_time = response.get('total_time', 0)
                answer += f"\n\n⏱️ **Processing time:** {total_time:.2f}s"
            
            # Store in history
            self.conversation_history.append({
                'question': question,
                'answer': answer,
                'timestamp': time.strftime("%H:%M:%S")
            })
            
            return answer
            
        except Exception as e:
            error_msg = f"Sorry, I encountered an error: {str(e)[:50]}"
            print(f"❌ Error: {e}")
            return f"⚠️ {error_msg}"
    
    def _format_sources(self, chunks):
        """Format retrieved chunks as sources."""
        if not chunks:
            return ""
        
        sources_text = "\n\n📚 **Sources:**\n"
        
        for i, chunk in enumerate(chunks[:3]):  # Show top 3
            meta = chunk.get('metadata', {})
            product = meta.get('product', meta.get('product_category', 'Unknown'))
            text = chunk.get('text', '')
            
            # Truncate
            if len(text) > 100:
                text = text[:100] + "..."
            
            sources_text += f"{i+1}. **{product}**: {text}\n"
        
        return sources_text
    
    def get_suggested_questions(self):
        """Get suggested questions for users."""
        return [
            "What are common credit card complaints?",
            "Why are loan applications denied?",
            "Tell me about billing disputes",
            "What fraud complaints are reported?"
        ]