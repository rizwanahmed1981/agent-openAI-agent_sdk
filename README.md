┌──────────────────────┐
│   User Input (query) │
└────────────┬─────────┘
             ▼
┌─────────────────────────────┐
│         Runner.run_sync     │
└────────────┬────────────────┘
             ▼
     ┌────────────────┐
     │     Agent      │
     └──────┬─────────┘
            ▼
┌──────────────────────────────┐
│  OpenAIChatCompletionsModel  │ (Gemini backend)
│    using AsyncOpenAI Client  │
└──────────────────────────────┘
#   a g e n t - o p e n A I - a g e n t _ s d k  
 #   a g e n t - o p e n A I - a g e n t _ s d k  
 