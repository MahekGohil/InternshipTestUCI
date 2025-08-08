step 1: Take the blog article text.

step 2: Use the LLM to extract the main points.

Prompt: Ask the LLM to rewrite the summary for each platform (Twitter, LinkedIn, Instagram, Facebook, TikTok), giving tone/length rules for each.

Output: Get all 5 posts in a clear format (e.g., JSON or Markdown).

Save/Use: Store them or post directly.

Example Prompt:
Article : India has replied aganist President trump 25% tarrif rates.
Create 5 posts:
1. Twitter (max 280 chars)
2. LinkedIn (professional)
3. Instagram caption (casual, emojis)
4. Facebook (conversational)
5. TikTok script (3 short lines)

Return in JSON.
Methodlogy that can be used: 
Make a GUI where user can give article and prompt and select the platform for which it has to generate the post.
Using API connect the dashboard and llm model for task completion.
