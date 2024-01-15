
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import NavBar from './NavBar'
import AnalyzeDataset from './AnalzeDataset'
import TestYourOwn from './TestYourOwn'
import GetAdvice from './GetAdvice'






function App() {


  return (
    <>
      <BrowserRouter>
        <NavBar />
        <main>
          <Routes>  */
          <Route path='/' element= {<AnalyzeDataset />} />
            <Route path='/analyzedataset/' element= { <AnalyzeDataset /> } />
            <Route path='/testyourownlawcase/' element= { <TestYourOwn /> } />
            <Route path='/getlegaladvice/' element= { <GetAdvice /> } />

          </Routes>
        </main>
      </BrowserRouter>

    </>
  )
}

export default App
