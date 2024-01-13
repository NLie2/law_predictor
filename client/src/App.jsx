import { useState } from 'react'
import { useEffect } from 'react'
import axios from 'axios'


import './style/App.css'

// Components 
import Question from './Question'
import ModelAnswer from './ModelAnswer'
import GoldAnswer from './GoldAnswer'


function App() {
  const [message, setMessage] = useState("")

  useEffect(() => {
    async function getData(){
      const { data } = await axios.get('http://127.0.0.1:5000/')
      setMessage(data)

    }
    getData()
  } , [])

  console.log(message)


  return (
    <div className='outer-div'>
      <div className='upper'>
        <Question />
      </div>
      <div className='lower'>
        <GoldAnswer />
        <ModelAnswer /> 

      </div>

    </div>
  )
}

export default App
