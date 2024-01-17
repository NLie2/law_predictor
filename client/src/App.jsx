
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import NavBar from './NavBar'
import AnalyseDataset from './AnalyseDataset'
import TestYourOwn from './TestYourOwn'
import GetAdvice from './GetAdvice'






function App() {


  return (
    <>
      <BrowserRouter>
        <NavBar />
        <main>
          <Routes>  */
          <Route path='/' element= {<AnalyseDataset />} />
            <Route path='/analysedataset/' element= { <AnalyseDataset /> } />
            <Route path='/testyourownlawcase/' element= { <TestYourOwn /> } />
            <Route path='/getlegaladvice/' element= { <GetAdvice /> } />

          </Routes>
        </main>
      </BrowserRouter>

    </>
  )
}

export default App
