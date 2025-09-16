"""
Configuration file for LLM prompts used in the summarization API.
"""

SYSTEM_INSTRUCTION = """[Role] You are a helpful assistant that summarizes text based on user preferences.

You excel at creating concise, accurate summaries that respect the user's specified length, style, and focus requirements.

Guidelines:
- For 'short' summaries: aim for 2-4 sentences or bullet points
- For 'medium' summaries: aim for 1-2 paragraphs or 5-8 bullet points  
- For 'long' summaries: aim for 2-3 paragraphs or 8-12 bullet points
- When a focus topic is provided, emphasize that topic throughout the summary
- Match the requested style exactly (bullet points, numbered lists, or paragraphs)
"""

def build_user_prompt(text: str, length: str, style: str, focus: str = None) -> str:
    """
    Constructs the user prompt for text summarization.
    
    Args:
        text: The text to summarize
        length: short, medium, or long
        style: bullet, paragraph, or numbered
        focus: Optional topic to emphasize
        
    Returns:
        Formatted prompt string
    """
    prompt = f"[Task] Summarize the following text in a {length} {style} format:\n\n{text}"
    
    if focus:
        prompt += f"\n\nSpecial emphasis: Focus particularly on aspects related to '{focus}'."
    
    return prompt