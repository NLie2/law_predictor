import PropTypes from 'prop-types';
import './style/Question.css';

function Question({ text }) {
  return (
    <div className="question">
      <h1>Case/ Question</h1>
      <p> {text} </p>
    </div>
  );
}

Question.propTypes = {
  text: PropTypes.string.isRequired,
};

export default Question;
