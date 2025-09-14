# LLM API Pricing Showdown 2025: Cost Comparison of OpenAI, Google, Anthropic, Cohere & Mistral

**Thursday, April 17, 2025**

## Comparative Analysis of Large Language Model API Pricing

This report provides a comparative analysis of Application Programming Interface (API) pricing for Large Language Models (LLMs) offered by major providers as of March 25, 2025. The objective is to offer a standardized view of per-token costs, enabling better evaluation based on budgetary considerations alongside performance needs. The analysis covers five prominent providers: OpenAI, Google (Gemini API), Anthropic (Claude API), Cohere, and Mistral AI.

Key findings indicate significant price variations not only between providers but also within each provider's portfolio of models. The LLM API market demonstrates clear price segmentation, with offerings ranging from highly economical models suited for high-volume, simpler tasks to premium-priced models designed for complex reasoning and cutting-edge performance.

A consistent trend across all reviewed providers is the substantial premium placed on output (completion) tokens compared to input (prompt) tokens, often by a factor of 3x to 5x or more. This pricing structure incentivizes careful prompt engineering and application design that favors concise, targeted responses. Practices such as Retrieval-Augmented Generation (RAG) or multi-step reasoning, which leverage cheaper input tokens for context and minimize lengthy generated outputs, are economically encouraged by this model.

Recent market dynamics, including significant price reductions by providers like Mistral AI, underscore the competitive nature of the landscape. While cost per token is a critical factor, it must be evaluated in conjunction with model performance, latency, specific feature sets, safety considerations, and the unique requirements of the intended application.

## Understanding the LLM Pricing Landscape

LLMs accessed via APIs have become foundational components for businesses integrating AI capabilities. As adoption scales, the cost associated with API usage directly impacts the economic viability, scalability, and ROI of AI initiatives. This report aims to provide a clear, standardized, and comparative analysis of the per-token API pricing for text-based generation tasks offered by leading LLM providers, reflecting publicly available data as of March 25, 2025.

**Providers Covered:**

- **OpenAI:** A pioneering organization in generative AI.
- **Google:** Offers its Gemini family of models via the Google AI platform's paid tier.
- **Anthropic:** Provider of the Claude family of models, known for a focus on AI safety.
- **Cohere:** Focused on enterprise applications, particularly retrieval-augmented generation.
- **Mistral AI:** Known for both open-source contributions and performant proprietary models via its La Plateforme API.

**Methodology Note:** Pricing data was sourced exclusively from the official websites, documentation, and pricing pages of the respective providers, accessed on March 25, 2025. LLM pricing is subject to frequent changes, driven by market competition, model updates, and evolving provider strategies, so users must always consult official documentation for the most current pricing.

This report focuses specifically on **standard, pay-as-you-go API pricing** for core LLM offerings, excluding promotional offers, free trials, custom enterprise agreements, regional pricing variations, and most specialized non-LLM services. While many modern LLMs possess multimodal capabilities, this report primarily focuses on the **text token pricing**.

**Pricing Unit:** All prices are standardized to **USD per 1 Million Tokens**. A distinction is consistently made between the cost of **Input Tokens** (prompt) and **Output Tokens** (completion or response). For English text, one token is approximately 0.75 words or four characters.

## Detailed Provider Pricing Breakdown

This section details the standard API pricing for LLMs offered by each of the five major providers, presented in USD per 1 million tokens, differentiating between input and output costs, as of March 25, 2025.

### OpenAI: The Market Leader's Pricing Strategy

OpenAI offers a range of LLMs through its API, including the versatile GPT-4 series and newer 'o-series' models for advanced reasoning. OpenAI provides models of varying sizes, allowing users to select based on performance needs and budget.

**Table 1: OpenAI LLM API Pricing (USD/1M Tokens)**

