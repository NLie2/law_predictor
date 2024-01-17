import AnalysisComponent from "./AnalysisComponent"
import { useState, useEffect } from 'react'  
import axios from 'axios'

function TestYourOwn(){

  const [question, setQuestion] = useState("")
  const [gold_answer, setGoldAnswer] = useState("")
  const [model_answer, setModelAnswer] = useState("")
  const [score, setScore] = useState("")
  const [baseline, setBaseline] = useState("")
  const [data, setData] = useState("")

  useEffect(() => {
    async function getData(){
      setQuestion(data['question'])
      setGoldAnswer(data['gold_answer'])
      setModelAnswer(data['model_answer'])
      setScore(data['score'])
      setBaseline(data['baseline'])

    }
    getData()
  } , [data])



  const handleClick = async() => {
    const { data } = await axios.get('http://127.0.0.1:5000/query')
    setData(data)
    console.log(data)

  }

  return(
    <div className='outer-div'> 
      <button onClick={handleClick}> Query Model </button>

      <AnalysisComponent
        question = {question}
        gold_answer = {gold_answer}
        model_answer = {model_answer}
        score = {score} 
        baseline = {baseline}
      />
    </div>
  )
}
export default TestYourOwn