import PropTypes from 'prop-types';

// import './style/ModelAnswer.css'


function ModelAnswer( {text, score, baseline} ){

  return(
    <div className="model-answer">
      <h1>Model Answer</h1>
      
      <div className="text-component"> 
        <div className="score-display">
          <h1> {score} </h1>
          <h2> Baseline {baseline} </h2>
        </div>
        <div className="textbox">
          <p> {text} </p>
        </div>
      </div>
    </div>

  )
}

ModelAnswer.propTypes = {
  text: PropTypes.string.isRequired,
  score: PropTypes.number.isRequired, 
  baseline: PropTypes.number.isRequired
};

export default ModelAnswer