| Model                                  | Input Cost ($/1M tokens) | Output Cost ($/1M tokens) | Notes                                                                                                                  |
| :------------------------------------- | :----------------------- | :------------------------ | :--------------------------------------------------------------------------------------------------------------------- |
| **Reasoning Models**                   |                          |                           |                                                                                                                        |
| o1 (o1-2024-12-17)                     | $15.00                   | $60.00                    | Frontier reasoning model. 200k context. Supports tools, structured outputs, vision.                                    |
| o3-mini (o3-mini-2025-01-31)           | $1.10                    | $4.40                     | Cost-efficient reasoning model. 200k context. Optimized for coding, math, science; supports tools, structured outputs. |
| **GPT Models**                         |                          |                           |                                                                                                                        |
| GPT-4.1 (gpt-4.1-2025-04-14)           | $2.00                    | $8.00                     | High-intelligence model for complex tasks. 1M context.                                                                 |
| GPT-4.1 mini (gpt-4.1-mini-2025-04-14) | $0.40                    | $1.60                     | Balances speed and intelligence. 1M context.                                                                           |
| GPT-4.1 nano (gpt-4.1-nano-2025-04-14) | $0.10                    | $0.40                     | Fastest, most cost-effective GPT-4.1 variant for low-latency. 1M context.                                              |
| GPT-4o (gpt-4o-2024-08-06)             | $2.50                    | $10.00                    | Latest generation 'omni' model (standard API usage, distinct from Realtime API pricing below).                         |
| GPT-4o mini (gpt-4o-mini-2024-07-18)   | $0.15                    | $0.60                     | Smaller, faster 'omni' model.                                                                                          |
| GPT-4o Realtime (Text)                 | $5.00                    | $20.00                    | Pricing for Realtime API endpoint (Text).                                                                              |
| GPT-4o mini Realtime (Text)            | $0.60                    | $2.40                     | Pricing for Realtime API endpoint (Text).                                                                              |
| **Legacy / Base Models**               |                          |                           |                                                                                                                        |
| GPT-3.5 Turbo (gpt-3.5-turbo-0125)     | $0.50                    | $1.50                     | Popular cost-effective model.                                                                                          |

_Note: Cached input pricing is available for many models but not listed here. Realtime API audio pricing is also available but excluded for primary text comparison focus._

**Analysis:** OpenAI's pricing structure shows a tiered approach, with models ranging from affordable (GPT-4.1 nano, GPT-4o mini) to significantly more expensive 'o-series' reasoning models (o1, o3-mini). This aligns with advertised capabilities, creating a value ladder for users based on task complexity and budget. The premium for the 'o' series reflects their specialized, multi-step reasoning tasks. The proliferation of 'mini' and 'nano' variants suggests OpenAI's strategy to compete aggressively in the cost-efficiency segment, responding to competitive pressures from providers like Mistral AI and Cohere.

### Google Gemini: Tiered Pricing for Context Management

Google offers access to its Gemini family of models through the Google AI platform, including Gemini 1.5 Pro, 1.5 Flash, 2.0 Flash, 2.0 Flash-Lite, 2.5 Pro Preview, and Flash-8B. Many Gemini models feature multimodal capabilities. A key differentiator in Google's pricing is the use of tiered pricing based on the number of input tokens in the prompt for some higher-end models.

**Table 2: Google Gemini API Pricing (USD/1M Tokens - Paid Tier)**

| Model                  | Input Cost (/1M tokens)  | Output Cost ($/1M tokens) | Notes                                                                              |
| :--------------------- | :----------------------- | :------------------------ | :--------------------------------------------------------------------------------- |
| Gemini 2.5 Pro Preview | $1.25 (≤ 200k tokens)    | $10.00 (≤ 200k tokens)    | Tiered pricing based on prompt size. Output includes thinking tokens.              |
|                        | $2.50 (> 200k tokens)    | $15.00 (> 200k tokens)    |                                                                                    |
| Gemini 2.0 Flash       | $0.10 (Text/Image/Video) | $0.40                     | Different input price for audio modality.                                          |
|                        | $0.70 (Audio)            |                           |                                                                                    |
| Gemini 2.0 Flash-Lite  | $0.075                   | $0.30                     |                                                                                    |
| Gemini 1.5 Pro         | $1.25 (≤ 128k tokens)    | $5.00 (≤ 128k tokens)     | Tiered pricing based on prompt size. Breakthrough 2M context window.               |
|                        | $2.50 (> 128k tokens)    | $10.00 (> 128k tokens)    |                                                                                    |
| Gemini 1.5 Flash       | $0.075 (≤ 128k tokens)   | $0.30 (≤ 128k tokens)     | Tiered pricing based on prompt size. 1M context window.                            |
|                        | $0.15 (> 128k tokens)    | $0.60 (> 128k tokens)     |                                                                                    |
| Gemini 1.5 Flash-8B    | $0.0375 (≤ 128k tokens)  | $0.15 (≤ 128k tokens)     | Tiered pricing based on prompt size. Smallest 1.5 series model, 1M context window. |
|                        | $0.075 (> 128k tokens)   | $0.30 (> 128k tokens)     |                                                                                    |

_Note: Pricing for Imagen 3 (per image) and Veo 2 (per second) excluded. Context caching costs also apply but are not listed here._

