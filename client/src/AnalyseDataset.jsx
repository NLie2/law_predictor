import { useState, useEffect } from 'react'


import axios from 'axios'


// Components
import AnalysisComponent from './AnalysisComponent'



export function AnalyseDataset() {

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
    <AnalysisComponent
      question = {data && data['model_predictions'][currentExample]['question']}
      gold_answer = {data && data['model_predictions'][currentExample]['gold_answer']}
      model_answer = {data && data['model_predictions'][currentExample]['model_answer']}
      score = {data && data['similarities'][currentExample]['cosine_model_gold']} 
      baseline = {data && data['similarities'][currentExample]['cosine_documents_baseline']}
      
    />

  </div>

  )
}



export default AnalyseDataset