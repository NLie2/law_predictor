import Container from 'react-bootstrap/Container'
import Nav from 'react-bootstrap/Nav'

import Navbar from 'react-bootstrap/Navbar'

import { Link } from 'react-router-dom'


function NavBar(  ) {

  return (
    <Navbar expand="lg" className="bg-body-tertiary shadow-lg">
      <Container className='navbar'>
        <Nav className="me-auto">
          <Link to="/analyzedataset/">Analyze Dataset</Link>
          <Link to="/testyourownlawcase/">Test on your own lawcase</Link>
          <Link to="/getlegaladvice/">Get legal advice</Link>
        </Nav>
      </Container>
    </Navbar>
  )
}

export default NavBar