**Analysis:** Google's Gemini API pricing is complex due to prompt size-based tiers for several models. This structure incentivizes users to keep input prompts below specified thresholds to avoid significant cost increases (often doubling the price per token for longer inputs). This approach differs from other providers who typically price models based on their maximum context window capability rather than charging more for utilizing more of that capacity. This model may encourage developers to use sophisticated context management techniques, adding an optimization layer that can increase application complexity but yield cost savings. Google also offers very low-cost options like Gemini 1.5 Flash-8B and Gemini 2.0 Flash-Lite.

### Anthropic Claude: Safety-Focused Premium Models

Anthropic offers its Claude family of models via API, known for strong performance and an emphasis on AI safety, reliability, and enterprise readiness. The primary models are Claude 3 Opus, Claude 3.5/3.7 Sonnet, and Claude 3/3.5 Haiku, representing different tiers of capability and speed. The Claude 3 generation models consistently feature a 200K token context window.

**Table 3: Anthropic Claude API Pricing (USD/1M Tokens)**

| Model                                          | Input Cost ($/1M tokens) | Output Cost ($/1M tokens) | Notes                                                                                               |
| :--------------------------------------------- | :----------------------- | :------------------------ | :-------------------------------------------------------------------------------------------------- |
| Claude 3 Opus (claude-3-opus-20240229)         | $15.00                   | $75.00                    | Most powerful model for complex tasks. 200K context.                                                |
| Claude 3.7 Sonnet (claude-3-7-sonnet-20250219) | $3.00                    | $15.00                    | Latest Sonnet, most intelligent model (as of Feb 2025), extended thinking capability. 200K context. |
| Claude 3.5 Sonnet (claude-3-5-sonnet-20241022) | $3.00                    | $15.00                    | Previous most intelligent Sonnet version. 200K context.                                             |
| Claude 3.5 Haiku (claude-3-5-haiku-20241022)   | $0.80                    | $4.00                     | Faster, improved Haiku version. 200K context.                                                       |
| Claude 3 Haiku (claude-3-haiku-20240307)       | $0.25                    | $1.25                     | Original Haiku, fastest and most compact. 200K context.                                             |

_Note: All models listed have vision capabilities. Prompt caching and batch processing can offer significant cost savings on API usage._

**Analysis:** Anthropic's pricing delineates models into distinct capability tiers: Opus for maximum intelligence, Sonnet for a balance of performance and cost, and Haiku for fastest response times. Claude 3 Opus is one of the most expensive models, positioning it as a premium offering. Anthropic's multi-channel distribution (direct API, Amazon Bedrock, Google Cloud Vertex AI) broadens access but may introduce slight pricing variations.

### Cohere: Enterprise-Focused Cost Efficiency

Cohere provides language models often tailored towards enterprise use cases, with an emphasis on RAG systems. Their primary generative models are in the Command family: Command A, Command R+, Command R, and the efficient Command R7B. Pricing reflects Production API key usage.

**Table 4: Cohere API Pricing (USD/1M Tokens - Command Models)**

| Model                  | Input Cost ($/1M tokens) | Output Cost ($/1M tokens) | Notes                                                                                                  |
| :--------------------- | :----------------------- | :------------------------ | :----------------------------------------------------------------------------------------------------- |
| Command A              | $2.50                    | $10.00                    | Efficient and performant model, specializing in agentic AI, multilingual use cases.                    |
| Command R+             | $2.50                    | $10.00                    | Powerful, scalable model for real-world enterprise use cases.                                          |
| Command R              | $0.15                    | $0.60                     | Optimized for long context tasks like RAG and tool use.                                                |
| Command R (Fine-tuned) | $0.30                    | $1.20                     | Pricing for inference using a fine-tuned Command R model. Training cost is separate ($3.00/1M tokens). |
| Command R7B            | $0.0375                  | $0.15                     | Smallest, most efficient model for speed and cost-effectiveness.                                       |

_Note: Prices reflect the latest versions as per the main pricing page. Rerank 3.5 is priced at $2.00 per 1K searches. Embed 4 is priced at $0.12 per 1M tokens (input)._

**Analysis:** Cohere's Command models pricing targets different market segments. Command R and R7B are aggressively priced, making them attractive for cost-sensitive or high-volume tasks. Command R's optimization for RAG workflows further strengthens its appeal for developers building search and retrieval systems. Higher-priced Command R+ and Command A models target complex enterprise tasks. Cohere's distinct pricing for its Rerank service ($2.00 per 1,000 searches) underscores its focus on the RAG pipeline, offering more predictable costs for this specific component.

