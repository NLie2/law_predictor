/* eslint-disable react/prop-types */
// import './DropdownMenu.css'; // Make sure to create this CSS file

function DropdownMenu( { links }){
    return (
      <div className="dropdown">
        <button className="menu-button">Menu</button>
        <div className="dropdown-content">
          <a href="#"> { links[0] }</a>
          <a href="#">{ links[1] }</a>
          <a href="#">{ links[2] }</a>
        </div>
      </div>
    );

}

export default DropdownMenu;