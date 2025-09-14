AI Companies Are Copying Each Other's Homework to Make Cheap Models
By Emma Cosgrove and Hugh Langley
Mar 7, 2025, 11:00 AM MEZ

The Price of Building AI Is Falling to New Lows
New, cheaper AI-development techniques have developers rejoicing — but it's not all upside.
As costs hit rock bottom, Big Tech foundation model builders must justify expensive offerings.

How Much Does It Cost to Start an AI Company?
The answer: less and less each day, as large language models (LLMs) are being created for smaller and smaller sums.

The cost of AI computing is falling.

A technique called distillation is making it cheaper to build decent LLMs.

This shift excites some and alarms others in the AI ecosystem.

What Is Distillation?
Distillation is, at its core, using one model to improve another:

A larger "teacher" model is prompted to generate responses and paths of reasoning.

A smaller "student" model mimics the behavior of the teacher.

Recent Examples of Distillation in Action
DeepSeek reportedly trained OpenAI-competitive models for about $5 million, sparking fears about reduced chip demand (Nvidia briefly lost $600B in market cap).

UC Berkeley researchers trained two models for under $1,000 in computing costs.

Stanford, University of Washington, and Allen Institute for AI trained a serviceable reasoning model for even less.

Why Developers Love Distillation
It allows improvement during training at much lower cost than other methods.

Developers use it along with fine-tuning to specialize foundation models.

Example: Taking Meta’s Llama and using DeepSeek’s R1 model to turn it into a US tax law expert.

“Perhaps the most interesting part of the R1 paper was being able to turn non-reasoning smaller models into reasoning ones.”
— SemiAnalysis, January 2025

Advantages of Distillation
Smaller footprint

“You can run it on your phone. You could run it on edge devices.”
— Samir Kumar, Touring Capital

Better performance
DeepSeek’s distilled models sometimes outperformed their larger counterparts.

The Technique Isn’t New — But the Landscape Is
Originally introduced in a 2015 paper by Google AI veterans including Geoffrey Hinton and Oriol Vinyals.

Rejected at the time from NeurIPS due to perceived lack of impact.

Now resurging due to:

Abundance of powerful open-source teacher models

Communities like Hugging Face

“DeepSeek is eroding the competitive moat of big model providers.”
— Kate Soule, IBM

How Far Can Distillation Go?
Hugging Face hosts 30,000+ models with “distill” in the name.

Still, none have reached the leaderboard.

Downsides of Distillation
Specializing a model can reduce performance in non-targeted areas.

Apple researchers attempted to define a "distillation scaling law":

Distillation beats supervised learning only when:

The teacher is high-quality

The teacher is larger (but not too large)

Resources are well-aligned

Despite the limits, distillation lowers the barrier to entry and accelerates AI prototyping.

Are Foundation Models Doomed?
“Just about every AI developer in the world today is using DeepSeek’s R1 to distill new models.”
— Jensen Huang, Nvidia CEO

The Rising Threat to Proprietary Models
Distillation threatens massive, expensive models from OpenAI and Anthropic.

Experts say:

Foundation models are becoming commoditized

Future value lies in products, not just models

“There’s a limit that pretrained models can achieve, and we’re getting closer to that wall.”
— Jasper Zhang, Hyperbolic

Can Big Tech Fight Back?
Some companies are removing reasoning traces from their models to prevent distillation.

OpenAI’s o1 hides reasoning paths; o3-mini reveals them.

“Leading AI companies will try to prevent distillation.”
— David Sacks, Trump AI Advisor, January 2025

Yet, controlling distillation may be impossible in the open-source world.

“Anyone can go to Hugging Face and find tons of GPT-generated datasets … likely taken without the rights to do so.”
— Kate Soule, IBM

Final Note
Anthropic and OpenAI did not respond to requests for comment.
