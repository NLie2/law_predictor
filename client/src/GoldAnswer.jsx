// import './style/GoldAnswer.css'

import PropTypes from 'prop-types';

function GoldAnswer({ text }) {
  return (
    <div className="gold-answer">
      <h1>Gold Answer</h1>
      <div className='text-component'>
        <div className='textbox'>
          <p> {text} </p>
        </div>
      </div>
    </div>
  );
}

GoldAnswer.propTypes = {
  text: PropTypes.string.isRequired,
};

export default GoldAnswer