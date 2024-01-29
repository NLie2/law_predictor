import  { useState, useEffect } from "react"
import axios from "axios"

// Components
import GenericAnswer from "./GenericAnswer"
import Question from "./Question"
import DropdownMenu from "./Dropdown"

// bootstrap components
// import Dropdown from 'react-bootstrap/Dropdown'
// import DropdownButton from 'react-bootstrap/DropdownButton';

function ViewBinaryClass() {
  const [data, setData] = useState("")
  const [currentExample, setCurrentExample] = useState(0)

  useEffect(() => {
    async function getData(){
      const { data } = await axios.get('http://127.0.0.1:5000/get_dataset')
      setData(data)
      setCurrentExample( 0 )

    }
    getData()
  } , [])

  console.log(data)
  console.log(currentExample)

  function handleClick(){
    setCurrentExample( currentExample + 1 )
  }


    return (
        <div className="view-binary-class">
            <div className= "model-display">
              <div className="model-name">
                <h1> GPT-4 </h1>
              </div>
              <DropdownMenu links = { [ 'GPT-3.5-turbo', 'GPT-4', 'GPT-4-ethics-prompt']}/>

              <div className="score-display">
                <h1> 99% </h1>
              </div>
            </div>

            <div className="dataset-viewer">
              <Question text= { data[String(currentExample)]['Question/Case Description']} />
              <button onClick={handleClick}> Next </button>
              <div className="model-gold-answers">
                <div className="gold-Answer">
                  <GenericAnswer type="Gold Answer" text="Lorem ipsum dolor sit amet, consectetur adipiscing elit." />
                </div>
                <div className="model-Answer">
                  <GenericAnswer type="Model Answer" text="Lorem ipsum dolor sit amet, consectetur adipiscing elit." />
                </div>
              </div>
            </div>
        </div>
    )
}

export default ViewBinaryClass