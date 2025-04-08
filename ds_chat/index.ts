import { request_chat } from "./src/request"
import { ChatMessageRequestMessage, ChatMessageResponseChoice } from "./src/structure"
import { tools } from './src/pre-defined'

async function main() {
  console.log('start')
  const data: ChatMessageRequestMessage[] = [
    {
      role: 'user',
      content: '有什么关于codejie统一工作台的信息吗？'
    }
  ]
  const ret: ChatMessageResponseChoice[] = await request_chat(data, { tools: tools})
  console.log(ret)  
  const ret_msg = ret[0].message
  const tool = ret_msg.tool_calls ? ret_msg.tool_calls[0] : undefined
  const ret_data: ChatMessageRequestMessage = {
    role: ret_msg.role,
    content: ret_msg.content,
    tool_calls: ret_msg.tool_calls
  }
  data.push(ret_data)
  const tool_data: ChatMessageRequestMessage = {
    role: 'tool',
    tool_call_id: tool?.id,
    content: 'it is very good.',
    name: 'get_worksapce'
  }
  data.push(tool_data)
  const ret1 = await request_chat(data, { tools: tools})
  console.log(ret1)

  const more_data: ChatMessageRequestMessage = {
    role: 'user',
    content: '请问用户具体反馈是什么内容？'
  }
  data.push(more_data)
  const ret2: ChatMessageResponseChoice[] = await request_chat(data, { tools: tools})
  console.log(ret2)
}

// async function main() {
//   console.log('start')
//   const data: ChatMessageRequestMessage[] = [
//     {
//       role: 'user',
//       content: "How's the weather in Hangzhou?"
//     }
//   ]
//   const ret: ChatMessageResponseChoice[] = await request_chat(data, { tools: tools})
//   console.log(ret)  
//   const ret_msg = ret[0].message
//   const tool = ret_msg.tool_calls ? ret_msg.tool_calls[0] : undefined
//   const ret_data: ChatMessageRequestMessage = {
//     role: ret_msg.role,
//     content: ret_msg.content,
//     tool_calls: ret_msg.tool_calls
//   }
//   data.push(ret_data)
//   const tool_data: ChatMessageRequestMessage = {
//     role: 'tool',
//     tool_call_id: tool?.id,
//     content: '24.'
//   }
//   data.push(tool_data)
//   const ret1 = await request_chat(data, { tools: tools})
//   console.log(ret1)
// }


main()