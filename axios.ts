import axios, { AxiosHeaders, AxiosRequestConfig } from "axios"

const headers: AxiosHeaders = new AxiosHeaders()
headers.setAuthorization('Bearer sk-f03579d24cf7424cb878c47c625b8b12')
headers.setContentType('application/json')
headers.setAccept('application/json')

// const config: AxiosRequestConfig = {
//   method: 'get',
//   baseURL: 'https://api.deepseek.com/models',
//   headers: headers
// }

// axios(config)
//   .then(ret => {
//     // console.log(ret)
//     const data = ret.data.data
//     console.log(data)
//   })
//   .catch(error => {
//     console.error(error)
//   })

// const data: any = JSON.stringify({
//   model: 'deepseek-chat',
//   prompt: '从前山上有座庙',
//   echo: true,
//   frequency_penalty: 1.2,
//   max_tokens: 128,
//   stop: '废都'
// })

  const data = {
  "model": "deepseek-chat",
  "prompt": "Once upon a time, ",
  "echo": false,
  "frequency_penalty": 0,
  "logprobs": 0,
  "max_tokens": 1024,
  "presence_penalty": 0,
  "stop": null,
  "stream": false,
  "stream_options": null,
  "suffix": null,
  "temperature": 1,
  "top_p": 1
  }


const config: AxiosRequestConfig = {
  method: 'post',
  baseURL: 'https://api.deepseek.com/beta/completions',
  headers: headers,
  data: data,
  timeout: 120 * 1000
}

axios(config)
  .then(ret => {
    console.log(ret.data)
  })
  .catch(error => {
    console.error(error)
  })