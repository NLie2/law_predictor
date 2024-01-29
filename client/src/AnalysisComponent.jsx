
// Components 
import Question from './Question'
import ModelAnswer from './ModelAnswer'
import GoldAnswer from './GenericAnswer'


import PropTypes from 'prop-types';

function AnalysisComponent( {question, gold_answer, model_answer, score, baseline}){
  return(
    <>
      <div className='upper'>
        <Question 
          text = {question && question} 
        />
      </div>
      <div className='lower'>
        <GoldAnswer 
          type = 'Gold Answer'
          text = {gold_answer && gold_answer} 
        />
        <ModelAnswer 
          text = {model_answer && model_answer} 
          score = {score && score} 
          baseline = {baseline && baseline} 
        /> 

      </div>
    </>
  )
}

AnalysisComponent.propTypes = {
  question: PropTypes.string.isRequired,
  gold_answer: PropTypes.string.isRequired,
  model_answer: PropTypes.string.isRequired,
  score: PropTypes.string.isRequired,
  baseline: PropTypes.string.isRequired
};

export default AnalysisComponent