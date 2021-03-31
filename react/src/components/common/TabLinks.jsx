import React from "react";
import { NavLink } from "react-router-dom";

function Tabs() {
  const activeStyle = { color: "gold"};
  return (
    <nav>
      <br></br>
      <h5>
        <NavLink activeStyle={activeStyle} exact to="/">
        Home
        </NavLink>
        <NavLink activeStyle={activeStyle} style={{marginLeft: "36px"}} to="/courses">
        Courses
        </NavLink>
        <NavLink activeStyle={activeStyle} style={{marginLeft: "36px"}} to="/about">
        About
        </NavLink>
      </h5>
    </nav>
  );
}

export default Tabs;
