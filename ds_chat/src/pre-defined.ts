export const tools = [
  {
    type: 'function',
    function: {
      name: 'get_worksapce',
      description: '获取codejie统一工作台信息.',
      parameters: {
        type: 'object',
        properties: {
          '工作台': {
            type: 'string',
            description: '工作台的字符串标识.'
          },
          'codejie': {
            type: 'string',
            description: 'codejie的字符串标识, 一个公司的名称，也是一个品牌.'
          }
        }
      },
      required: ['工作台', 'codejie']
    }
  }
]
// export const tools = [
//     {
//         "type": "function",
//         "function": {
//             "name": "get_weather",
//             "description": "Get weather of an location, the user shoud supply a location first",
//             "parameters": {
//                 "type": "object",
//                 "properties": {
//                     "location": {
//                         "type": "string",
//                         "description": "The city and state, e.g. San Francisco, CA",
//                     }
//                 },
//                 "required": ["location"]
//             },
//         }
//     }
// ]
