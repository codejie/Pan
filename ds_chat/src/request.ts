import axios, { AxiosHeaders, AxiosResponse } from "axios";
import { ChatMessageRequestMessage, ChatMessageResponseChoice } from "./structure";
import { token } from "../token.json";

const _base_url: string = 'https://api.deepseek.com'
const _token: string = token

const _urls: { [key in string]: string } = {
  'chat': '/chat/completions',
  'beta': '/beta/completions'
}

const _headers = new AxiosHeaders( {
    // 'Content-Type': 'application/json',
    'Content-Type': 'application/json',
    // 'Accept': 'application/json',
    'Accept': 'application/json', //,text/event-stream',
    'Authorization': 'Bearer ' + _token,
    'Connection': 'keep-alive'
})

function _request(type: string, data: any, method: string = 'post'): Promise<AxiosResponse<any, any>> {
  return axios({
    headers: _headers,
    url: _base_url + _urls[type],
    method: method,
    data: data
  })  
}

export function request_chat(msgs: ChatMessageRequestMessage[], extra: any = undefined): Promise<ChatMessageResponseChoice[]> {
  const data = {
    model: 'deepseek-chat',
    messages: msgs,
    // response_format: {
    //   type: 'json_object'
    // },
    // stream: true,
    ...extra
  }
  return new Promise<ChatMessageResponseChoice[]>((resolve, reject) => {
    _request('chat', data, 'post')
      .then(ret => {
        // const chioces = ret.data.chioces
        resolve(ret.data.choices) 
      })
      .catch(err => {
        reject(err)
      })
  })
}

// function _stream(type: string, data: any, method: string = 'post'): Promise<void> {
//   return new Promise<void>((resolve, reject) => {
//     axios({
//       headers: _headers,
//       url: _base_url + _urls[type],
//       method: method,
//       data: data,
//       // responseType: 'stream'
//     })
//       .then(ret => {
//         const source = new EventSource(ret.config.url!)
//         source.onmessage = (event) => {
//           console.log(event.data)
//         }
//         source.onerror = (event) => {
//           console.log(event)
//         }
//         resolve()
//       })
//       .catch(err => {
//         reject(err)
//       })
//   })
// }

// export function stream_chat(msgs: ChatMessageRequestMessage[], extra: any = undefined): Promise<void> {
//   const data = {
//     model: 'deepseek-chat',
//     messages: msgs,
//     response_format: {
//       type: 'json_object'
//     },
//     stream: true,
//     ...extra
//   }
//   return _stream('chat', data, 'post')
// }