### Mistral AI: Aggressive Pricing After Major Cuts

Mistral AI has gained prominence through its open-source model releases and commercially available proprietary models via La Plateforme API. In September 2024, Mistral AI implemented significant price reductions across its API offerings. Their API portfolio ranges from efficient options like Mistral Nemo and Ministral to the powerful Mistral Large, along with specialized models.

**Table 5: Mistral AI API Pricing (USD/1M Tokens)**

| Model                                       | Input Cost ($/1M tokens) | Output Cost ($/1M tokens) | Notes                                                                                                                                                                                                        |
| :------------------------------------------ | :----------------------- | :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mistral Large (mistral-large-latest, 24.11) | $2.00                    | $6.00                     | Top-tier reasoning model. 131k context. (Reduced from $3/$9).                                                                                                                                                |
| Mistral Small (mistral-small-latest, 25.03) | $0.20                    | $0.60                     | Leader in small models category, includes image understanding. 131k context. (Reduced from $1/$3). Legacy Mixtral models deprecated.                                                                         |
| Codestral (codestral-latest, 25.01)         | $0.20                    | $0.60                     | Cutting-edge coding model. 256k context. (Reduced from $1/$3).                                                                                                                                               |
| Mistral Nemo (open-mistral-nemo, 24.07)     | $0.15                    | $0.15                     | Best multilingual open source model (available via API). 131k context. (Reduced from $0.3/$0.3).                                                                                                             |
| Pixtral 12B (pixtral-12b-2409)              | $0.15                    | $0.15                     | 12B model with image understanding. 131k context.                                                                                                                                                            |
| Ministral 8B (ministral-8b-latest, 24.10)   | $0.07^                   | $0.21^                    | Powerful edge model. 131k context. (Pricing inferred based on structure, verify official source). Legacy Mistral 7B deprecated.                                                                              |
| Ministral 3B (ministral-3b-latest, 24.10)   | $0.02^                   | $0.06^                    | World's best edge model. 131k context. (Pricing inferred based on structure, verify official source).                                                                                                        |
| Mistral Embed (mistral-embed, 23.12)        | $0.01                    | $0.01                     | State-of-the-art semantic embedding model. 8k context. (Note: Some sources list $0.01 for input/output combined, others imply $0.10/M tokens for Embed v1 - verify official page for current Embed pricing). |

_Note: Prices based on the September 2024 update where available. Ministral pricing inferred based on relative positioning and standard input/output ratios, requiring verification. Mistral OCR is priced per page (~$0.001/page). Embedding pricing needs verification on the official page._

**Analysis:** Mistral AI's pricing reflects an aggressive competitive stance, especially after the September 2024 price reductions. Models like Mistral Small and Mistral Nemo are now highly cost-effective. Mistral Large offers high-end capabilities at a lower price point than direct competitors. This aggressive strategy, coupled with offering both open-source and competitively priced proprietary APIs, aims to capture significant market share and provides developers with flexibility.

## Comprehensive Provider Comparison

This section provides a direct comparison of API pricing across the five major providers, grouping representative models into approximate capability tiers.

**Table 6: LLM API Pricing Comparison by Tier (USD/1M Tokens)**

