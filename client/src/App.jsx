import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './style/App.css'

// Components 
import Question from './Question'
import ModelAnswer from './ModelAnswer'
import GoldAnswer from './GoldAnswer'

function App() {
  const [count, setCount] = useState(0)

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
