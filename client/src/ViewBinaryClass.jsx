import  { useState, useEffect } from "react"
import axios from "axios"

// Components
import GenericAnswer from "./GenericAnswer"
import Question from "./Question"

function ViewBinaryClass() {
  const [data, setData] = useState("")
  // const [currentExample, setCurrentExample] = useState("example1")

  useEffect(() => {
    async function getData(){
      const { data } = await axios.get('http://127.0.0.1:5000/')
      setData(data)

    }
    getData()
  } , [])

  console.log(data)

    return (
        <div className="view-binary-class">
            <div className= "model-display">
              <div className="model-name">
                <h1> GPT-4 </h1>
              </div>

              <nav> other models </nav>
              <div className="score-display">
                <h1> 99% </h1>
              </div>
            </div>

            <div className="dataset-viewer">
              <Question text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
                  Nulla euismod, nisl quis ultricies ultricies, nisl mauris 
                  ultricies diam, vitae ultricies nisl libero nec nisl. 
                  Sed ac nisl at justo mollis condimentum. 
                  Donec quis diam nec nisl ultr" />
              <button> Next </button>
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