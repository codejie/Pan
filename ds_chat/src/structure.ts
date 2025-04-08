export interface ChatMessageRequestMessage {
  role: string,
  content: string,
  name?: string,
  prefix?: boolean,
  reasoning_content?: string
  tool_calls?: {
    id: string,
    type: 'function',
    function: {
      name: string,
      arguments: string
    }
  }[]
  tool_call_id?: string
}

export interface ChatMessageRequest {
  model: 'deepseek-chat' | 'deepseek-reasoner',
  messages: ChatMessageRequestMessage[],
  response_format?: {
    type: 'json_object' | 'text'
  },
  max_tokens?: number,
  temperature?: number,
  top_p?: number,
  frequency_penalty?: number,
  presence_penalty?: number,
  stop?: string | string[],
  logprobs?: number,
  stream?: boolean,
  stream_openai?: any
}

export interface ChatMessageResponseChoice {
  finish_reason: 'stop' | 'length' | 'content_filter' | 'tool_calls' | 'insufficient_system_resource',
  index: number,
  message: {
    role: 'assistant'
    content: string,
    reasoning_content?: string,
    tool_calls?: {
      id: string,
      type: 'function',
      function: {
        name: string,
        arguments: string
      }
    }[]
  },
  logprobs?: {
    content: {
      token: string,
      logprob: number
      bytes?: number[],
      top_logprobs?: {
        token: string,
        logprob: number
        bytes?: number[]
      }[]
    }[]
  }
}

export interface ChatMessageResponse {
  model: string,
  id: string,
  created: number,
  choices: ChatMessageResponseChoice[],
  system_fingerprint: string,
  object: 'chat.completion'
  usage: {
    completion_tokens: number,
    prompt_tokens: number,
    prompt_cache_hit_tokens: number,
    prompt_cache_miss_tokens: number,
    total_tokens: number,
    completion_tokens_details: {
      cached_tokens: number
    }
  }
}

///
// export interface ChatMessageCodeContent {
//   content: string,
//   language?: string,
//   code?: string
// }