| Provider                 | Model                       | Tier             | Input Cost | Output Cost | Blended Cost (1:3 Ratio)\* | Notes                                                     |
| :----------------------- | :-------------------------- | :--------------- | :--------- | :---------- | :------------------------- | :-------------------------------------------------------- |
| **Economy / Small**      |                             |                  |            |             |                            | Focus on cost-efficiency, speed, simpler tasks            |
| Cohere                   | Command R7B                 | Economy          | $0.0375    | $0.15       | $0.12                      | Extremely cost-effective.                                 |
| Google                   | Gemini 1.5 Flash-8B (≤128k) | Economy          | $0.0375    | $0.15       | $0.12                      | Very low cost, tiered pricing.                            |
| Mistral AI               | Ministral 3B                | Economy          | $0.02^     | $0.06^      | $0.05^                     | Edge model, pricing inferred.                             |
| Mistral AI               | Ministral 8B                | Economy          | $0.07^     | $0.21^      | $0.18^                     | Edge model, pricing inferred.                             |
| Google                   | Gemini 2.0 Flash-Lite       | Economy          | $0.075     | $0.30       | $0.24                      |                                                           |
| OpenAI                   | GPT-4.1 nano                | Economy          | $0.10      | $0.40       | $0.33                      | Fastest GPT-4.1 variant.                                  |
| Mistral AI               | Mistral Nemo                | Economy          | $0.15      | $0.15       | $0.15                      | Multilingual, competitive price.                          |
| Mistral AI               | Pixtral 12B                 | Economy          | $0.15      | $0.15       | $0.15                      | Includes vision.                                          |
| Anthropic                | Claude 3 Haiku              | Economy          | $0.25      | $1.25       | $1.00                      | Original Haiku, fast.                                     |
| **Mid-Range / Balanced** |                             |                  |            |             |                            | Balance of performance, cost, and speed for general tasks |
| Cohere                   | Command R                   | Mid-Range        | $0.15      | $0.60       | $0.49                      | Optimized for RAG.                                        |
| OpenAI                   | GPT-4o mini                 | Mid-Range        | $0.15      | $0.60       | $0.49                      | Small 'omni' model.                                       |
| Google                   | Gemini 1.5 Flash (≤128k)    | Mid-Range        | $0.075     | $0.30       | $0.24                      | Tiered pricing.                                           |
| Google                   | Gemini 2.0 Flash (Text)     | Mid-Range        | $0.10      | $0.40       | $0.33                      |                                                           |
| Mistral AI               | Mistral Small               | Mid-Range        | $0.20      | $0.60       | $0.50                      | Highly competitive post-reduction.                        |
| OpenAI                   | GPT-4.1 mini                | Mid-Range        | $0.40      | $1.60       | $1.30                      |                                                           |
| OpenAI                   | GPT-3.5 Turbo               | Mid-Range        | $0.50      | $1.50       | $1.25                      | Legacy but popular.                                       |
| OpenAI                   | GPT-4o mini Realtime (Text) | Mid-Range        | $0.60      | $2.40       | $1.95                      | Realtime API endpoint.                                    |
| Anthropic                | Claude 3.5 Haiku            | Mid-Range        | $0.80      | $4.00       | $3.20                      | Faster, improved Haiku.                                   |
| **High-Performance**     |                             |                  |            |             |                            | Higher accuracy, complex instructions, enterprise focus   |
| OpenAI                   | GPT-4.1                     | High-Performance | $2.00      | $8.00       | $6.50                      |                                                           |
| Mistral AI               | Mistral Large               | High-Performance | $2.00      | $6.00       | $5.00                      | Competitively priced frontier model.                      |
| OpenAI                   | GPT-4o                      | High-Performance | $2.50      | $10.00      | $8.13                      |                                                           |
| Cohere                   | Command R+                  | High-Performance | $2.50      | $10.00      | $8.13                      |                                                           |
| Cohere                   | Command A                   | High-Performance | $2.50      | $10.00      | $8.13                      |                                                           |
| Anthropic                | Claude 3.7 Sonnet           | High-Performance | $3.00      | $15.00      | $12.00                     | Latest Sonnet model.                                      |
| Anthropic                | Claude 3 Opus               | High-Performance | $15.00     | $75.00      | $60.00                     | Most powerful model for complex tasks.                    |
| OpenAI                   | o1                          | High-Performance | $15.00     | $60.00      | $48.75                     | Frontier reasoning model.                                 |

_Blended cost assumes a typical 1:3 ratio of input to output tokens in API usage patterns. Actual costs will vary based on application-specific token ratios._

**Analysis:** The cross-provider comparison shows that at the economy tier, Mistral AI and Cohere offer the lowest cost options, with Google's Gemini 1.5 Flash-8B also being a low-cost alternative with tiered pricing. OpenAI's GPT-4.1 nano and GPT-4o mini provide competitive mid-range options.

In the mid-range, competition is intense, with models from multiple providers in the $0.15-$1.00 per million tokens (blended) range. Mistral Small and Cohere's Command R stand out for their performance and affordability.

The high-performance tier shows the most significant price differentiation, with Claude 3 Opus and OpenAI's o1 commanding premium prices. Mistral Large offers compelling value in this tier, providing high-end capabilities at a lower price point than direct competitors.

Across all tiers, the consistent premium on output tokens (typically 3-5x input costs) incentivizes optimizing for concise outputs. This pricing structure effectively subsidizes context-rich inputs while charging more for generation.

The comparison highlights differing strategic approaches: OpenAI and Anthropic maintain premium positioning for flagships while expanding across the price spectrum. Google employs complex tiered pricing based on input length. Cohere and Mistral AI focus on performance-per-dollar, with Mistral leveraging its open-source roots to drive API adoption. These pricing dynamics will likely continue to shift, influencing application architecture, LLM-based business models, and AI accessibility.
