import { useState, useEffect } from 'react'


import axios from 'axios'


// import './style/App.css'

// Components 
import Question from './Question'
import ModelAnswer from './ModelAnswer'
import GoldAnswer from './GoldAnswer'

export function AnalyzeDataset() {

  const [data, setData] = useState("")
  const [currentExample, setCurrentExample] = useState("example1")

  useEffect(() => {
    async function getData(){
      const { data } = await axios.get('http://127.0.0.1:5000/')
      setData(data)

    }
    getData()
  } , [])

  console.log(data)

  const handleClick = () => {
    setCurrentExample(
      currentExample === 'example1' ? 'example2' : 
      currentExample === 'example2' ? 'example3' : 
      'example1'
    )
  }

  return(
    <div className='outer-div'>
    <button onClick={handleClick}> NEXT </button>
    <div className='upper'>
      <Question 
        text = {data && data['model_predictions'][currentExample]['question']} 
      />
    </div>
    <div className='lower'>
      <GoldAnswer 
        text = {data && data['model_predictions'][currentExample]['gold_answer']} 
      />
      <ModelAnswer 
        text = {data && data['model_predictions'][currentExample]['model_answer']} 
        score = {data && data['similarities'][currentExample]['cosine_model_gold']} 
        baseline = {data && data['similarities'][currentExample]['cosine_documents_baseline']} 
      /> 

    </div>

  </div>

  )
}

export default AnalyzeDataset