// import './style/GoldAnswer.css'

import PropTypes from 'prop-types';

function GenericAnswer({ type, text }) {
  return (
    <div className="gold-answer">
      <h1>{type}</h1>
      <div className='text-component'>
        <div className='textbox'>
          <p> {text} </p>
        </div>
      </div>
    </div>
  );
}

GenericAnswer.propTypes = {
  type: PropTypes.string.isRequired,
  text: PropTypes.string.isRequired,
};

export default GenericAnswer